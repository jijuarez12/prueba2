with open("listas_ejercicio2.txt","r") as input_file:
    todoLista = input_file.readlines()
    linea2 = todoLista[1].split()
    listaB_new = linea2[2:]
    acum_lista = []
    i = 0
    while i<len(listaB_new):
        if float(listaB_new[i])>=0.0 :
            acum_lista.append(listaB_new.pop(i))
            i = i - 1
            a = len(listaB_new)
        i = i + 1
    listaB_new = listaB_new + acum_lista
    acumB_new = ""
    for p in range(0,len(listaB_new)):
        acumB_new = acumB_new + str(listaB_new[p]) + " "
todoLista[1] = str(linea2[0]) + " " + str(linea2[1]) + " " + acumB_new + '\n'
with open("listas_ejercicio2.txt","w") as output_file:
    for linea in todoLista:
        output_file.write(linea)
with open("listas_ejercicio2.txt","r") as input_file:
    print("Contenido del archivo modificado: ")
    for line in input_file:
        print(line)