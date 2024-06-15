#Notas
#V1.1: Se agrega contador de posicioon de fila y columna, tambien se impelmenta una matriz



#Matriz donde van los datos de las materias
subjectt = [
           ]

#Posicion de fila
rowpo = 0 

#posicion de columna
colpo = 0

#Identificar las nostas que tiene una materia
def notes():
    nt = int(input("Ingrese cuantas notas tiene esta materia: "))
    for i in range(nt):
        sb = (f"Ingrese de que es la nota numero {i+1}: ")
        



#Inicio de codigo preguntando cuantas materias esta viendo
subject = int(input("Ingrese cuantas materias esta viendo: "))
for i in range (subject):
    sub = input(f"Ingrese su materia numero {i+1}: ")
    subjectt.append([sub])
    

print(subjectt)

