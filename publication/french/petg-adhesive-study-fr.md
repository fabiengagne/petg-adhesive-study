# Essai comparatif d’adhésifs pour PETG

**Jacques Girard¹, Fabien Gagné¹**  
¹ Mostly Intentional Design Labs, Montréal, QC, Canada

## Résumé

Cette étude comparative évalue la performance de six adhésifs pour l’assemblage de pièces imprimées en PETG destinées à une application marine, soit les boîtiers des bouées autonomes du projet Amavia. Les adhésifs examinés sont un époxy JB Weld, un époxy à prise rapide de 5 minutes, un adhésif polyuréthane Gorilla, un adhésif à bois Titebond III, ainsi que deux cyanoacrylates de viscosités différente, régulier et épais. Deux éprouvettes par adhésif ont été soumises à un chargement en torsion reproduisant le type de sollicitation attendu sur le col fileté du compartiment batterie. Le couple maximal ainsi que le mode de rupture ont été consignés. Les adhésifs polyuréthane et Titebond III ont présenté les résistances les plus faibles, avec rupture principalement dans l’adhésif. Les époxys ont offert de meilleures performances, mais avec une variabilité notable entre les éprouvettes. Les cyanoacrylates ont fourni les meilleurs résultats : aucun des quatre essais n’a entraîné de rupture du joint. Les résistances observées sont donc rapportées comme des bornes inférieures (> 20,4 N·m), la déformation ou la rupture du PETG et du montage d’essai devenant alors le facteur limitant. Le cyanoacrylate épais a été retenu pour l’application finale en raison de sa résistance mécanique, de son temps de travail supérieur à celui du CA liquide et de sa viscosité mieux adaptée à l’obtention d’un joint continu. Un essai d’étanchéité en immersion est prévu afin de compléter la validation pour l’usage réel.

**Mots-clés :** PETG, adhésif, collage, cyanoacrylate, époxy, torsion, impression 3D, étanchéité, Amavia.

---

## Introduction

L’assemblage par adhésif de pièces issues de fabrication additive constitue un problème distinct de celui des polymères moulés, car la structure couche par couche introduit une anisotropie (propriété qui dépend de la direction dans laquelle on la mesure), une porosité interne et des interfaces inter-couches susceptibles de devenir les éléments limitants du joint. Des travaux consacrés au PETG imprimé par extrusion montrent notamment que les paramètres de fabrication — orientation du raster, largeur d’extrusion, hauteur de couche et qualité des liaisons inter-couches — influencent fortement la rigidité, la résistance et les modes de rupture des pièces [[[1]](#ref-1)(#ref-1)–[[3]](#ref-3)(#ref-3)].

Le comportement d’un joint ne dépend par ailleurs pas uniquement de la résistance nominale de l’adhésif. La compatibilité adhésif–substrat, la rigidité relative des deux matériaux, l’épaisseur de la ligne de collage, la géométrie du joint et la préparation de surface peuvent modifier à la fois la charge ultime et le mode de rupture. Une étude récente comparant plusieurs familles d’adhésifs sur des thermoplastiques imprimés, dont le PETG, conclut que le **type d’adhésif** est le facteur dominant de la résistance du joint parmi les variables étudiées [[4]](#ref-4). D’autres travaux spécifiques aux assemblages PETG imprimés confirment que les paramètres d’impression et l’épaisseur de l’adhésif influencent significativement la résistance et le comportement de rupture des joints [[[1]](#ref-1)(#ref-1), [[2]](#ref-2)(#ref-2)].

Les données publiées comparant directement cyanoacrylates et époxys sur **PETG imprimé** demeurent limitées. Sur d’autres polymères imprimés, Yap *et al.* ont toutefois mesuré des résistances de joint plus élevées avec un cyanoacrylate qu’avec un époxy pour les matériaux ASA et Nylon 12 chargé de fibres de carbone [[5]](#ref-5). Cette observation ne peut pas être transposée quantitativement au PETG, mais elle montre que la supériorité d’un époxy ne peut pas être présumée pour une pièce imprimée.

Les retours de la communauté d’impression 3D sont eux-mêmes contradictoires : certains utilisateurs rapportent des assemblages PETG au cyanoacrylate assez résistants pour entraîner la rupture de la pièce, tandis que d’autres préfèrent l’époxy et signalent une faible tenue de certains cyanoacrylates [[[6]](#ref-6)(#ref-6), [[7]](#ref-7)(#ref-7)]. Ces divergences renforcent l’intérêt d’un essai comparatif réalisé avec les **adhésifs réellement disponibles**, le PETG réellement utilisé et un chargement représentatif de l’application Amavia.

Le présent travail constitue donc un essai comparatif d’ingénierie appliquée, et non une caractérisation normalisée de propriétés adhésives. Son objectif est d’identifier un système de collage approprié au col fileté du compartiment batterie d’une bouée Amavia, soumis à des sollicitations répétées en torsion et devant ultérieurement assurer une fonction d’étanchéité.

---

## Objectif

L'objectif de cet essai est de déterminer **quel adhésif convient le mieux pour assembler durablement des pièces imprimées en PETG destinées aux bouées Amavia**, en particulier le col fileté/couvercle du compartiment batterie.

Ce joint doit :

- supporter des efforts de torsion répétés lors de l'ouverture et de la fermeture du couvercle ;
- conserver une bonne résistance mécanique ;
- rester étanche dans un environnement aquatique.

L'essai vise avant tout une **comparaison pratique entre plusieurs adhésifs facilement disponibles**, plutôt qu'une mesure normalisée de résistance absolue.

Deux éprouvettes sont utilisées par adhésif. Cet échantillonnage est faible, mais suffisant pour obtenir une première comparaison entre les produits.

---

## Adhésifs testés

Six produits ou familles d’adhésifs ont été comparés :

| Adhésif | Type | Manufacturier / siège social |
|---|---|---|
| **JB Weld** | Époxy bicomposant | **J-B Weld Company, LLC** (Marietta, Georgia, États-Unis) |
| **Gorilla Polyurethane** | Adhésif polyuréthane | **The Gorilla Glue Company** (Cincinnati, Ohio, États-Unis) |
| **Cyanoacrylate épais** | CA visqueux, produit bon marché provenant de Dollarama | **Adhaero** — manufacturier réel non identifié avec certitude ; produit commercialisé chez Dollarama. **Dollarama Inc.** (Montréal, Québec, Canada) est indiqué ici comme détaillant/distributeur, et non comme manufacturier confirmé. |
| **Cyanoacrylate régulier** | CA liquide, même marque que le CA épais | **Adhaero** — manufacturier réel non identifié avec certitude ; produit commercialisé chez Dollarama. **Dollarama Inc.** (Montréal, Québec, Canada) est indiqué ici comme détaillant/distributeur, et non comme manufacturier confirmé. |
| **Titebond III** | Adhésif à bois résistant à l'eau | **Franklin International, Inc.** (Columbus, Ohio, États-Unis) |
| **System Three Quick Cure 5** | Époxy à prise rapide, 5 minutes | **System Three Resins, Inc.** (Lacey, Washington, États-Unis) |

La Titebond III est incluse comme essai exploratoire. Elle n'est pas destinée au PETG, mais sa fluidité et sa résistance à l'eau rendaient intéressant de vérifier si elle pouvait pénétrer dans la texture de l'impression et fournir un collage acceptable.


### Identification des manufacturiers

Les sièges sociaux des fabricants identifiés ont été vérifiés à partir de sources publiques des entreprises. Pour les cyanoacrylates **Adhaero**, les sources commerciales permettent de confirmer la marque et sa vente chez Dollarama, mais pas d'identifier de manière fiable l'entité manufacturière derrière le produit. Pour cette raison, **Dollarama Inc. (Montréal, Québec, Canada)** est mentionnée uniquement comme détaillant/distributeur. L'époxy à prise rapide a pu être identifié visuellement comme **System Three Quick Cure 5**, fabriqué par **System Three Resins, Inc.**

---

# Protocole d'essai

## Éprouvettes

Deux éprouvettes PETG sont préparées pour chaque adhésif.

La géométrie permet d'appliquer un **couple de torsion**, afin de reproduire le plus fidèlement possible le chargement réel attendu sur le col fileté du compartiment batterie.

Les premières éprouvettes possèdent une prise carrée. Les suivantes utilisent une prise hexagonale, ce qui entraîne une légère modification du montage en cours d'essai.

## Instrumentation

Le couple est mesuré à l'aide d'une **clé dynamométrique numérique SOARFLY, modèle YX01-24** (*Digital Torque Wrench*).

Le montage est maintenu dans un étau et l'instrument conserve la valeur maximale atteinte pendant l'essai.

La clé dynamométrique a été vérifiée au préalable avec des charges de valeur connue et donnait des lectures jugées très précises.

Les résultats sont exprimés sous forme de **couple en N·m**.

## Critères observés

Le couple maximal n'est pas le seul critère utilisé.

Le **mode de rupture** est également observé :

- rupture de l’adhésif ;
- décollement de l’interface ;
- fissuration ou délamination du PETG ;
- rupture du PETG ;
- déformation ou glissement de l'éprouvette dans la douille avant rupture du joint.

Lorsque le PETG ou le montage d'essai devient le maillon faible, la valeur obtenue devient une **borne inférieure de la résistance réelle du joint**, plutôt qu'une mesure de sa rupture.

---

# Résultats

| Adhésif | Échantillon A | Échantillon B | Observation principale |
|---|---:|---:|---|
| **Gorilla polyuréthane** | **5,4 N·m** | **3,0 N·m** | Rupture de l’adhésif |
| **Titebond III** | **9,8 N·m** | **7,0 N·m** | Rupture nette de l’adhésif |
| **JB Weld** | **16,1 N·m** | **11,8 N·m** | Début de rupture/délamination du PETG ; variabilité |
| **System Three Quick Cure 5** | **18,6 N·m** | **12,8 N·m** | À 18,6 N·m, le PETG casse avant la adhésif ; l'autre joint cède |
| **CA régulier (CAR)** | **> 20,4 N·m** | **> 20,5 N·m** | Aucune rupture du joint ; limite imposée par le PETG ou le montage |
| **CA épais (CAE)** | **> 20,9 N·m** | **> 20,8 N·m** | Aucune rupture du joint ; limite imposée par le PETG ou le montage |

## Gorilla polyuréthane

Résultats :

- **5,4 N·m**
- **3,0 N·m**

La rupture se produit dans la adhésif elle-même.

Le PETG demeure pratiquement intact, ce qui indique que l'adhésif est clairement le maillon faible.

**Moyenne approximative : 4,2 N·m.**

C'est le moins performant des produits testés.

## Titebond III

Résultats :

- **9,8 N·m**
- **7,0 N·m**

Dans les deux cas, le joint adhésif cède sans dommage notable au PETG.

**Moyenne : 8,4 N·m.**

La performance est meilleure que celle du polyuréthane, mais nettement inférieure aux époxys et aux cyanoacrylates.

## JB Weld

Résultats :

- **16,1 N·m**
- **11,8 N·m**

À forte charge, on commence à observer de la fissuration ou de la délamination du PETG.

L’adhésif présente également de bonnes propriétés pratiques d'application :

- bonne épaisseur ;
- couverture facile à contrôler ;
- application relativement simple.

Cependant, les deux éprouvettes présentent une dispersion importante.

**Moyenne : environ 14,0 N·m.**

## System Three Quick Cure 5

Résultats :

- **18,6 N·m**
- **12,8 N·m**

À **18,6 N·m**, ce n'est pas le collage qui casse : c'est le PETG lui-même.

Sur le second échantillon, le joint adhésif finit par céder à **12,8 N·m**, avec également un début de fissuration du matériau.

**Moyenne : 15,7 N·m.**

Cet adhésif offre donc une bonne résistance, mais une certaine variabilité entre les éprouvettes.

---

# Cyanoacrylate régulier

Résultats :

- **CAR-A > 20,4 N·m**
- **CAR-B > 20,5 N·m**

Aucune rupture du joint n’a été observée lors des deux essais.

Dans les deux cas, la limite de l’essai a été imposée par le PETG ou par le montage : délamination locale, déformation de l’éprouvette et/ou rotation dans la douille.

Il n’est donc pas approprié de calculer une moyenne de rupture pour le CA régulier. Les valeurs mesurées doivent être interprétées comme des **bornes inférieures** de la résistance du joint.

**Résistance du joint CA régulier : > 20,4–20,5 N·m dans les conditions de cet essai.**

---

# Cyanoacrylate épais

Résultats :

- **CAE-A > 20,9 N·m**
- **CAE-B > 20,8 N·m**

Aucune rupture du joint n’a été observée lors des deux essais.

Comme pour le CA régulier, le PETG ou le montage d’essai a atteint sa limite avant l’adhésif. Les valeurs mesurées constituent donc des **bornes inférieures** et non des couples de rupture.

**Résistance du joint CA épais : > 20,8–20,9 N·m dans les conditions de cet essai.**

Le résultat demeure particulièrement intéressant considérant qu’il s’agit d’un cyanoacrylate épais bon marché provenant de Dollarama.

Une réserve demeure toutefois quant à la répétabilité du produit : rien ne garantit qu’un tube acheté plus tard contiendra exactement la même formulation.

---

# Discussion

## Comparaison des performances

Dans les conditions de ce montage, l’ordre observé est :

**CA épais ≈ CA régulier > System Three Quick Cure 5 > JB Weld > Titebond III > Gorilla polyuréthane**

Cette relation doit être interprétée avec prudence. Les valeurs associées aux cyanoacrylates ne sont pas des couples de rupture : **aucun des quatre joints CA n’a rompu**. Les résultats sont donc des bornes inférieures :

- **CAR-A > 20,4 N·m** ;
- **CAR-B > 20,5 N·m** ;
- **CAE-A > 20,9 N·m** ;
- **CAE-B > 20,8 N·m**.

Les essais établissent ainsi que, pour la géométrie, le PETG, la préparation de surface et les produits utilisés ici, les deux formulations de cyanoacrylate supportent **plus de 20 N·m**. Le couple de rupture réel du joint n’a pas été déterminé.

## Mode de rupture et rôle du PETG imprimé

Le passage d’une rupture de l’adhésif à une déformation, une délamination ou une rupture du PETG est particulièrement significatif. Dans la littérature sur les assemblages de pièces imprimées, une rupture de l’adhérent peut survenir lorsque la résistance de l’interface de collage excède la résistance inter-couches de la pièce imprimée [[4]](#ref-4). Cette interprétation est compatible avec les observations faites ici pour les CA et, sur un des essais, pour le System Three Quick Cure 5.

Ce comportement est aussi cohérent avec la nature anisotrope des pièces FDM. Les études consacrées au PETG montrent que la microstructure produite par dépôt couche par couche, l’orientation des filaments et la qualité des interfaces inter-couches modifient la réponse mécanique et peuvent favoriser la délamination [[[1]](#ref-1)(#ref-1)–[[3]](#ref-3)(#ref-3)]. Ainsi, lorsqu’une éprouvette se déforme ou se délamine avant le joint, l’essai ne caractérise plus seulement l’adhésif : il devient aussi un essai de la pièce imprimée et de la géométrie de serrage.

## Mise en perspective avec la littérature

Les résultats obtenus ne sont pas directement comparables aux valeurs de résistance publiées dans les essais de type *single-lap joint*, puisque le présent montage applique un **couple de torsion** sur une géométrie spécifique à l’application. Ils concordent néanmoins avec plusieurs tendances publiées.

Premièrement, la littérature montre que le choix de l’adhésif peut dominer la résistance d’un joint sur thermoplastique imprimé. Dans l’étude d’Öz et Öztürk, qui compare quatre familles d’adhésifs et quatre thermoplastiques imprimés, le type d’adhésif représente la contribution statistique la plus importante à la résistance du joint ; le polyuréthane est également la famille qui présente la capacité portante la plus faible dans leur série d’essais [[4]](#ref-4). Les formulations et la géométrie étant différentes, cela ne constitue pas une validation directe de notre classement, mais fournit un contexte cohérent avec la faible performance du Gorilla polyuréthane observée ici.

Deuxièmement, les essais de Vamshinath *et al.* et de Khosravani *et al.* sur des joints PETG imprimés montrent que l’épaisseur du joint ainsi que les paramètres d’impression modifient la résistance et les modes de rupture [[[1]](#ref-1)(#ref-1), [[2]](#ref-2)(#ref-2)]. La performance mesurée dans le présent travail doit donc être considérée comme propre au procédé d’impression, à l’état de surface, à la géométrie et à l’application des adhésifs utilisés.

Troisièmement, Yap *et al.* ont observé, sur deux autres polymères imprimés, des joints cyanoacrylate plus résistants que des joints époxy [[5]](#ref-5). Bien que leurs substrats ne soient pas du PETG, ce résultat montre qu’un CA peut surpasser un époxy sur des pièces FDM et donne un précédent scientifique compatible avec notre observation expérimentale.

## Cyanoacrylate régulier et cyanoacrylate épais

Le présent protocole ne permet pas de distinguer mécaniquement les deux CA : les quatre éprouvettes ont dépassé la capacité utile du montage sans rupture du joint. Le choix du **CA épais** repose donc principalement sur des considérations de mise en œuvre plutôt que sur une différence de résistance démontrée.

Le CA régulier polymérise très rapidement et sa faible viscosité complique le contrôle d’un joint circulaire de grande dimension. Le CA épais offre, dans l’expérience réalisée, environ **1 à 2 minutes de temps de travail**, permet un repositionnement et facilite l’observation d’une couverture continue. Pour le col du compartiment batterie, ces caractéristiques réduisent le risque pratique de laisser une zone insuffisamment mouillée.

L’hypothèse formulée pendant l’essai selon laquelle le CA pourrait pénétrer davantage dans la texture superficielle du PETG reste plausible, mais **n’est pas démontrée** par les mesures présentes. La littérature consultée permet d’affirmer que la préparation de surface et la structure imprimée peuvent influencer la performance d’un joint [[[1]](#ref-1)(#ref-1), [[2]](#ref-2)(#ref-2), [[4]](#ref-4)(#ref-4)], mais elle ne permet pas d’attribuer ici la bonne performance du CA à un mécanisme microscopique particulier.

## Retours de la communauté

Les échanges de la communauté d’impression 3D ne donnent pas de consensus clair. Des utilisateurs rapportent des joints CA sur PETG qui résistent jusqu’à la rupture de la pièce, en particulier avec un CA de bonne qualité et une préparation de surface adéquate [[6]](#ref-6). D’autres signalent au contraire des résultats médiocres au CA et préfèrent des époxys bicomposants [[7]](#ref-7). Ces témoignages ne constituent pas des données scientifiques contrôlées, mais ils illustrent la sensibilité du résultat au produit exact, à la préparation de surface, au vieillissement, à la géométrie et au mode de chargement.

Cette variabilité communautaire justifie l’approche adoptée ici : tester les produits réellement accessibles dans l’environnement du projet plutôt que se fier uniquement à une recommandation générique par famille chimique.

## Limites de l’étude

Plusieurs limites doivent être conservées à l’esprit :

- seulement **deux éprouvettes par adhésif** ont été testées ;
- le protocole n’est pas un essai normalisé de type ASTM D3163 ;
- la géométrie et le mode de chargement sont volontairement spécifiques à l’application Amavia ;
- les quatre essais CA sont **censurés par la limite du PETG ou du montage**, et non par rupture du joint ;
- aucune incertitude instrumentale formelle ni dispersion statistique robuste n’a été calculée ;
- la résistance à l’eau, au vieillissement, aux cycles thermiques et aux ouvertures/fermetures répétées n’est pas encore caractérisée ;
- la formulation exacte des cyanoacrylates Adhaero n’est pas documentée et pourrait varier avec l’approvisionnement.

Un travail ultérieur pourrait utiliser davantage d’éprouvettes, un montage capable de dépasser 21 N·m sans glissement ni déformation parasite, et un protocole normalisé de cisaillement en recouvrement en complément du présent essai applicatif. Des essais après immersion et après cyclage mécanique seraient particulièrement pertinents pour l’usage marin visé.

---

# Choix retenu : cyanoacrylate épais

Même si le CA liquide donne une résistance mécanique pratiquement identique, le CA épais présente plusieurs avantages importants pour l'application Amavia.

## CA régulier

Le CA liquide :

- prend en quelques secondes ;
- laisse très peu de temps pour repositionner les pièces ;
- est très fluide ;
- peut facilement couler hors de la zone de collage ;
- est plus difficile à répartir uniformément sur un grand joint.

## CA épais

Le CA épais :

- offre environ **1 à 2 minutes de temps de travail** ;
- permet de repositionner les pièces ;
- est plus facile à appliquer uniformément ;
- permet de mieux vérifier visuellement la couverture du joint ;
- reste suffisamment fluide pour bien mouiller les surfaces.

Pour un grand joint circulaire devant également assurer l'étanchéité, ces caractéristiques sont particulièrement intéressantes.

Une hypothèse proposée pendant l'essai est que le cyanoacrylate pourrait également pénétrer légèrement dans la structure superficielle du PETG imprimé et obtenir ainsi un meilleur ancrage mécanique que des adhésifs plus visqueux.

Cette hypothèse n'est toutefois pas démontrée par l'essai.

---

# Application sur la pièce réelle

À la suite des essais mécaniques, le **cyanoacrylate épais** est choisi pour assembler le véritable col fileté au boîtier.

## Préparation des surfaces

Les deux surfaces sont :

<a id="ref-1"></a>**[1]** poncées à différents grades de papier abrasif ;
<a id="ref-2"></a>**[2]** nettoyées avec de l'**alcool isopropylique à 99 %** ;
<a id="ref-3"></a>**[3]** enduites d’adhésif ;
<a id="ref-4"></a>**[4]** assemblées en s'assurant que toute la circonférence du joint est couverte.

L’adhésif est appliqué sur les deux surfaces.

## Avantages observés pendant l'assemblage

Le temps de prise du CA épais permet :

- de positionner correctement les deux pièces ;
- de faire de petits ajustements après le premier contact ;
- de vérifier que l’adhésif forme un joint continu sur toute la circonférence.

L’adhésif étant transparent, le résultat est également relativement discret sur le plan esthétique.

---

# Étape suivante

La prochaine étape annoncée est un **essai d'étanchéité dans l'eau** du véritable boîtier assemblé avec le CA épais.

L'objectif sera de vérifier que l'excellente résistance mécanique observée lors des essais de torsion s'accompagne également d'une bonne résistance à l'eau et d'une étanchéité durable.

---

# Conclusion

Dans les conditions spécifiques de cet essai, les six adhésifs présentent des comportements nettement différents. Le **Gorilla polyuréthane** et le **Titebond III** atteignent les plus faibles couples avant rupture du joint. Les deux époxys offrent des performances sensiblement supérieures, mais avec une dispersion notable entre les deux éprouvettes.

Les deux **cyanoacrylates**, régulier et épais, constituent le résultat principal de l’étude : **aucun des quatre joints n’a rompu**. Les valeurs CAR-A > 20,4 N·m, CAR-B > 20,5 N·m, CAE-A > 20,9 N·m et CAE-B > 20,8 N·m doivent donc être considérées comme des bornes inférieures. À ces niveaux, le PETG ou le montage devient le facteur limitant.

La littérature disponible confirme que la performance des joints sur pièces imprimées dépend fortement de la famille d’adhésif, des paramètres d’impression et du mode de rupture [[[1]](#ref-1)(#ref-1)–[[5]](#ref-5)(#ref-5)]. Elle fournit également des précédents où le cyanoacrylate surpasse l’époxy sur d’autres polymères FDM [[5]](#ref-5), sans toutefois permettre de généraliser ce résultat à tous les PETG ou à tous les produits commerciaux.

Pour l’application Amavia, le **cyanoacrylate épais** est retenu non parce qu’il a démontré une résistance supérieure au CA régulier — ce que le montage actuel ne permet pas d’établir — mais parce qu’il combine une résistance supérieure à la capacité mesurable de l’essai avec une viscosité et un temps de travail plus favorables à la réalisation d’un joint circulaire continu.

La validation n’est pas complète tant que la tenue à l’immersion, au vieillissement et aux cycles répétés de torsion n’a pas été mesurée. Le prochain jalon expérimental est donc l’essai d’étanchéité et de durabilité du boîtier assemblé.

---

# Références

1. Vamshinath, K., Niteesh Kumar, N., Tarun Kumar, R., Nagaraju, D. S., Sateesh, N. & Subbaiah, R. (2022). “Analysis of the effect of the process parameters on the mechanical strength of 3D printed and adhesively bonded PETG single lap joint.” *Materials Today: Proceedings*, 62, 4509–4514. https://doi.org/10.1016/j.matpr.2022.04.950

2. Khosravani, M. R., Soltani, P. & Reinicke, T. (2021). “Fracture and structural performance of adhesively bonded 3D-printed PETG single lap joints under different printing parameters.” *Theoretical and Applied Fracture Mechanics*, 116, 103087. https://doi.org/10.1016/j.tafmec.2021.103087

3. “Exploring the Role of Manufacturing Parameters on Microstructure and Mechanical Properties in Fused Deposition Modeling (FDM) Using PETG.” (2021). *Applied Composite Materials*, 28, 1799–1828. https://doi.org/10.1007/s10443-021-09940-9

4. Öz, Ö. & Öztürk, F. H. (2025). “The effect of adhesive and adherend compliance on the failure of 3D-printed parts.” *Welding in the World*, 69, 2869–2883. https://doi.org/10.1007/s40194-025-02048-9

<a id="ref-5"></a>**[5]** Yap, Y. L., Toh, W., Koneru, R., Lin, R., Chan, K. I., Guang, H., Chan, W. Y. B., Teong, S. S., Zheng, G. & Ng, T. Y. (2020). “Evaluation of structural epoxy and cyanoacrylate adhesives on jointed 3D printed polymeric materials.” *International Journal of Adhesion and Adhesives*, 100, 102602. https://doi.org/10.1016/j.ijadhadh.2020.102602

<a id="ref-6"></a>**[6]** Reddit, r/3Dprinting (2025). “How to properly glue two PETG parts together?” Discussion communautaire ; certains participants rapportent de bons résultats avec des cyanoacrylates de qualité et différentes viscosités. https://www.reddit.com/r/3Dprinting/comments/1ngjhb9/

<a id="ref-7"></a>**[7]** Reddit, r/3Dprinting (2026). “PLA TO PETG Superglue.” Discussion communautaire illustrant des retours opposés, certains utilisateurs préférant un époxy bicomposant au cyanoacrylate pour PETG. https://www.reddit.com/r/3Dprinting/comments/1qva5qo/

> **Note sur les références communautaires :** les sources [[6]](#ref-6) et [[7]](#ref-7) sont incluses uniquement comme contexte d’usage et ne constituent pas des preuves expérimentales contrôlées.
