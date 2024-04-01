import alphabet
from turtle import*
import random as r

def ecrire(texte,taille,épaisseur,couleur,souligne):
    hideturtle()
    reset()
    tailleTotale=0
    smile=0
    coeur=0
    if épaisseur=="oui":
        width(3)
    for lettre in texte:
        curTaille = taille
        code=ord(lettre)
        if code==41:
            if smile==1:
                tailleTotale+=alphabet.largeur_smile(curTaille)
                smile=2
            else:
                smile=0
        if code>=65 and code<=90:
            lettre=chr(code+32)
            curTaille=1.3*taille
            code=ord(lettre)
        if code==32:
            tailleTotale+=curTaille*2/3
        if code==39:
             tailleTotale+=alphabet.largeur_apos(curTaille)
        if code==58:
            smile=1
        if code==60:
            coeur=1
        if code>=48 and code<=57:
            if code==48:
                lettre="zéro"
            if code==49:
                lettre="un"
            if code==50:
                lettre="deux"
            if code==51:
                if coeur==1:
                    tailleTotale+=alphabet.largeur_coeur(curTaille)
                    coeur=2
                else:
                    coeur=0
                    lettre="trois"
            if code==52:
                lettre="quatre"
            if code==53:
                lettre="cinq"
            if code==54:
                lettre="six"
            if code==55:
                lettre="sept"
            if code==56:
                lettre="huit"
            if code==57:
                lettre="neuf"
        if code>=97 and code<=122 or code>=48 and code<=57 and coeur!=2 or code==224 or code==232 or code==233:
            tailleTotale+=getattr(alphabet, "largeur_"+lettre)(curTaille)
        else:
            tailleTotale+=taille*2/3
        tailleTotale+=0.25*taille
    up()
    forward(-tailleTotale/2)
    down()
    
    for lettre in texte:
        if couleur=="aléatoire":
            couleurs=["blue","green","red","cyan","magenta","yellow","black"]
            color(couleurs[r.randint(0, 6)])
        else:
            color(couleur)
        curTaille = taille
        code=ord(lettre)
        if code>=65 and code<=90:
            lettre=chr(code+32)
            curTaille=1.3*taille
            code=ord(lettre)
        
        if code==32:
            alphabet.space(curTaille)
        if code==39:
            alphabet.apos(curTaille)
        if code==33:
            alphabet.exc(curTaille)
        if code==63:
            alphabet.intero(curTaille)
        if code==46:
            alphabet.point(curTaille)
        if code==41:
            if smile==1:
                None
            if smile==2:
                alphabet.smile(curTaille)
        if code>=48 and code<=57:
            if code==48:
                lettre="zéro"
            if code==49:
                lettre="un"
            if code==50:
                lettre="deux"
            if code==51:
                if coeur==1:
                    None
                if coeur==2:
                    alphabet.coeur(curTaille)
                else:
                    lettre="trois"
            if code==52:
                lettre="quatre"
            if code==53:
                lettre="cinq"
            if code==54:
                lettre="six"
            if code==55:
                lettre="sept"
            if code==56:
                lettre="huit"
            if code==57:
                lettre="neuf"
        if code>=97 and code<=122 or code>=48 and code<=57 and coeur!=2 or code==224 or code==232 or code==233:
            getattr(alphabet, lettre)(curTaille)
        else:
            alphabet.space(curTaille)
        alphabet.interlettre(curTaille)
         
    if souligne=="oui":
        up()
        forward(-tailleTotale)
        right(90)
        forward(0.5*taille)
        left(90)
        down()
        forward(tailleTotale)