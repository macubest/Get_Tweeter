# -*- coding: utf-8 -*-
# -*- coding: 850 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import MySQLdb
import re
from re import sub
#Creamos una coneccion a la pagina web
browser = webdriver.Firefox()
base_url ='https://twitter.com/search?vertical=default&q=%'
query = '23banreservas&src=typd'
url = base_url + query
browser.get(url)
time.sleep(1)
#contamos la cantidad de scroll que necesitamos para cargar los comentarios
count = 0
while count < 50:
 browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(2)
 count = count +1
#filtramos el texto por clases 
body = browser.find_element_by_tag_name('body')
tweets_txt = browser.find_elements_by_class_name('tweet-text')
nombre = browser.find_elements_by_tag_name('b')
tweet_id = browser.find_elements_by_id('data-tweet-id')
#entramos el en loop para validar cada comentario
cur = db.cursor()
count = 0
i = 0
for tweet in tweets_txt:
 tweet_n = nombre[i]
 i =i +1
 tweet_text = str((tweet.text.encode("utf-8")))
 #filtramos los comentarios bajo los parametros especificados
 patron = re.compile(r'(?i)(\W|^)(altos|alto|basura|#basura|cobro|dudoso|#dudoso|disparate|estafadores|#estafadores|fraudulento|#fraudulento|filas|impuesto|#impuesto|desastre|desastres|lentitud|largas|ladrones|molesto|molesta|mentiroso|mucho|mierda|proqueria|pesimo|problema|peor|queja|reserva|robo|solucionen|servicio|timadores|vamos|verguenza\smía)(\W|$)') 
 cadena =(patron.findall(tweet_text))
 if cadena:
   print("USUARIO : |" +str(tweet_n.text) +"|")	
   print("TWEET "+str(tweet.text.encode("utf-8")))
   print("---------------------------------------")
# una ves terminado cerramos el navegador automaticamente	  	 
browser.close()

