# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:15:03 2018

@author: coriande
"""

##ex 22           
def score_lettre(lettre):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a=0
    for i in range (25):
        if lettre==alphabet[i]:
            a=i+1
            return (int(a))
    return a
    ##lorsque l'on tombe sur les guillemets ou s'il ne s'agit pas d'une lettre
##la fonction retourne le numero de la lettre de l'alphabet

def score_mot(mot):
    score=0
    mot=str(mot)
    for i in range (len(mot)):
        score+=score_lettre(mot[i])
    return score
## la fonction calcule le score d'un mot en fonction de ses lettres, elle ne prend pas en compte la place du mot dans la liste
    
##assert score_mot("ABC")==6
##print(score_mot("COLIN"))

def score_liste(liste):
    score=0
    for i in range(len(liste)):
##on parcours tous les nombres de la liste
        score+=score_mot(liste[i])*(i+1)
##apres avoir calculé le score du mot, on le multiplie par sa position (i+1)
    return score

##assert score_liste(["COLIN","AAA"])==53+3*2

def score():
##il faut maintenant trier notre liste par ordre alphabétique et lui appliquer le trie
    document=open("p022_names.txt","r")
    for ligne in document:
        chaine=ligne
        l=chaine.split(',')
        l=sorted(l)
    score=score_liste(l)
##trier une liste
    return score

print(score())
