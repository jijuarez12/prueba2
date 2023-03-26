import urllib.request
URL = "https://www.gutenberg.org/files/2000/2000-0.txt"
objetoArchivo = urllib.request.urlopen(URL)
texto_archivo = objetoArchivo.read().decode('utf-8')
lista_lineas = texto_archivo.split("\n")

#a
for i in range(0,10):
    print(lista_lineas[i])
lista_palabras = texto_archivo.split()

#b
for item in lista_palabras:
    cant_repetidas = lista_palabras.count(item)
    if cant_repetidas>1:
        for i in range(0,cant_repetidas):
            lista_palabras.remove(item)
    print(item)

#c
for item in lista_palabras:
    print(item)
conteo = 0

#d
for item in lista_palabras:
    if len(item)>2 and item[0] == item[-1]:
        conteo = conteo + 1
print("La cantidad de palabras con mas de 2 letras y con el primer y ultimo caracter iguales es: ",conteo)