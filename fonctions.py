from os import write
import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import webbrowser



def get_category_url(lien):
#on récupère les liens de chaque catégories
  page = requests.get(lien)
  soup = BeautifulSoup(page.content, 'html.parser')
  soup_category = soup.find('div', {'class', 'side_categories'})
  links = [lien + a.get('href') for a in soup_category.find_all('a', href=True)]
  #print(links)
  return links

#on récupère les livres de chaque catégories
def get_all_books(books):
  # page_book = requests.get(books)
  # soup_books = BeautifulSoup(page_book.content, 'html.parser')
  # soup_book_link = soup_books.find('div', {'class', 'image_container'})
  # liens_livres = [books + a.get('href') for a in soup_book_link.find_all('a', href = True)]
  # print(liens_livres)
  for elements in books:
    books_images = elements.find("a")
    lien = books_images["href"]
    new_liens = urljoin("https://books.toscrape.com/catalogue/category/books/travel_2/index.html", lien)
    # print(new_liens) 

def get_data_book(lien_livre):
  lien_du_livre = lien_livre
  page_data = requests.get(lien_livre)
  soup_data = BeautifulSoup(page_data.content,'html.parser')

  soup_data_titre = soup_data.find('h1')
  soup_data_price = soup_data.find('p',{'class', 'price_color'})
  soup_data_book = soup_data.find_all('tr')
  soup_image = soup_data.find('img')
  titre = soup_data_titre.get_text()
  prix = soup_data_price.get_text()
 

  image = soup_image['src']

  lien_image = urljoin('https://books.toscrape.com/', image)

  upc = soup_data_book[0].get_text()
  type_produit = soup_data_book[1].get_text()
  prix_sans_taxe = soup_data_book[2].get_text()
  prix_avec_taxe = soup_data_book[3].get_text()
  taxe = soup_data_book[4].get_text()
  disponibilite = soup_data_book[5].get_text()
  review = soup_data_book[6].get_text()

  liste_data = []
  liste_data.append(lien_du_livre)
  liste_data.append(upc)
  liste_data.append(type_produit)
  liste_data.append(prix_sans_taxe)
  liste_data.append(prix_avec_taxe)
  liste_data.append(taxe)
  liste_data.append(disponibilite)
  liste_data.append(review)
  liste_data.append(titre)
  liste_data.append(lien_image)
  #création du dictionnaire
  dic_data_book = {}
  #on créée la liste des clés
  keys = ['lien du livre', 'UPC', 'Product Type', 'Price (excl. tax)','Price (incl. tax)', 'Tax', 'Availability','Number of reviews', 'titre', 'image']
  #on loop dans les clés et la liste de données  
  for key, values in zip(keys, liste_data):
    values = values.replace(key,'').strip()
    dic_data_book[key] = values

  #manque url livre
  return dic_data_book
 
def get_image_book(url_image):
  pass

#récupère les données dans un csv
#pas bien agencé dans le csv
def write_book_csv(dictionnaire):
   with open('data_books.csv', 'w',) as csv_file:  
      writer = csv.writer(csv_file)
      for key, value in dictionnaire.items():
         writer.writerow([key, value])

      