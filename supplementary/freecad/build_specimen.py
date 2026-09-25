"""Reconstruct the nominal PETG adhesive specimen and export TechDraw projections.

Run with the Python bundled in FreeCAD 1.1.3, e.g.:
  PYTHONPATH=/path/to/FreeCAD/usr/lib /path/to/FreeCAD/AppRun python build_specimen.py
The script uses the STL as the measured source; it does not alter that STL or the
existing publication figures.
"""
from pathlib import Path
import math
import struct
import html
import FreeCAD as App
import Part
import Sketcher
import TechDraw

ROOT = Path(__file__).resolve().parents[2]
STL = ROOT / "supplementary/stl/adhesive-test-specimen.stl"
FCSTD = ROOT / "supplementary/freecad/specimen-reconstruction.FCStd"
SVG = ROOT / "media/figures/specimen-freecad-candidate.svg"
TEMPLATE = Path(__file__).with_name("specimen-sheet-template.svg")

# Nominal sections inferred from the STL (millimetres).
BASE_RADIUS = 12.5
BASE_HEIGHT = 3.0
TRANSITION_HEIGHT = 1.5
TOTAL_HEIGHT = 13.0
HEX_ACROSS_FLATS = 21.0
HEX_RADIUS = HEX_ACROSS_FLATS / math.sqrt(3.0)
HEX_ANGLE = math.atan2(-0.21775, 12.1224)
BONDING_GAP = 3.0
V = App.Vector


def stl_bounds(path):
    data = path.read_bytes()
    count = struct.unpack_from("<I", data, 80)[0]
    if len(data) != 84 + 50 * count:
        raise ValueError("STL triangle count does not match file length")
    points = []
    for i in range(count):
        tri = struct.unpack_from("<12fH", data, 84 + 50 * i)
        points.extend((tri[j], tri[j + 1], tri[j + 2]) for j in (3, 6, 9))
    low = tuple(min(p[j] for p in points) for j in range(3))
    high = tuple(max(p[j] for p in points) for j in range(3))
    return count, low, high


count, low, high = stl_bounds(STL)
assert count == 384
assert abs((high[0] - low[0]) - 25.0) < 0.02
assert abs((high[2] - low[2]) - 13.0) < 0.001

doc = App.newDocument("PETGSpecimenReconstruction")
base = doc.addObject("Part::Cylinder", "Base")
base.Label = "01  Circular base — Ø25 × 3 mm"
base.Radius = BASE_RADIUS
base.Height = BASE_HEIGHT

round_section = doc.addObject("Sketcher::SketchObject", "RoundSection")
round_section.Label = "02  Round transition section — z = 3 mm"
round_section.Placement.Base.z = BASE_HEIGHT
round_section.addGeometry(Part.Circle(V(), V(0, 0, 1), BASE_RADIUS), False)

hex_section = doc.addObject("Sketcher::SketchObject", "HexSection")
hex_section.Label = "03  Hex transition section — z = 4.5 mm"
hex_section.Placement.Base.z = BASE_HEIGHT + TRANSITION_HEIGHT
corners = [V(HEX_RADIUS * math.cos(HEX_ANGLE + i * math.pi / 3),
             HEX_RADIUS * math.sin(HEX_ANGLE + i * math.pi / 3), 0) for i in range(6)]
for i in range(6):
    hex_section.addGeometry(Part.LineSegment(corners[i], corners[(i + 1) % 6]), False)

transition = doc.addObject("Part::Loft", "Transition")
transition.Label = "04  Ruled round-to-hex transition — 1.5 mm"
transition.Sections = [round_section, hex_section]
transition.Solid = True
transition.Ruled = True

hex_drive = doc.addObject("Part::Extrusion", "HexDrive")
hex_drive.Label = "05  Hex drive — 21 mm across flats"
hex_drive.Base = hex_section
hex_drive.Dir = V(0, 0, TOTAL_HEIGHT - BASE_HEIGHT - TRANSITION_HEIGHT)
hex_drive.Solid = True

specimen = doc.addObject("Part::MultiFuse", "Specimen")
specimen.Label = "Reconstructed specimen — nominal solid"
specimen.Shapes = [base, transition, hex_drive]
specimen.Refine = True
specimen.addProperty("App::PropertyString", "SourceSTL", "Provenance")
specimen.SourceSTL = "supplementary/stl/adhesive-test-specimen.stl"
specimen.addProperty("App::PropertyString", "Reconstruction", "Provenance")
specimen.Reconstruction = "Nominal analytic reconstruction; transition approximated by a ruled loft. STL remains the source geometry."

doc.recompute()
if specimen.Shape.isNull() or not specimen.Shape.isValid() or len(specimen.Shape.Solids) != 1:
    raise RuntimeError("The reconstructed specimen is not one valid solid")
# The BRep's conservative bounding box can include control-point overshoot;
# tessellation gives the actual nominal outside envelope.
vertices, _ = specimen.Shape.tessellate(0.03)
assert max(math.hypot(p.x, p.y) for p in vertices) <= BASE_RADIUS + 0.001
assert abs(max(p.z for p in vertices) - TOTAL_HEIGHT) < 0.001

# Two editable links place their bonded faces at x = -1.5 and +1.5 mm.
left = doc.addObject("App::Link", "LeftSpecimen")
left.Label = "Left specimen — bonded face at x = -1.5 mm"
left.setLink(specimen)
left.Placement = App.Placement(V(-BONDING_GAP / 2, 0, 0), App.Rotation(V(0, 0, 1), V(-1, 0, 0)))
right = doc.addObject("App::Link", "RightSpecimen")
right.Label = "Right specimen — bonded face at x = +1.5 mm"
right.setLink(specimen)
right.Placement = App.Placement(V(BONDING_GAP / 2, 0, 0), App.Rotation(V(0, 0, 1), V(1, 0, 0)))
assembly = doc.addObject("App::DocumentObjectGroup", "BondingArrangement")
assembly.Label = "Bonding arrangement — 3 mm face-to-face gap"
assembly.addObject(left)
assembly.addObject(right)

# Keep only the two placed links visible in the initial 3D view.
for obj in (base, round_section, hex_section, transition, hex_drive, specimen):
    obj.Visibility = False
left.Visibility = True
right.Visibility = True

page = doc.addObject("TechDraw::DrawPage", "DrawingPage")
page.Label = "Orthographic views and opposed specimen projection"
template = doc.addObject("TechDraw::DrawSVGTemplate", "DrawingTemplate")
template.Template = str(TEMPLATE)
page.Template = template


def make_view(name, label, sources, direction, x, y, scale=2.8):
    view = doc.addObject("TechDraw::DrawViewPart", name)
    view.Label = label
    view.Source = sources
    view.Direction = V(*direction)
    view.Scale = scale
    view.HardHidden = False
    view.SmoothHidden = False
    view.SeamHidden = False
    page.addView(view)
    view.X = x
    view.Y = y
    return view


side = make_view("SideView", "Side — single specimen", [specimen], (0, -1, 0), 95, 220)
top = make_view("TopView", "Top — hex drive", [specimen], (0, 0, -1), 295, 220)
bottom = make_view("BottomView", "Bottom — bonded face", [specimen], (0, 0, 1), 95, 95)
projected = make_view("OpposedProjection", "Opposed pair — axonometric", [left, right], (1, -1, 1), 295, 95, 2.5)
doc.recompute()
for view in (side, top, bottom, projected):
    if view.getStatusString() != "Valid":
        raise RuntimeError(f"TechDraw view {view.Name}: {view.getStatusString()}")

FCSTD.parent.mkdir(parents=True, exist_ok=True)
SVG.parent.mkdir(parents=True, exist_ok=True)
doc.saveAs(str(FCSTD))


def view_svg(view, cx, cy, scale):
    code = TechDraw.viewPartAsSvg(view)
    code = code.replace('stroke-width="0.7"', 'stroke-width="0.14"')
    code = code.replace('stroke-width="0.35"', 'stroke-width="0.10"')
    return f'<g transform="translate({cx} {cy}) scale({scale})">{code}</g>'


panels = [
    ("01 / SIDE", "Single specimen • circular base, transition and hex drive", side, 400, 320, 12.0),
    ("02 / TOP", "Hex drive end • 21.0 mm across flats", top, 1200, 320, 12.0),
    ("03 / BOTTOM", "Circular bonded face • nominal Ø25.0 mm", bottom, 400, 825, 12.0),
    ("04 / OPPOSED PAIR", "Bonded faces facing • 3.0 mm clear gap before assembly", projected, 1200, 825, 11.0),
]
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1120" viewBox="0 0 1600 1120">',
         '<rect width="1600" height="1120" fill="white"/>',
         '<g font-family="Arial,Helvetica,sans-serif" fill="#17212b">',
         '<text x="65" y="48" font-size="34" font-weight="700">PETG adhesive test specimen</text>',
         '<text x="65" y="80" font-size="18">FreeCAD reconstruction from the supplied STL · review candidate · dimensions in mm</text>',
         '</g>']
for i, (title, subtitle, view, cx, cy, scale) in enumerate(panels):
    x0 = 50 if i % 2 == 0 else 820
    y0 = 110 if i < 2 else 600
    parts += [f'<rect x="{x0}" y="{y0}" width="730" height="460" rx="10" fill="none" stroke="#bdc6ce" stroke-width="1.5"/>',
              f'<text x="{x0+26}" y="{y0+42}" font-family="Arial,Helvetica,sans-serif" font-size="22" font-weight="700" fill="#17212b">{html.escape(title)}</text>',
              f'<text x="{x0+26}" y="{y0+72}" font-family="Arial,Helvetica,sans-serif" font-size="16" fill="#4d5966">{html.escape(subtitle)}</text>',
              view_svg(view, cx, cy, scale)]
parts += ['<text x="65" y="1093" font-family="Arial,Helvetica,sans-serif" font-size="15" fill="#4d5966">Nominal reverse engineering: Ø25 × 3 base, 1.5 transition, 21 across flats, 13 overall. The STL mesh is the dimensional reference.</text>', '</svg>']
SVG.write_text('\n'.join(parts))
print('FreeCAD:', FCSTD)
print('SVG:', SVG)
print('Solid volume:', round(specimen.Shape.Volume, 3), 'mm^3')
print('Gap:', BONDING_GAP, 'mm')
