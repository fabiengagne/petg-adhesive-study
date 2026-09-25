# Internal Verification Report: SOARFLY YX01-24 Digital Torque Wrench

## Purpose

This internal test was performed to check the indication of the digital torque wrench used for the PETG adhesive torsion tests against torques generated from known masses applied at measured lever-arm distances. The verification was intended as an in-house functional check only. It was not a traceable calibration. The reference masses used for the verification were weighed to **±1 g** before use.

## Instrument

- **Instrument:** Digital torque wrench
- **Brand:** SOARFLY
- **Model:** YX01-24
- **Display resolution:** **0.1 N·m**
- **Commercially stated accuracy:** ±1 % (no traceable calibration certificate available)
- **Commercially stated maximum capacity:** 220 N·m

## Test principle

A known mass, measured to **±1 g**, was used to generate a force under gravity. The force was applied at a measured perpendicular distance from the torque axis. The reference torque was calculated as (T = F r = m g r), using (g = 9.81 mathrm{m/s^2}).

For each test point, the load was applied continuously for **at least 4 s** before the instrument reading was recorded.

Two masses appear in the handwritten notes:

- **2.0 kg**, corresponding to **19.62 N** using (g = 9.81 mathrm{m/s^2});
- **4.2 kg**, corresponding to approximately **41.2 N**.

## Narrative description of the test

The torque wrench was arranged so that a known gravitational load produced a moment about the wrench axis at a measured lever arm. A reference mass was applied at the selected distance from the axis. The load was brought onto the wrench and maintained for a minimum of 4 s so that a stable indication could be observed and recorded. The indicated torque was then compared with the torque calculated from the applied force and the measured lever arm.

Several lever-arm distances were used in order to check the instrument response at multiple torque levels. The original handwritten notes are preserved with this report because several entries are difficult to read and will be confirmed before the report is considered final.

## Preliminary transcription of handwritten notes

The table below is a **preliminary transcription**. Entries marked **[to confirm]** are not considered authoritative until checked against the original test recollection.

| Mass | Force | Lever arm | Instrument indication | Reference torque calculated from mass and arm | Status |
|---:|---:|---:|---:|---:|---|
| 2.0 kg | 19.62 N | 0.300 m | approx. 5.9 N·m **[to confirm]** | 5.89 N·m | Handwriting partly unclear |
| 2.0 kg | 19.62 N | 0.360 m | 7.0 N·m | 7.06 N·m | Readable |
| 2.0 kg | 19.62 N | 0.160 m **[to confirm]** | approx. 3.2 N·m **[to confirm]** | 3.14 N·m | Handwriting difficult to read |
| 4.2 kg | approx. 41.2 N | 0.305 m | 12.2 N·m | 12.57 N·m | Readable |
| 4.2 kg | approx. 41.2 N | 0.360 m **[to confirm]** | **14.9 N·m** | **14.83 N·m** | Instrument reading is legible; lever arm should still be confirmed |

The reference torques in the fifth column were recalculated independently from the stated masses and lever-arm values. They are included to help identify transcription errors while the handwritten values are being clarified.

## Initial observations

The readable test points indicate that the wrench response was of the correct order of magnitude across the tested range. For the 4.2 kg mass, the clearly legible point at 0.305 m records 12.2 N·m versus a calculated 12.57 N·m, while the second legible instrument reading is 14.9 N·m versus approximately 14.83 N·m if the lever arm is confirmed as 0.360 m.

No conclusion about compliance with the seller-stated ±1 % accuracy specification should be drawn from these preliminary values because:

1. some handwritten readings still require confirmation;
2. the reference masses were weighed to ±1 g, but the lever-arm measurement uncertainty has not yet been quantified;
3. the exact force application geometry and alignment have not yet been documented;
4. the procedure was an internal functional verification and not a traceable calibration.

A final error table and percentage deviation should be calculated only after all handwritten values and setup dimensions have been confirmed.

## Records

- Original handwritten test notes: `handwritten-notes.jpg`
- Instrument used: SOARFLY YX01-24
- Display resolution: 0.1 N·m
- Minimum torque application duration per test point: 4 s

## Items to confirm

- [ ] Confirm the first reading with the 2.0 kg mass at approximately 0.300 m.
- [ ] Confirm the third 2.0 kg test lever arm and instrument reading.
- [ ] Confirm that the second lever arm used with the 4.2 kg mass was 0.360 m. The instrument reading itself is legible as 14.9 N·m.
- [ ] Record the method used to measure the lever arm and its measurement resolution.
- [x] Reference masses were weighed to ±1 g.
- [ ] Record whether torque was applied in the clockwise or counterclockwise direction.
- [ ] Add the test date if it can be reconstructed.
