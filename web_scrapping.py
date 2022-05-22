# Import libraries
import requests
from bs4 import BeautifulSoup
from csv import writer
import locale
from datetime import datetime
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Create an URL object
url = 'https://www.mundonets.com/baloto/'
# Create object page
page = requests.get(url)
page.text
baloto_list = []
revancha_list = []

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
# Getting fecha ultimo sorteo
fechaI=soup.select('td', class_= 'tabla_sorteos_baloto')[3].text
fecha= datetime.strptime(fechaI, '%d %B %Y')
fecha=fecha.date()

# Getting balotas baloto
baloto=soup.find_all('li', class_= 'bola amarilla')
for b in baloto:
    baloto = b.text
    baloto_list.append(baloto.strip())

# Getting balotas revancha
revancha=soup.find_all('li', class_= 'bola roja')
for r in revancha:
  revancha = r.text
  revancha_list.append(revancha.strip())

SB_B=revancha_list[0]
SB_R=baloto_list[5]
baloto_list[5]=SB_B
baloto_list.insert(0, fecha)
del revancha_list[0]
revancha_list.insert(5, SB_R)
revancha_list.insert(0, fecha)

with open('baloto.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(baloto_list)
    f_object.close()
with open('revancha.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(revancha_list)
    f_object.close()