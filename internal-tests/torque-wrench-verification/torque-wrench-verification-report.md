# Internal Verification Report: SOARFLY YX01-24 Digital Torque Wrench

## Purpose

This internal test was performed on 2026-09-22 to check the indication of the digital torque wrench used for the PETG adhesive torsion tests against torques generated from known masses applied at measured lever-arm distances. The verification was intended as an in-house functional check only. It was not a traceable calibration. The reference masses used for the verification were weighed to **±1 g** before use.

## Instrument

- **Instrument:** Digital torque wrench
- **Brand:** SOARFLY
- **Model:** YX01-24
- **Serial number shown on the instrument:** SN:20260702093 ([photograph](../../media/photos/torque-wrench-serial.jpeg))
- **Display resolution:** **0.1 N·m**
- **Commercially stated accuracy:** ±1 % (no traceable calibration certificate available)
- **Commercially stated maximum capacity:** 220 N·m

## Test principle

A known mass, measured to **±1 g**, was used to generate a force under gravity. The force was applied at a measured perpendicular distance from the torque axis. The reference torque was calculated as (T = F r = m g r), using (g = 9.81 mathrm{m/s^2}).

For each test point, the load was applied continuously for **at least 4 s** before the instrument reading was recorded.

Two masses appear in the handwritten notes:

- **2.0 kg**, corresponding to **19.62 N** using (g = 9.81 mathrm{m/s^2}), used for the first test series;
- **4.2 kg**, corresponding to approximately **41.2 N**.

## ASTM method context

The verification method used here, in which known masses generate a static torque through a measured lever arm, is consistent in principle with ASTM torque-verification practice. ASTM E2624-17(2025), *Standard Practice for Torque Calibration of Testing Machines*, explicitly recognizes the use of standard weights and lever arms as one of the permitted methods for calibrating static or quasi-static torque-capable testing machines and devices. ASTM E2428-22, *Standard Practice for Calibration and Verification of Elastic Torque Measurement Standards*, provides the related framework for calibration and verification of elastic torque measurement standards used in torque metrology.

This internal check was **not performed as a formal ASTM E2624 or ASTM E2428 calibration**. In particular, the procedure did not establish full metrological traceability or a complete uncertainty budget for lever-arm length, alignment, force application geometry, and all other contributors required for a formal calibration. The ASTM references are therefore used to document that the dead-weight and lever-arm principle is an established torque-verification approach, not to claim conformance with either standard.

References:
1. ASTM International, ASTM E2428-22, *Standard Practice for Calibration and Verification of Elastic Torque Measurement Standards*, ASTM International, West Conshohocken, PA, 2022. https://doi.org/10.1520/E2428-22
2. ASTM International, ASTM E2624-17(2025), *Standard Practice for Torque Calibration of Testing Machines*, ASTM International, West Conshohocken, PA, 2025. https://doi.org/10.1520/E2624-17R25

## Description of the test

The torque wrench was arranged so that a known gravitational load produced a moment about the wrench axis at a measured lever arm in the clockwise direction. A reference mass was applied at the selected distance from the axis. The load was brought onto the wrench and maintained for a minimum of 4 s so that a stable indication could be observed and recorded. The indicated torque was then compared with the torque calculated from the applied force and the measured lever arm.

Several lever-arm distances were used in order to check the instrument response at multiple torque levels. The original handwritten notes are preserved with this report.

## Final transcription and comparison

Reference torque was recalculated from the recorded mass and lever arm using \(T = m g r\), with \(g = 9.81\ \mathrm{m/s^2}\).

| Mass | Force | Lever arm | Instrument indication | Calculated reference torque | Mean of indication and reference | Error | Relative error |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2.0 kg | 19.62 N | 0.300 m | 5.9 N·m | 5.89 N·m | 5.90 N·m | +0.01 N·m | +0.24 % |
| 2.0 kg | 19.62 N | 0.360 m | 7.0 N·m | 7.06 N·m | 7.03 N·m | -0.06 N·m | -0.89 % |
| 2.0 kg | 19.62 N | 0.160 m | 3.2 N·m | 3.14 N·m | 3.17 N·m | +0.06 N·m | +1.94 % |
| 4.2 kg | 41.20 N | 0.305 m | 12.2 N·m | 12.57 N·m | 12.38 N·m | -0.37 N·m | -2.92 % |
| 4.2 kg | 41.20 N | 0.360 m | 14.9 N·m | 14.83 N·m | 14.87 N·m | +0.07 N·m | +0.45 % |

The mean column is the arithmetic mean of the instrument indication and the calculated reference value for each test point. It is included only as a descriptive comparison and is not used as an accuracy metric.

Across the five test points, the mean signed relative error is approximately **-0.24 %**, the mean absolute relative error is approximately **1.29 %**, and the root-mean-square relative error is approximately **1.63 %**.

## Initial observations and assessment

The instrument follows the expected torque closely over the approximately 3 to 15 N·m range tested. Three of the five points fall within ±1 % of the calculated reference torque. The largest observed deviation is approximately **-2.92 %** at the 12.57 N·m reference point.

The seller-stated ±1 % accuracy claim is therefore **not demonstrated by this internal check over the full tested range**. At the same time, this result should not be interpreted as a formal calibration failure. The wrench display resolution is 0.1 N·m, corresponding to a quantization contribution of up to about ±0.05 N·m, which alone represents about ±1.6 % at the lowest 3.14 N·m reference point. The reference masses were measured to ±1 g, making their contribution comparatively small, but the uncertainty in lever-arm length, load alignment, and exact force application geometry was not characterized.

For the purpose for which the wrench was used in the PETG adhesive screening, the internal verification supports treating the instrument as **reasonably accurate for comparative testing**, with observed agreement generally on the order of a few percent. The present data do not justify claiming a verified ±1 % measurement accuracy. Because only one indication was recorded at each torque point, this test does **not** establish measurement precision or repeatability in the strict metrological sense. For publication purposes, the most defensible characterization remains that the SOARFLY YX01-24 was functionally checked against known gravitational loads and showed agreement within approximately **3 %** over the tested range, without traceable calibration.

## Records

- Original handwritten test notes: `handwritten-notes.jpg`
- Instrument used: SOARFLY YX01-24
- Instrument serial number: SN:20260702093
- Display resolution: 0.1 N·m
- Minimum torque application duration per test point: 4 s
