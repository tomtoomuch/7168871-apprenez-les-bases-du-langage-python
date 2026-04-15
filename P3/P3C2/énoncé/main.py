import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
with open("./index.html", 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

#print(page.content)

titre_page = soup.title.string
print(titre_page)

h1_titre = soup.find(id="titre").string
print(h1_titre)

# Création du dictionnaire pour stocker les produits
produit = {
    "nom_produit": "",
    "prix_produit": "",
    "description_produit": ""
}

#Créer une boucle pour extraire les données des produits pour alimenter le dictionnaire
noms_produits = soup.select("li.product>h2")
print(noms_produits)

prix_produits = soup.select("li.product>h2+p.price")
print(prix_produits)

descriptions_produits = soup.select("p.price+p")
print(descriptions_produits)