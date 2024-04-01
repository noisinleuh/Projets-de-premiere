liste=[7,4,8,1,2,5]

def echange(liste,i,j):
    """
    Rend une liste où la place de deux éléments ont étés inversés.
    
    Parameters
    ----------
    liste : list
        liste étudiée
    i : int
        indice.
    j : int
        indice.

    Returns
    -------
    liste : list
        liste où les éléments d'indice i et j ont été échangés.
    """
    temp=liste[i]
    liste[i]=liste[j]
    liste[j]=temp
    return liste

def mini(liste,début):
    """
    Rend l'indice du minimum d'une liste.
    
    Parameters
    ----------
    liste : list
        liste étudiée.
    début : int
        indice.

    Returns
    -------
    n : int
        indice du nombre le plus petit dans la liste.
    """
    n=début
    for i in range(début,len(liste)):
        if liste[i]<liste[n]:
            n=i
    return n

def tbalai(liste):
    """
    Transforme une liste non triée en liste triée.

    Parameters
    ----------
    liste : list
        liste à trier.

    Returns
    -------
    liste : list
        liste triée.

    """
    for i in range(0,len(liste)):
        echange(liste, i, mini(liste,i))
    return liste

def decal(liste,i,val):
    """
    Insère un élément dans un liste à un indice donné.

    Parameters
    ----------
    liste : list
        liste étudiée.
    i : int
        indice.
    val : any
        élément inséré.

    Returns
    -------
    liste : liste
        liste avec le nouvel élément.

    """
    avant=liste[i]
    liste[i]=val
    for j in range(i,len(liste)-1):
        apres=liste[j+1]
        liste[j+1]=avant
        avant=apres
    liste.append(avant)
    return liste

def place(liste,val):
    """
    Rends la place qu'un nombre devrait prendre dans une liste triée

    Parameters
    ----------
    liste : liste
        liste étudiée.
    val : int or float
        Valeur dont on cherche l'indice.

    Returns
    -------
    i : int
        Indice de la place que devrait prendre la valeur.

    """
    i=0
    while i<len(liste) and liste[i]<val :
        i+=1
    return i

def tinser(liste):
    """
    Transforme une liste non triée en liste triée.

    Parameters
    ----------
    liste : list
        liste à trier.

    Returns
    -------
    res : list
        liste triée.

    """
    res=[liste[0]]
    for val in range(1,len(liste)):
        indice=place(res, liste[val])
        if indice==len(res):
            res.append(liste[val])
        else:
            decal(res,indice,liste[val])
    return res