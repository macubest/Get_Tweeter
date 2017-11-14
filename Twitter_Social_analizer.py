# -*- coding: utf-8 -*-
# -*- coding: 850 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import MySQLdb
import re
from re import sub




db = MySQLdb.connect(host="localhost",    # tu host, usualmente localhost
                     user="macubest",         # tu usuario
                     passwd="admin1234",  # tu password
                     db="info_db"
                     )        # el nombre de la base de datos


browser = webdriver.Firefox()
base_url ='https://twitter.com/search?vertical=default&q=%'
query = '23banreservas&src=typd'

url = base_url + query

browser.get(url)
time.sleep(1)

count = 0
while count < 50:
 browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(2)
 count = count +1

body = browser.find_element_by_tag_name('body')

tweets_txt = browser.find_elements_by_class_name('tweet-text')
nombre = browser.find_elements_by_tag_name('b')
tweet_id = browser.find_elements_by_id('data-tweet-id')

#print(tweet_id.Text)
cur = db.cursor()
count = 0
i = 0
for tweet in tweets_txt:
 #tweet_i = tweet_id[0]
 tweet_n = nombre[i]
 #print(tweet_i.text.encode("utf-8"))
 #print("USUARIO")
 #print(tweet_n.text)
 i =i +1
 #print("Text")
 tweet_text = str((tweet.text.encode("utf-8")))
 #cur.execute("INSERT INTO social_tbl values(3,'"+social_usr+"','"+social_text2+","'twitter'")")
 #cur.execute("INSERT INTO social_tbl values("+str(i)+",'"+tweet_n.text+"','"+tweet.text+"','twitter')")
 #db.commit()
 patron = re.compile(r'(?i)(\W|^)(altos|alto|basura|#basura|cobro|dudoso|#dudoso|disparate|estafadores|#estafadores|fraudulento|#fraudulento|filas|impuesto|#impuesto|desastre|desastres|lentitud|largas|ladrones|molesto|molesta|mentiroso|mucho|mierda|proqueria|pesimo|problema|peor|queja|reserva|robo|solucionen|servicio|timadores|vamos|verguenza\smía)(\W|$)') 
 cadena =(patron.findall(tweet_text))
 if cadena:
   print("USUARIO : |" +str(tweet_n.text) +"|")	
   #print("COINCIDENCIAS :")
   print("TWEET "+str(tweet.text.encode("utf-8")))
   print("---------------------------------------")
	  #print("Coincidencias")	 
browser.close()

