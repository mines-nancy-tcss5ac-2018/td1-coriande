# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:06:49 2018

@author: coriande
"""


##exercice 55
def pal(n):
    ##verifie si un nombre est un palindrone 
    n=str(n)
    for i in range (len(n)//2):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True

assert pal(567765)==True
assert pal(56775)==False

def inverse(n):
    n=str(n)
#nombre à inverser
    n1=""
#nombre inversé
    for i in range(len(n)):
        n1=n1+n[len(n)-i-1]
    n1=int(n1)
    return n1
    
assert inverse(567)==765

def lychrel(n):
    ##cette fonciton regarde si un nombre n est un lychrel
    a=0
    s=n+inverse(n)
    if not pal(s):
        while a<=50:
            s=s+inverse(s)
            a+=1
            if pal(s):
                return False
        return True
    else :
        return False
        
assert lychrel(196)==True

def nbre_lychrel(n):
    #on va ici compter le nombre de lychrels inférieurs à n
    a=0
    #on vérifie si a est un lychrel
    s=0
    #compteur des lychrels
    while a<=n:
        if lychrel(a):
            s+=1
        a+=1
    return s

##print(nbre_lychrel(10000))

    
