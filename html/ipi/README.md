# Projet IPI Développement Applicatif

Ce projet aura pour but de mettre en place un serveur apache, une plate-forme CGI et des scripts Python.

## Spécifications :

On estime que le radar se comporte comme un laser avec très eu d'atténuaton

Angle 
Rayon
Valeur à ce croisement

Cette valeur va être mappée sur une palette de couler pour la visualiser à l'écran

Un plot python est une zone dans laquelle on va dessiner une image. Subplot et trois chiffre

Subplot 111 veut dire un plot d'une dimansion sur une dimension et on prend la 1ere image (plot permet de dviser mon écran)

subplot 221 divise mon écran en 4 et on prend la première image en haut à gauche. Nous on n'a qu'une seule image donc on ne divise pas on prend 111.

Python sait gérer les coordonnées Polaires avec Polar=True  (Polaire c'est R et THETA)

On définit une palette de couleurs en listant toutes les couleurs

Le tracé de l'image se fat en une seule instruction l'instruction scatter :

    dessin = scatter(theta, r, c=colors, s=1, lw=0, cmap=radar_palette)


'colors' = 'valeurs'
's' une taille pour chaque point 1px
'lw' c'est la forme on peut faire un rond etc etc mais ici on veut juste un pixel
'cmap' map la palette de couleur

Le reste c'est pour décorer l'images avec coordonnées titre etc par exemple pour fare des cercles à 50 000 km, 100 000km, etc..
Les labels seront en gris "gray" et en gras "bold"

    ax.set_rgrids([50000, 100000, 150000, 200000, 250000], labels=['50', '100', '150', '200', '250km'], angle=90, color='gray', weight='bold')


l'alpha permet de gérer la transparence de l'image :

    dessin.set_alpha(1) 

Enfin on sauvegarde l'image dans un ficher :

    savefig(radarimage, dpi=100)

dpi = dots per inch le nombre de points par pouces pour affiner l'image plus y en a

1066 ou bien la ligne c'est le nombre de point qu'il a en ligne droite le Rayon
720 ou bien "column" c'est le nombre de "secteur" d'angle Theta de division de cercle


Ligne 365 c'est le début des données

La ligne juste avant "2 1 0" est la ligne identifiant qui permet de savoir où commencent les données de points.


On va lire d'abord le 1er Rayon donc les 1066 premières lignes. Et on va faire ça 720 (THETA) fois pour avoir chacun des rayons 
Il faut bien lire le Rayon en premier (1066)

On va représenter le "missing" en noir pour les valeur absente.

chaque points d'un rayon est espacé de 250/1066 km
chaque thetha augmente de 360/720 ° soit 1/2 ° par avancement

