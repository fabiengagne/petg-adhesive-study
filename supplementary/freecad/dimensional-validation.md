# Validation dimensionnelle du modèle 2D et 3D reconstruit sur FreeCAD

Le fichier `specimen-reconstruction.FCStd` reconstruit un solide sur FreeCAD (The FreeCAD Project Association (FPA), Anderlecht Belgium) version 1.1.3 pour Linux (version AppImage) à partir de `../stl/adhesive-test-specimen.stl` qui avait été produit à l'origine sur Fusion 360 (Autodesk inc., San Francisco CA États-Unis). Le fichier `specimen-reconstruction.stl` est exporté depuis ce solide FreeCAD. Le repère a été recentré : le STL source est centré vers X = 100 mm, le modèle FreeCAD vers X = 0 mm. Cette translation ne change aucune dimension.

| Grandeur | STL du dépôt | STL exporté de FreeCAD |
|---|---:|---:|
| Hauteur totale | 13,000 mm | 13,000 mm |
| Diamètre nominal de la base | 25,000 mm | 25,000 mm |
| Hauteur de la base circulaire | 3,000 mm | 3,000 mm |
| Hauteur du raccord vers l'hexagone | 1,500 mm | 1,500 mm |
| Prise hexagonale entre plats | 21,000 mm | 21,000 mm |
| Volume fermé calculé depuis les triangles | 5 324,3 mm³ | 5 326,0 mm³ |

Les dimensions extérieures et les plans de transition coïncident aux arrondis indiqués. Les sections intermédiaires du STL source correspondent à un raccord en quart de cercle de rayon **1,5 mm** sur chacun des six plats de l'hexagone. Le modèle FreeCAD reproduit ce raccord par six coupes à profil circulaire. L'écart entre les volumes calculés depuis les triangles des deux STL est de **1,66 mm³ (0,031 %)**. Le solide analytique FreeCAD a un volume de 5 326,34 mm³; la faible différence résiduelle avec les STL provient notamment de leur discrétisation des surfaces courbes. Le STL du dépôt demeure la référence de fabrication.

La vue des deux éprouvettes utilise deux liens FreeCAD dont les faces à coller sont opposées et distantes de **6,0 mm** dans cette proposition. Cet écart est une séparation visuelle avant assemblage, augmentée à 6 mm pour que les deux faces soient lisibles sur la projection; ce n'est pas une épaisseur de colle prescrite.

Le script `build_specimen.py` régénère le fichier FreeCAD, son STL exporté et la planche SVG avec l'interpréteur Python livré avec FreeCAD. La planche actuelle est une proposition de revue et ne remplace pas les figures de publication existantes.
