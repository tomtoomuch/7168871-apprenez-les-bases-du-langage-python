nombre_utilisateur = input("Premier nombre --> ")
if nombre_utilisateur.isnumeric():
    nombre1 = int(nombre_utilisateur)
    print(f"Le premier nombre saisi est le : {nombre1}.")
    nombre_utilisateur = ""
    nombre_utilisateur = input(f"Saississez un second nombre --> ")
    if nombre_utilisateur.isnumeric():
        nombre2= int(nombre_utilisateur)
        print(f"Le second nombre saisi est le : {nombre2}. Choisissez maintenant une opération.")
        operation_utilisateur = input("--> ")
        operations_valides = ("+","-","*","/")
        if operation_utilisateur in operations_valides:
            operation = operation_utilisateur
            print(f"Votre opération : {nombre1} {operation} {nombre2} = ???")
            match operation_utilisateur:
                case "+":
                    resultat = nombre1 + nombre2
                    print(f"Le résultat de cette addition est  : {resultat}")
                case "-":
                    resultat = nombre1 - nombre2
                    print(f"Le résultat de cette soustraction est  : {resultat}")
                case "*":
                    resultat = nombre1 * nombre2
                    print(f"Le résultat de cette multiplication est : {resultat}")
                case "/":
                    if nombre2 != 0:
                        resultat = nombre1 / nombre2
                        print(f"Le résultat de cette division est : {resultat}; soit arrondi à l'entier le plus proche : {round(resultat)}")
                    else:
                        raise SystemExit("La division par 0 n'est pas possible. Fin du programme.")
        else:
            raise SystemExit("Votre saisie est incorrecte. Fin du programme.")
    else:
#       nombre_utilisateur = ""
#       print("Votre saisie est incorrecte. Saisissez un nombre entier !")
#       nombre_utilisateur = input("--> ")
        raise SystemExit("Votre saisie est incorrecte. Fin du programme.")