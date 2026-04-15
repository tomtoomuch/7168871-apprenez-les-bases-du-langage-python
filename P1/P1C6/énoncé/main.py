plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
print(plateformes_sociales[2])
plateformes_sociales[2] = "LinkedIn"
print(plateformes_sociales[2])
plateformes_sociales.append("TikTok")
print(plateformes_sociales)
plateformes_sociales.insert(2,"Snapchat")
print(plateformes_sociales)
plateformes_sociales.remove("Snapchat")
print(plateformes_sociales)

print("via les tuples")
plateformes_sociales_tuple = ("Facebook","Instagram", "TikTok","Twitter")

print("Exercice chapitre")
fruits = ["pomme","banane","orange"]
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.remove("orange")
fruits[1] = "ananas"
print(f"Cette liste contient {len(fruits)} éléments.")
fruits.sort()
print(fruits)