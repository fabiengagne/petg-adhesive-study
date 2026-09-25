# Torsional screening data

`torsional-screening-results.csv` contains one row per bonded test assembly, in the order shown by the chapters of the [experiment video](https://youtu.be/kQGwA80CW48). Each assembly consists of two printed PETG halves joined at their circular faces. Thus the 12 tested assemblies use 24 printed halves. The `A` and `B` suffixes distinguish the two assemblies for each adhesive.

The video description labels both the 03:14 and 07:42 chapters as “Polyuréthane Gorilla - A”. At 03:14 the spoken identification is “PUG B” and the recorded peak is 3.0 N·m; at 07:42 the spoken identification is “échantillon numéro A” and the peak is 5.4 N·m. The CSV follows the spoken identification and the manuscript's specimen labels.

Torque values and broad failure observations are transcribed from Table 2 and the corresponding result paragraphs of the English manuscript. `lower_bound` means that the bond did not fail at the displayed peak torque; the value is not a measured bond-failure torque. For all four CA assemblies, the printed PETG reached its practical limit before bond failure; the fixture did not limit these tests. `observed_peak` means that the manuscript does not establish a single per-assembly joint failure classification. `not specified` and `not documented per assembly` mark missing information rather than inferred results. The manuscript reports that both square and hexagonal drive features were used, but does not map those features to individual assemblies.

The video chapter times identify the start of each test segment, not the exact instant of peak-torque measurement. Video: https://youtu.be/kQGwA80CW48

The recorded specimen-printing settings are preserved in `additive-manufacturing-parameters.md`; unverified slicer and profile details are explicitly identified there.
