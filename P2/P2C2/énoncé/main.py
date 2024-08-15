def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
liste = input("Saisissez une liste de nombres séparés par des virgules :")
liste.split(",")
print("Liste des nombre", liste)


somme=0
for nombre in liste:
    somme += int(nombre)
    print("Somme des nombres : ", somme)

moyenne = somme/len(liste)
print("La moyenne des nombres : ", moyenne)

for nombre in liste:
    if int(nombre) > moyenne:
        nombre_sup_moyenne +=1
    print("Les nombres supérieurs à la moyenne sont : ", nombre_sup_moyenne)

nombre_pair = 0
i = 0
while i < len(liste):
    if int(list[i]) % 2 == 0:
        nombre_pair +=1
    i +=1
print("Nombre de nombres pairs : ", nombre-pair)

    
 


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
