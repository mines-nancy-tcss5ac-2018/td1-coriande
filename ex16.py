# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:07:29 2018

@author: coriande
"""


##ex 16        
def digit(n):
    somme=0
    while n!=0:
        somme+=n%10
## le reste de la division euclidienne correspond à la dizaine
        n=(n-n%10)//10
## on enlève à n sa dizaine et on divise par 10 pour traiter le chiffre suivant
    return somme

assert (digit(22224)==12)

##print(digit(2**1000))

