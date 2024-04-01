import alphabet
import ecrire

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

texte=input("Ecrivez votre mot ou votre phrase: ")
taille=int(input("Chosissez une taille entre 10 et 50: "))
while taille<10 or taille>50:
    taille=int(input("Chosissez une taille entre 10 et 50: "))
épaisseur=input("Voulez-vous que votre texte soit en gras ? (écrivez oui ou non): ")
while épaisseur!="oui" and épaisseur!="non":
    épaisseur=input("Voulez-vous que votre texte soit en gras ? (écrivez oui ou non): ")
souligne=input("Voulez-vous que votre texte soit souligné ? (écrivez oui ou non): ")
while souligne!="oui" and souligne!="non":
    souligne=input("Voulez-vous que votre texte soit souligné ? (écrivez oui ou non): ")
couleur=input("Choisissez une couleur (blue, green, red, cyan, magenta, yellow, black): ")
while couleur!="blue" and couleur!="green" and couleur!="red" and couleur!="cyan" and couleur!="magenta" and couleur!="yellow" and couleur!="black" and couleur!="white" and couleur!="aléatoire":
    couleur=input("Choisissez une couleur (blue, green, red, cyan, magenta, yellow, black, white): ")


ecrire.ecrire(texte,taille,épaisseur,couleur,souligne)