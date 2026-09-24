# Preliminary Torsional Screening of Commercial Adhesives for 3D-Printed Glycol-Modified Polyethylene Terephthalate (PETG) Assemblies

**Fabien Gagné¹, Jacques Girard¹**  
¹ Mostly Intentional Design Labs, Montréal, QC, Canada

**Proposed article type:** Technical Note  
**Running title:** TORSIONAL SCREENING OF PETG ADHESIVES

## Abstract

This technical note presents a preliminary application-specific screening of six commercial adhesives for joining parts made from fused deposition modeling (FDM) printed glycol-modified polyethylene terephthalate (PETG). The intended application is a threaded battery-compartment collar for the Amavia autonomous buoy project, where the bonded joint is subjected primarily to repeated torsional loading and must ultimately provide a watertight assembly. Two specimens per adhesive were loaded in torsion using a digital torque wrench, and both peak applied torque and observed failure mode were recorded. A polyurethane adhesive and Titebond III exhibited the lowest torque capacity and failed primarily within the adhesive. Two epoxy systems produced higher values but showed substantial specimen-to-specimen variation. Neither the regular-viscosity nor thick cyanoacrylate (CA) joints failed during testing. The four CA specimens sustained more than 20.4, 20.5, 20.9, and 20.8 N·m, respectively, before deformation, delamination, fracture, or slippage of the printed PETG specimen or fixture limited the test. These values are therefore lower bounds rather than joint failure torques. The results are not intended as a statistical characterization of adhesive strength. They demonstrate that an application-specific torsional screening procedure can distinguish markedly different failure behaviors and identify adhesive systems for further validation. Thick CA was selected for subsequent watertight assembly trials because its measured lower-bound strength was comparable to the regular CA while its longer working time and higher viscosity improved assembly control.

**Keywords:** additive manufacturing, adhesive bonding, cyanoacrylate, PETG, polymer joining, torsion, 3D printing, failure mode

## Plain Language Summary

Six readily available adhesives were compared for joining 3D-printed PETG parts used in a marine buoy project. The specimens were twisted in a fixture because the real part is repeatedly loaded in torsion when a threaded battery-compartment cover is opened and closed. The polyurethane and wood adhesives failed at relatively low torque. The epoxy adhesives performed better. All four cyanoacrylate specimens remained bonded beyond 20 N·m, at which point the printed plastic or the fixture became the limiting element. The study is a preliminary engineering screening rather than a statistical strength characterization. It identifies promising adhesive systems and the additional measurements needed for a more complete validation.

## 1. Introduction

Adhesive bonding of additively manufactured thermoplastics differs from bonding conventionally molded polymers because layer-by-layer fabrication introduces anisotropy, meaning that a mechanical property can depend on the direction in which it is measured, as well as internal voids and interlayer interfaces that may become limiting features of the assembly. Published studies on printed glycol-modified polyethylene terephthalate (PETG) have shown that raster orientation, extrusion conditions, layer height, and interlayer bonding can substantially influence stiffness, strength, and failure behavior [[1](#ref-1), [2](#ref-2), [3](#ref-3)].

The strength of an adhesively bonded assembly also depends on more than the nominal strength of the adhesive. Adhesive chemistry, adherend compliance, bond-line thickness, joint geometry, loading mode, and surface preparation can all affect the apparent capacity and the observed failure mode. Öz and Öztürk reported that adhesive type was the dominant factor among the variables investigated in a comparative study of several adhesives and 3D-printed thermoplastics [[4](#ref-4)]. Vamshinath et al. and Khosravani et al. further showed that printing and joint parameters influence the behavior of bonded PETG assemblies [[1](#ref-1), [2](#ref-2)].

Published comparisons between cyanoacrylate (CA) and epoxy systems specifically on printed PETG remain limited. On other fused deposition modeling (FDM) printed polymers, Yap et al. measured stronger joints with a cyanoacrylate than with an epoxy for the materials evaluated in their study [[5](#ref-5)]. Their results cannot be transferred quantitatively to PETG, but they illustrate that epoxy cannot be assumed to outperform CA for all printed thermoplastic joints.

ASTM D3163-01(2023) provides a standardized lap-shear procedure for comparing adhesive joints made from rigid plastic adherends [[6](#ref-6)]. The present work does not attempt to reproduce or replace that method. Instead, it addresses an application-specific loading condition in which a bonded, threaded collar is repeatedly twisted during use. The objective was therefore to perform a preliminary torsional screening of readily available adhesives using printed PETG specimens whose loading is representative of the intended assembly.

The work is presented as a **Technical Note** because it reports limited preliminary results from an application-specific evaluation method. It does not establish allowable design stresses, statistically characterize adhesive strength, or propose a standardized test procedure.

## 2. Materials and Methods

### 2.1 Application Context

The test was developed in support of the [Amavia](https://github.com/fabiengagne/Amavia) open-source self-positioning buoy project. The specific assembly of interest is a bonded threaded collar used on a battery compartment. The compartment must be opened repeatedly for battery removal and charging, which subjects the bonded interface to torsional loading. The final assembly must also resist water ingress.

The present study addresses only the mechanical screening stage. Long-term immersion, environmental aging, and repeated opening and closing cycles remain outside the scope of the current test series.

### 2.2 Printed Material

All test specimens and application parts were printed from **OVERTURE PETG Rock White, 1.75 mm filament**, marketed by **Overture 3D Technologies, LLC**, 10777 Westheimer Rd, Suite 159, Houston, TX 77042, USA.

### 2.3 Additive Manufacturing Parameters

Specimens were produced on an **Original Prusa i3 MK3** using the default Prusa PETG profile with the following recorded settings:

| Parameter | Value |
|---|---:|
| Nozzle diameter | 0.4 mm |
| Nozzle temperature | 250 °C |
| Build plate temperature | 80 °C |
| Build surface | Original Prusa PEI surface |
| Build-plate adhesive | None |
| Build-plate cleaning | 99 % isopropyl alcohol before each print |
| Layer height | 0.15 mm |
| Infill | 15 % |
| Perimeters | 4 |
| Top solid layers | 6 |
| Bottom solid layers | 6 |

The specimens were printed with the **bonding interface directly on the build plate**, so the bonded face corresponds to the first-layer surface.

<!-- TODO: Document slicer software and version, exact Prusa PETG profile name/version, infill pattern, print speed if known, extrusion width if known, and cooling settings if known. -->

### 2.4 Adhesives Evaluated

Six adhesive systems were screened.

| Adhesive | Adhesive family | Manufacturer or supplier identification |
|---|---|---|
| J-B Weld | Two-part epoxy | J-B Weld Company, LLC, Marietta, GA, USA |
| Gorilla polyurethane adhesive | Polyurethane | The Gorilla Glue Company, Cincinnati, OH, USA |
| Adhaero thick CA | Thick cyanoacrylate | Exact manufacturer not confirmed; retail product obtained from Dollarama Inc., Montréal, QC, Canada |
| Adhaero regular CA | Low-viscosity cyanoacrylate | Exact manufacturer not confirmed; retail product obtained from Dollarama Inc., Montréal, QC, Canada |
| Titebond III | Water-resistant wood adhesive | Franklin International, Inc., Columbus, OH, USA |
| System Three Quick Cure 5 | Five-minute epoxy | System Three Resins, Inc., Lacey, WA, USA |

<!-- TODO: Confirm the exact J-B Weld product designation and exact Gorilla product designation from photographs or packaging. -->
<!-- TODO: If available, record lot numbers, purchase dates, and product expiration dates. -->

Titebond III was intentionally included as an exploratory control outside its principal intended use. Its low viscosity and water-resistant formulation made it useful as a practical comparison, but the product is not marketed specifically for structural PETG bonding.

### 2.5 Specimen Geometry

Two specimens were prepared for each adhesive, for a total of 12 specimens. The specimen geometry was designed to transmit torsional load through the bonded interface while permitting mechanical engagement with the test fixture.

Early specimens used a square drive feature. Later specimens used a hexagonal drive feature that could be engaged directly by a socket. This fixture change is a limitation of the present preliminary series and will be eliminated in future testing.

<!-- TODO: Insert dimensioned drawing and identify all critical dimensions. -->
<!-- TODO: Record bonded diameter, bonded area, bond-line geometry, wall thickness, drive dimensions, overall specimen dimensions, and orientation of the layer lines relative to the bonded interface. -->
<!-- TODO: Add STL files as supplementary material and cite them here once committed. -->

### 2.6 Surface Preparation and Bonding Procedure

For all adhesive systems, both mating surfaces were abraded and then cleaned with **99 % isopropyl alcohol** before bonding. The exact abrasive grit sequence is still being documented.

After adhesive application and assembly, the specimens were **lightly pressed together** during the initial bonding period. All bonded specimens were allowed to cure for **13 days before mechanical testing**.

<!-- TODO: Document exact abrasive grit sequence used on the test specimens. -->
<!-- TODO: Document adhesive quantity or application method and confirm whether adhesive was applied to one or both mating surfaces for each adhesive system. -->
<!-- TODO: Document cure temperature and storage conditions during the 13-day curing period. -->

For the subsequent full-scale application part, both mating surfaces were sanded with multiple abrasive grades, cleaned with 99 % isopropyl alcohol, coated with thick CA, and assembled while ensuring continuous adhesive coverage around the circumference. These application-part observations are not used as substitute data for the specimen preparation procedure and will be separated from the final specimen method description.

### 2.7 Torsional Screening Apparatus

Torque was applied using a **SOARFLY YX01-24 digital torque wrench**. The specimen was held in a bench vise through a dedicated drive feature or socket arrangement, depending on specimen geometry. Torque was increased manually until one of the following occurred:

1. adhesive or interfacial failure;
2. fracture or delamination of the printed PETG;
3. permanent deformation of the specimen;
4. specimen or socket slippage that prevented further valid loading.

The torque wrench retained the maximum indicated torque reached during each loading event.

Before the experiments, the instrument response was checked against known loads and was found to agree closely with the expected values.

<!-- TODO: Add manufacturer-rated torque range, resolution, stated accuracy, serial number if available, and details of the verification with known loads. -->
<!-- TODO: Describe the verification geometry, reference masses, lever arm, number of verification points, and measured errors. -->
<!-- TODO: Record approximate torque application rate or test duration. -->

The values reported in this note are applied torque values in N·m. They are not converted to adhesive shear stress because the joint geometry and stress distribution were application-specific and were not equivalent to a standardized uniform shear specimen.

### 2.8 Failure Classification and Data Interpretation

Failure behavior was classified visually after testing using the following categories:

- adhesive or bond-line failure;
- interfacial separation;
- PETG cracking;
- PETG interlayer delamination;
- PETG bulk fracture;
- permanent specimen deformation;
- fixture or socket slippage.

When the printed PETG specimen or fixture reached its practical limit before bond failure, the measured torque was treated as a **lower bound** on the joint capacity and reported using the greater-than symbol.

Only two specimens were tested for each adhesive. This sample size does not support statistical comparison of adhesive populations, estimation of variance, or determination of design allowables. The data are therefore interpreted as preliminary screening observations intended to identify distinctly different behaviors and failure modes.

## 3. Results

Table 2 summarizes the individual specimen results. Means are intentionally not used for the primary comparison because the sample size is two per adhesive and four CA results are right-censored by specimen or fixture limitations.

| Adhesive | Specimen A | Specimen B | Principal observation |
|---|---:|---:|---|
| Gorilla polyurethane | 5.4 N·m | 3.0 N·m | Adhesive failure |
| Titebond III | 9.8 N·m | 7.0 N·m | Adhesive failure |
| J-B Weld epoxy | 16.1 N·m | 11.8 N·m | PETG cracking/delamination observed; variable response |
| System Three Quick Cure 5 | 18.6 N·m | 12.8 N·m | PETG failed first at 18.6 N·m; bond failed in second specimen |
| Regular CA (CAR) | >20.4 N·m | >20.5 N·m | No bond failure; PETG or fixture limited test |
| Thick CA (CAE) | >20.9 N·m | >20.8 N·m | No bond failure; PETG or fixture limited test |

### 3.1 Polyurethane and Titebond III

The polyurethane adhesive produced the lowest observed torque values, 5.4 and 3.0 N·m. Failure occurred within or at the adhesive joint while the PETG remained largely intact.

Titebond III failed at 9.8 and 7.0 N·m. The printed PETG showed no comparable structural damage before the bond failed. In this application-specific torsional configuration, both systems were therefore limited by the bonded joint rather than the printed substrate.

### 3.2 Epoxy Systems

J-B Weld specimens sustained 16.1 and 11.8 N·m. Cracking or delamination of the PETG was observed at the higher load, indicating that the printed adherend was beginning to contribute to the limiting failure behavior.

System Three Quick Cure 5 sustained 18.6 and 12.8 N·m. At 18.6 N·m, the printed PETG fractured while the adhesive remained bonded. The second specimen experienced bond failure at 12.8 N·m with concurrent signs of cracking in the printed material.

The spread between the two observations for each epoxy system is too large, relative to the small sample size, to support a quantitative ranking between the two epoxies.

### 3.3 Cyanoacrylate Systems

Neither regular CA specimen experienced bond failure. CAR-A reached more than 20.4 N·m and CAR-B more than 20.5 N·m before deformation, delamination, or socket interaction prevented a valid continuation of loading.

Neither thick CA specimen experienced bond failure. CAE-A reached more than 20.9 N·m and CAE-B more than 20.8 N·m before the printed PETG or fixture became limiting.

Accordingly, the four CA values are **not failure torques**. They are lower bounds demonstrating that, for the tested geometry and preparation, each CA joint sustained more than approximately 20 N·m.

## 4. Discussion

### 4.1 Screening Outcome

The observed behavior can be summarized qualitatively as follows:

**CA systems > epoxy systems > Titebond III > polyurethane adhesive**

This ordering is a screening observation, not a statistically validated ranking. The distinction is particularly important for the CA systems because their actual bond-failure torques were not measured.

The most significant experimental transition was not simply an increase in indicated torque. It was the change in the limiting failure mode. The weaker adhesive systems failed at the bonded interface or within the adhesive. At higher torque, the printed PETG, its interlayer structure, or the fixture became limiting before the CA bond failed.

### 4.2 Role of the Printed Adherend

The observed PETG cracking and delamination are consistent with the anisotropic nature of FDM parts and with prior studies showing that process parameters and interlayer bonding influence the mechanical response of printed PETG [[1](#ref-1), [2](#ref-2), [3](#ref-3)]. Öz and Öztürk similarly noted that failure of printed adherends can occur when the bond becomes stronger than the local capacity of the printed material [[4](#ref-4)].

This failure transition is important for application-specific selection. Once the adherend fails before the bond, further increases in nominal adhesive strength may provide little benefit unless the printed geometry, print orientation, or local wall structure is also modified.

### 4.3 Relation to Published Adhesive Studies

The present torsional geometry cannot be compared directly with published single-lap shear strength values. ASTM D3163 itself cautions that apparent strength measured using one joint geometry should not be treated as an allowable stress for another joint geometry or bonding process [[6](#ref-6)]. The current data should therefore remain tied to the tested PETG, specimen configuration, preparation method, and torsional loading condition.

Within that limitation, the general trends are compatible with published work showing a strong dependence on adhesive family and adherend behavior [[1](#ref-1), [2](#ref-2), [4](#ref-4)]. Yap et al. also reported cases in which cyanoacrylate joints outperformed epoxy joints on other FDM-printed polymers [[5](#ref-5)]. That result does not establish the same relation for PETG, but it provides precedent for the behavior observed here.

### 4.4 Selection of Thick Cyanoacrylate for the Application

The current test cannot establish a mechanical difference between the regular and thick CA formulations because none of the four CA joints failed.

Thick CA was selected for the next application stage for practical assembly reasons. The regular CA had a working time of only a few seconds and flowed readily beyond the intended bond region. The thick formulation provided approximately 1 to 2 min of working time in the observed assembly process, allowing the circular collar to be positioned and adjusted while making it easier to verify continuous adhesive coverage.

This selection is therefore based on **processability combined with a demonstrated lower-bound torsional capacity**, not on evidence that thick CA is mechanically stronger than regular CA.

### 4.5 Limitations

The following limitations define the scope of the current Technical Note:

1. only two specimens were tested per adhesive;
2. no statistical inference, repeatability estimate, or population-level strength ranking is possible;
3. two fixture geometries were used during the preliminary series;
4. the CA tests were limited by the PETG specimen or fixture rather than bond failure;
5. the exact abrasive grit sequence, adhesive application details, and curing environment still require formal documentation before submission;
6. instrument uncertainty has not yet been formally propagated;
7. immersion, environmental aging, thermal cycling, and repeated torsional cycling have not yet been evaluated;
8. the exact manufacturer formulation of the Adhaero CA products is not publicly documented and may vary with supply.

A future test series should use a single specimen and fixture geometry, additional replicates, a fixture capable of loading the CA joints to actual failure, and controlled environmental conditioning.

## 5. Conclusions

A preliminary torsional screening procedure was used to compare six readily available adhesive systems on FDM-printed PETG specimens for an application involving a bonded threaded collar.

The polyurethane adhesive and Titebond III failed at relatively low applied torque and were limited by the bonded joint. The two epoxy systems sustained higher torque, with some tests showing a transition toward cracking or failure of the printed PETG.

The regular and thick CA systems produced the principal result of the study. None of the four CA joints failed. Their observed capacities were CAR-A >20.4 N·m, CAR-B >20.5 N·m, CAE-A >20.9 N·m, and CAE-B >20.8 N·m. These are lower bounds because the PETG specimen or fixture became limiting before bond failure.

The data do not establish statistically significant differences between adhesive populations and do not provide design allowables. They do demonstrate distinct application-specific failure behaviors that are useful for screening candidate adhesives.

Thick CA was selected for subsequent full-scale watertight assembly trials because it combined a lower-bound torsional capacity above 20 N·m with better handling and positioning characteristics than the low-viscosity CA.

Further work will complete documentation of the abrasive preparation and adhesive application procedure, incorporate the specimen STL geometry as supplementary material, increase replication, improve the fixture, and evaluate immersion and repeated torsional cycling.

## Data and Supplementary Materials

The working manuscript and project files are maintained in the public repository:

https://github.com/fabiengagne/petg-adhesive-study

Planned supplementary material includes the specimen STL files, dimensioned drawings, test photographs, adhesive packaging photographs, and additional experimental data.

## Author Contributions

**Fabien Gagné:** Conceptualization, methodology, investigation, data curation, formal analysis, visualization, writing (original draft), project administration.  
**Jacques Girard:** Methodology, investigation, validation, resources, review and editing.

<!-- TODO: Confirm CRediT roles with both authors before submission. ASTM ScholarOne requires contributor-role selection. -->

## Acknowledgments

The authors acknowledge the open-source Amavia project context in which the application-specific bonding problem was identified.

<!-- TODO: Add any additional acknowledgments or state "None" if not applicable. -->

## References

<a id="ref-1"></a>**[1]** Vamshinath, K., Niteesh Kumar, N., Tarun Kumar, R., Nagaraju, D. S., Sateesh, N., and Subbaiah, R., “Analysis of the Effect of the Process Parameters on the Mechanical Strength of 3D Printed and Adhesively Bonded PETG Single Lap Joint,” *Materials Today: Proceedings*, Vol. 62, 2022, pp. 4509–4514. https://doi.org/10.1016/j.matpr.2022.04.950

<a id="ref-2"></a>**[2]** Khosravani, M. R., Soltani, P., and Reinicke, T., “Fracture and Structural Performance of Adhesively Bonded 3D-Printed PETG Single Lap Joints under Different Printing Parameters,” *Theoretical and Applied Fracture Mechanics*, Vol. 116, 2021, Article 103087. https://doi.org/10.1016/j.tafmec.2021.103087

<a id="ref-3"></a>**[3]** “Exploring the Role of Manufacturing Parameters on Microstructure and Mechanical Properties in Fused Deposition Modeling (FDM) Using PETG,” *Applied Composite Materials*, Vol. 28, 2021, pp. 1799–1828. https://doi.org/10.1007/s10443-021-09940-9

<a id="ref-4"></a>**[4]** Öz, Ö., and Öztürk, F. H., “The Effect of Adhesive and Adherend Compliance on the Failure of 3D-Printed Parts,” *Welding in the World*, Vol. 69, 2025, pp. 2869–2883. https://doi.org/10.1007/s40194-025-02048-9

<a id="ref-5"></a>**[5]** Yap, Y. L., Toh, W., Koneru, R., Lin, R., Chan, K. I., Guang, H., Chan, W. Y. B., Teong, S. S., Zheng, G., and Ng, T. Y., “Evaluation of Structural Epoxy and Cyanoacrylate Adhesives on Jointed 3D Printed Polymeric Materials,” *International Journal of Adhesion and Adhesives*, Vol. 100, 2020, Article 102602. https://doi.org/10.1016/j.ijadhadh.2020.102602

<a id="ref-6"></a>**[6]** ASTM International, ASTM D3163-01(2023), *Standard Test Method for Determining Strength of Adhesively Bonded Rigid Plastic Lap-Shear Joints in Shear by Tension Loading*, ASTM International, West Conshohocken, PA, 2023. https://doi.org/10.1520/D3163-01R23
