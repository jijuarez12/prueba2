import urllib.request
def cantidadDePalabras(url):
    objetoArchivo = urllib.request.urlopen(url)
    texto_archivo = objetoArchivo.read().decode('utf-8')

    lista = texto_archivo.split()
    return len(lista)

URL = "https://www.gutenberg.org/files/2000/2000-0.txt"
cont = cantidadDePalabras(URL)
print("La cantidad de palabras es: ",cont)