import requests
import mysql.connector
from bs4 import BeautifulSoup

cnx = mysql.connector.connect(host="localhost", user="root", passwd="", database="")
cursor = cnx.cursor()

car = input()
url ='https://www.truecar.com/used-cars-for-sale/listings/'

r = requests.get(url) #site's link in ('')
soup = BeautifulSoup(r.text , 'html.parser')

data=[]
for card in soup.select('[class="card-content vehicle-card-body order-3 vehicle-card-carousel-body"]'):
    price = card.select_one('[class="heading-3 my-1 font-bold"]').text
    miles = card.select_one('div[class="flex w-full justify-between"]').text
    data.append({
        'price': price , 'miles':miles
    })

query = "INSERT INTO cars VALUES ('data')" 
cursor.execute(query, (data))

print(data)