#a
N = int(input("Ingrese la cantidad de numeros: "))
lista = []
for i in range(0,N):
    dato = int(input("Dato: "))
    lista.append(dato)

#b
for p in range(1,3):
    lista.remove(min(lista))

#c
sum = 0
for k in range(0,len(lista)):
    sum = sum + lista[k]
promedio = sum/len(lista)
print("El promedio de los numeros restantes es: ",promedio)

#d
cont_num_mayores_prom = 0
for m in range(0,len(lista)):
    if lista[m]>promedio:
        cont_num_mayores_prom = cont_num_mayores_prom + 1
print("La cantidad de numeros mayores al promedio es: ",cont_num_mayores_prom)

#e
print("Inserte datos para la segunda version")
lista_a_reemplzar = N*[None]
for o in range(0,N):
    lista_a_reemplzar[o] = int(input("Dato: "))
print("La lista para la segunda version: ",lista_a_reemplzar)