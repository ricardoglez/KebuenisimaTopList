import requests
from bs4 import BeautifulSoup as bs

def obtenerLista(fech):
	fecha = str(fech)
	archivoNuevo = open("listaKebuena" + fecha, 'w')
	url = "http://www.kebuena.com.mx/kebuenisimas-anteriores?fecha="
	urlAct = url + fecha
	r = requests.get(urlAct)
	soup = bs(r.content)
	lista = soup.find_all("div", {"class": "lista"})
	for contenido in lista:
	    itm = contenido.find_all("div", {"class": "itm-body"})
	    contador = 0
	    for caract in itm:
	        titulo = contenido.find_all("h2")
	        info = contenido.find_all("p")
	        if(contador > 0 & contador < 19):
	        	tit = titulo[contador].text.encode('utf-8')
	        	tit = tit.strip()
	        	aut = "Autor: " + info[contador * 2 - 1].text.encode('utf-8')
	        	aut = aut.strip()
	        	album = "Album: " + info[contador * 2].text.encode('utf-8')
	        	album = album.strip()

	        	archivoNuevo.write(str(contador) + " Titulo: " + tit + '\n')
	        	archivoNuevo.write(str(contador) + " " + aut + '\n')
	        	archivoNuevo.write(str(contador) + " " + album + '\n')
	        elif (contador == 0):
	        	tit = titulo[contador].text.encode('utf-8')
	        	tit = tit.strip()

	        	archivoNuevo.write("/////Fecha///////"+ tit+'\n')
	        contador += 1
	archivoNuevo.close()


#Mayo
obtenerLista(20150509)
obtenerLista(20150516)
obtenerLista(20150523)
obtenerLista(20150530)
#Junio
obtenerLista(20150606)
obtenerLista(20150613)
obtenerLista(20150620)
obtenerLista(20150627)
#Julio
obtenerLista(20150704)
obtenerLista(20150711)
obtenerLista(20150718)
obtenerLista(20150725)
#Agosto
obtenerLista(20150801)
obtenerLista(20150808)
obtenerLista(20150815)
obtenerLista(20150822)
obtenerLista(20150829)
#Septiembre
obtenerLista(20150905)
obtenerLista(20150912)
obtenerLista(20150919)
obtenerLista(20150926)
#Octubre
obtenerLista(20151003)
obtenerLista(20151010)
obtenerLista(20151017)
obtenerLista(20151024)
obtenerLista(20151031)
#Noviembre
obtenerLista(20151107)
obtenerLista(20151114)



