from os import write
import requests
import csv
import urllib
from PIL import Image
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from fonctions import get_category_url, write_book_csv
from fonctions import get_all_books
from fonctions import get_data_book
from fonctions import write_book_csv
#on stock l'url et on la request via  get
url = "http://books.toscrape.com/"

#on stock les liens de la page
#links = soup.find_all("a")
links = get_category_url(url)


categorie_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
lien_livre = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
#on créée une liste des liens entiers
page = requests.get(categorie_url)
soup = BeautifulSoup(page.content, 'html.parser')
soup_books = soup.find_all("article", {"class", "product_pod"})

#liens des livres
liens_livres = get_all_books(soup_books)

data_livres = {}
data_livres = get_data_book(lien_livre)

print(data_livres)

#on récupère l'image d'une url
lien_image = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page_image = requests.get(lien_image)
soup_image = BeautifulSoup(page.content, 'html.parser')
image = soup.find('img')
image_data = image['src']
image_link = urljoin('https://books.toscrape.com/', image_data)
print(image_link)


image_save = requests.get(image_link).content
with open('image_livre.jpg','wb') as handler:
   handler.write(image_save)


# print(soup_data_all)


#print(links) 

# #création fichier csv
# liste_livres = open("liste_livres.csv","w")
# en_tete = ["product_page_url", "universal_ product_code","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]

write_book_csv(data_livres)

