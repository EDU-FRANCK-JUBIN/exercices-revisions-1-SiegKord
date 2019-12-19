# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:37:50 2019

@author: Nicolas
"""

import turtle as tu
from turtle import Screen

#Définition du caractère de remplissage
space=" "

#Définition du caractère de dessin du sapin 
char_sapin="^"

#Nombre de lignes constituant le sapin 
nbre_ligne= 12

#Nombre de "blancs" à insérer avant le ^
padSize=nbre_ligne- 1

#Position actuelle en lignes dans le dessin du sapin
num_ligne= 0

#Saut d'une ligne pour ergonomie
print()

for num_ligne in range(1,nbre_ligne+ 1) :
    #Nombre de caractères sapin à dessiner
    if(num_ligne== 1 ) :
        nbre_char_sapin= 1
    else:
        nbre_char_sapin= 2 *num_ligne-1
        
    #Affichage d'une ligne de sapin 
    print(space*padSize,char_sapin*nbre_char_sapin,space*padSize)
    
    #Décrémenter le nombre de caractères de remplissage
    padSize-= 1
