import feedparser
import sys
import os
from datetime import datetime

# Función para buscar noticias en el feed RSS por una palabra clave
def buscar_noticias(feed_url, palabra_clave):
    feed = feedparser.parse(feed_url)
    
    noticias_coincidentes = []
    
    for entry in feed.entries:
        titulo = entry.title
        
        # Verificar si el campo 'summary' existe en el objeto entry
        if 'summary' in entry:
            descripcion = entry.summary
        else:
            descripcion = "No hay descripción disponible."
        
        # Verificar si la palabra clave está en el título o descripción
        if palabra_clave.lower() in titulo.lower() or palabra_clave.lower() in descripcion.lower():
            noticias_coincidentes.append((titulo, descripcion))
    
    return noticias_coincidentes

# Verificar si se proporciona una palabra clave como argumento en la línea de comandos
if len(sys.argv) != 2:
    print("Uso: python buscar_noticias.py <palabra_clave>")
    sys.exit(1)

palabra_clave = sys.argv[1]

# Directorio donde se almacenarán los resultados
directorio_resultados = "/home/cyberpunk/CyberpunkTools_resultados"  

# Verificar si el directorio existe, si no, créalo
if not os.path.exists(directorio_resultados):
    os.makedirs(directorio_resultados)

# Obtener la fecha y hora actual como parte del nombre del archivo
fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nombre_archivo = f"{directorio_resultados}/noticias_{fecha_actual}.txt"

# Lista de enlaces RSS de los principales portales de noticias en español
feeds = [
# Agrega aquí los enlaces RSS de los portales de noticias que desees buscar
   'http://www.bbc.co.uk/mundo/temas/america_latina/index.xml',
   'http://rss.cnn.com/rss/edition_world.rss',
   "https://feeds.bbci.co.uk/news/rss.xml",
   "http://rss.cnn.com/rss/edition.rss",
   "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
   "https://www.theguardian.com/world/rss",
   "https://www.aljazeera.com/xml/rss/all.xml",
   "https://apnews.com/rss",
   "http://feeds.nbcnews.com/nbcnews/public/news",
   "https://www.washingtonpost.com/rss",
   "https://abcnews.go.com/abcnews/topstories",
   "https://news.yahoo.com/rss/",
   "http://rssfeeds.usatoday.com/usatoday-NewsTopStories",
   "https://www.latimes.com/rss2.0.xml",
   "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
   "https://www.independent.co.uk/news/rss",
   "http://feeds.foxnews.com/foxnews/latest",
   "https://www.npr.org/rss/rss.php?id=1001",
   "https://www.cbc.ca/cmlink/rss-topstories",
   "https://www.smh.com.au/rss/feed.xml"
   # Agrega más feeds RSS aquí
]

# Crear y abrir el archivo para escribir los resultados
with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    archivo.write(f"Resultados de búsqueda para '{palabra_clave}'\n\n")
    
    # Realizar la búsqueda en cada feed RSS
    for feed_url in feeds:
        noticias_coincidentes = buscar_noticias(feed_url, palabra_clave)
        
        if noticias_coincidentes:
            archivo.write(f"Resultados en {feed_url}:\n")
            
            for i, (titulo, descripcion) in enumerate(noticias_coincidentes, start=1):
                archivo.write(f"{i}. Título: {titulo}\n")
                archivo.write(f"   Descripción: {descripcion}\n\n")
                
                print(f"{i}. Título: {titulo}")
                print(f"   Descripción: {descripcion}\n")
        else:
            archivo.write(f"No se encontraron noticias relacionadas con '{palabra_clave}' en {feed_url}\n")
            print(f"No se encontraron noticias relacionadas con '{palabra_clave}' en {feed_url}")

print(f"Los resultados se han guardado en el archivo: {nombre_archivo}")
