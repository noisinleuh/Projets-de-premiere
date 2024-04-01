import conversion

réponse=input("Quelle action voulez-vous effectuer? (écrire conversion ou ieee ou calcul) ")
while réponse !="conversion" and réponse != "calcul" and réponse != "ieee"  :
    réponse=input("Quelle action voulez-vous effectuer? (écrire conversion ou ieee ou calcul) ")
if réponse == "conversion":
    conversions=input("Quelle conversion voulez-vous faire? (écrire base en base ou complément à deux ou flottant) ")
    while conversions !="base en base" and réponse != "complément à deux" and réponse != "flottant":
        conversions=input("Quelle conversion voulez-vous faire? (écrire base en base ou complément à deux ou flottant) ")
    if conversions == "base en base":
        a=input("Quel nombre voulez vous convertir? ")
        b1= int(input("En quelle base est-il? (2-36) "))
        while b1<2 or b1>36:
            b1= int(input("En quelle base est-il? (2-36) "))
        b2= int(input("En quelle base voulez vous le convertir? (2-36) "))
        while b1<2 or b1>36:
            b2= int(input("En quelle base voulez vous le convertir? (2-36) "))
        print ("\n Le nombre ", a, " en base ", b2, " est ", conversion.base_en_base(a,b1,b2))
    elif conversions == "complément à deux":
        base=input("Votre nombre est il en décimal ou en complément à deux? (écrire décimal ou complément à deux) ")
        while base !="décimal" and réponse != "complément à deux":
            base=input("Votre nombre est il en décimal ou en complément à deux? (écrire décimal ou complément à deux) ")
        if base=="décimal":
            x=input("Quel est votre nombre? ")
            print ("\n Le nombre ", a, " en complément à deux est ", conversion.decicompl(x))
        else:
            x=input("Quel est votre nombre? ")
            print ("\n Le nombre ", a, " en décimal est ", conversion.compldeci(x))
    elif conversions=="flottant":
        base=input("Votre nombre est il en décimal ou en binaire flottant? (écrire décimal ou binaire) ")
        while base !="décimal" and réponse != "binaire":
            base=input("Votre nombre est il en décimal ou en binaire flottant? (écrire décimal ou binaire) ")
        if base=="décimal":
            x=input("Quel est votre nombre? ")
            print ("\n Le nombre ", a, " en binaire flottant est ", conversion.floatbin(x))
        else:
            x=input("Quel est votre nombre? ")
            print ("\n Le nombre ", a, " en décimal est ", conversion.binfloat(x))

if réponse=="calcul":
    calcul=input("Quel calcul voulez-vous faire? (écrire addition, soustraction ou multiplication) ")
    while calcul !="addition" and calcul!="soustraction" and calcul!="multiplication":
        calcul=input("Quel calcul voulez-vous faire? (écrire addition, soustraction ou multiplication) ")
    if calcul=="addition":
        a=input(str("Premier nombre: "))
        b=input(str("Deuxième nombre: "))
        bits=input("Nombre de bits fixe? (écrire oui ou non) ")
        while bits !="oui" and bits!="non":
            bits=input("Nombre de bits fixe? (écrire oui ou non) ")
        if bits=="oui":
            c=int(input("Combien de bits? "))
            while type(c)!=int:
                c=input(int("Combien de bits? "))
            print("\n La somme de",a,"et",b,"est",conversion.addibin_fixe(a, b, c),"à un nombre de bits de", c)
        else:
            print("\n La somme de",a,"et",b,"est",conversion.addibin(a, b))
    elif calcul=="soustration":
        a=input(str("Premier nombre: "))
        b=input(str("Deuxième nombre: "))
        print("\n La différence de",a,"et",b,"est",conversion.sousbin(a, b))
    elif calcul=="multiplication":
        a=input(str("Premier nombre: "))
        b=input(str("Deuxième nombre: "))
        bits=input("Nombre de bits fixe? (écrire oui ou non) ")
        while bits !="oui" and bits!="non":
            bits=input("Nombre de bits fixe? (écrire oui ou non) ")
        if bits=="oui":
            c=int(input("Combien de bits? "))
            while type(c)!=int:
                c=int(input("Combien de bits? "))
            print("\n Le produit de",a,"et",b,"est",conversion.multibin_fixe(a, b, c),"à un nombre de bits de", c)
        else:
            print("\n Le produit de",a,"et",b,"est",conversion.multibin(a, b))

if réponse=="ieee":
    nombre=float(input("Quel est le nombre décimal que vous voulez convertir en binaire? "))
    bits=input("Quelle précision désirez vous? (écrire simple ou double) ")
    while bits!="simple" and bits!="double":
        bits=input("Quelle précision désirez vous? (écrire simple ou double) ")
    if bits=="simple":
        bits=1
    elif bits=="double":
        bits=2
    print("\n Le nombre ",nombre," en IEEE 754 avec précision ", bits," est ", conversion.decieee(nombre, bits))