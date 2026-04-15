races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(100):
    print(f"{x} bouteilles à la mer")

capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print(f"{capacite_actuelle}/{capacite_maximale}")

#for i in range(10):
#   if i == 5:
#        break
#    print(i)

print("Exo chapitre")
nombres = input("Saisissez plusieurs nombres séparés par des virgules (sans espaces) -->")
liste = nombres.split(",")
print("Liste des nombres : ", liste)
liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)
print("Liste des nombres entiers : ", liste_entiers)

somme = 0
for nombre in liste_entiers:
    somme +=nombre
print("Somme des entiers : ", somme)

moyenne = somme / len(liste_entiers)
print("La moyenne de cette liste est : ", moyenne)

nombres_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombres_au_dessus_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne : ", nombres_au_dessus_moyenne)