# -*- coding: utf-8 -*-
import datetime
import tmdbsimple as tmdb
import telegram
import random
import operator
from plexapi.server import PlexServer
import requests
import datetime
import unicodedata

 
now = datetime.datetime.now() 

#TELEGRAM INFO
USERID = 'ID telegram to send message' 
KEY= 'API OF THE BOT'

#TMDB INFO
tmdb.API_KEY = 'yourTMDB-API'

#PLEX INFO 
PLEX_URL = 'http://yourIP:32400'
PLEX_TOKEN = 'yourplextoken'

#LANGUAGE CODE. example 'es-ES'
lang = 'XXXX'

# Your library names for movies
LIBRARY_NAMES = 'MOVIES' 

plex = PlexServer(PLEX_URL, PLEX_TOKEN)

def peli_random(library_name):
    	
    movies = plex.library.section(library_name)
	lista = []
	
	for video in movies.search():
		lista += [video]
    
	return random.choice(lista)



bot = telegram.Bot(token=KEY)

titulo = peli_random(LIBRARY_NAMES).title
 
search = tmdb.Search()
response = search.movie(language=lang,query=titulo)
busqueda = None
busqueda2 = None
for r in search.results:
	ye = r['release_date'].split("-")
	print ye[0],fecha, r['title'],titulo
	if r['title'] == titulo and fecha == ye[0]:
		print "asingno"
		busqueda = r
		break
	if busqueda == None and r['title'] == titulo:
		if busqueda != None:
			fecha2 = busqueda2['release_date'].split("-")
			if abs(int(fecha)-int(ye))<abs(int(fecha)-int(fecha2)):
				busqueda2 = r
				print "fuerzo mejor encontrado"
			else:
				continue
		else:
			busqueda2 = r
			print "fuerzo primero"

if busqueda == None and busqueda2 != None :
	busqueda = busqueda2
elif busqueda2 == None:
	busqueda = search.results[0]
	
	
link_foto ='https://image.tmdb.org/t/p/w500/'+busqueda['poster_path']

dia = now.strftime("%d-%m-%Y")
texto = '📺🎬 PLEX PELÍCULA ALEATORIA DEL DÍA '+dia+' 🎬📺\n\n'+ busqueda['title'].encode('utf-8')+'\n\n📚Sinopsis: '+busqueda['overview'].encode('utf-8')+'\n\n📆Fecha de Lanzamiento: '+busqueda['release_date'].encode('utf-8')+'\n\n⭐️Valoración: '+str(busqueda['vote_average'])+'\n\n'+ link_foto.encode('utf-8')


bot.send_message(chat_id=USERID, text=texto )

