import random
m = int(input("Ingrese la cantidad de elementos de las listas: "))

#a
listaA = []
acumA = ""
for i in range(0,m):
    listaA.append(int(input("Dato para lista A: ")))
    acumA = acumA + str(listaA[i]) + ' '
print("Lista A: ",acumA)

#b
listaB = []
acumB = ""
for p in range(0,m):
    listaB.append(random.randint(-30,100))
    acumB = acumB + str(listaB[p]) + ' '
print("Lista B: ",acumB)

#c
listaC = []
acumC = ""
for q in range(0,m):
    listaC.append(-10 + 5*(q+1) - 0.05*(q+1)*(q+1))
    acumC = acumC + str(listaC[q]) + ' '
print("Lista C: ",acumC)

#d
with open("listas_ejercicio2.txt","w") as output_file:
    output_file.write("Lista A: " + acumA + '\n')
    output_file.write("Lista B: " + acumB + '\n')
    output_file.write("Lista C: " + acumC + '\n')

#e
with open("listas_ejercicio2.txt","r") as input_file:
    print("Contenido del archivo: \n")
    for line in input_file:
        print(line)
print("------------------------------------------------------------")

#f
vectorD = m*[None]
acumD = ""
for k in range(0,m):
    vectorD[k] = listaA[k] + listaB[k] + listaC[k]
    acumD = acumD + str(vectorD[k]) + ' '
print("El vector D es: ",acumD)

#g
with open("listas_ejercicio2.txt","a") as output_file:
    output_file.write("Vector D: " + acumD + '\n')
with open("listas_ejercicio2.txt","r") as input_file:
    print("Contenido del archivo junto al vector D: \n")
    for line in input_file:
        print(line)