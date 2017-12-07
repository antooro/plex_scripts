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
response = search.movie(language='es-ES',query=titulo)

busqueda = search.results[0]
link_foto ='https://image.tmdb.org/t/p/w500/'+busqueda['poster_path']

dia = now.strftime("%d-%m-%Y")
texto = '📺🎬 PLEX PELÍCULA ALEATORIA DEL DÍA '+dia+' 🎬📺\n\n'+ busqueda['title'].encode('utf-8')+'\n\n📚Sinopsis: '+busqueda['overview'].encode('utf-8')+'\n\n📆Fecha de Lanzamiento: '+busqueda['release_date'].encode('utf-8')+'\n\n⭐️Valoración: '+str(busqueda['vote_average'])+'\n\n'+ link_foto.encode('utf-8')


bot.send_message(chat_id=USERID, text=texto )

