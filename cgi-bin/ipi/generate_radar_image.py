#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi, sys
from pylab import *
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap

# Donnees specifique au radar :
# La distance du radar divisé par le nombre de points sur un rayon nous donnera la valeur 
# à incrémenter à R à chaque ligne.
# 360 ° divisé par le nombre de fragments THETA nous donnera l'incrémentation de THETA à chaque
# lignes.

radar_distance = 128

# Ces deux valeurs sont trouvées dans le fichier :
r_division = 1066
theta_divsion = 720

# Calcul de l'increment :
i_theta = 360.0 / 720.0

i_r = 128.0 / 1066.0

# Fichier
radar_file = "text_files/Villers_20140102_110000T18_Zhpol300m.txt"

# On va devoir remplir ces trois tableaux en parcourant le fichier radar txt
theta = []
r = []
values = []

line_count = 1


with open(radar_file) as f:
    for i in xrange(365):
        f.next()
    i_line = 1
    theta_value = 0.0
    r_value = 0.0
    for line in f:
        values.append(line.lstrip().split(" ")[0])
        r.append(r_value)
        if i_line % 1066 == 0:
            theta_value += i_theta
            r_value = 0.0

        theta.append(theta_value)
        r_value += i_r
        i_line += 1

print r[10]
print theta[1077]
print values[18]

colors = values
ax = subplot(111, polar=True)
radar_palette = ListedColormap([
'#000083', '#00009f', '#0000af', '#0000bf', '#0000cf', '#0000df', '#0000ef', '#0000ff', '#000fff',
'#001fff', '#002fff', '#003fff', '#004fff', '#005fff', '#006fff', '#007fff', '#009fff', '#00afff',
'#00bfff', '#00cfff', '#00dfff', '#00efff', '#00ffff', '#0fffef', '#1fffdf', '#2fffcf', '#3fffbf',
'#4fffaf', '#5fff9f', '#6fff8f', '#7fff7f', '#8fff6f', '#9fff5f', '#afff4f', '#bfff3f', '#cfff2f',
'#dfff1f', '#efff0f', '#ffff00', '#ffef00', '#ffdf00', '#ffcf00', '#ffbf00', '#ffaf00', '#ff9f00',
'#ff8f00', '#ff6f00', '#ff5f00', '#ff4f00', '#fe3f00', '#ff2f00', '#ff1f00', '#ff0f00', '#ff0000',
'#ef0000', '#df0000', '#cf0000', '#bf0000', '#af0000', '#9f0000', '#8f0000', '#7f0000'
], 'indexed')
