#Notas
#V1: Se establecen la funcion que pregunta cuantas notas tiene una materia y se inicia el codigo donde se pregunta las materias que vera, el nombre y se guarda en una lista.


def notes():
    nt = int(input("Ingrese cuantas notas tiene esta materia: "))
    for i in range(nt):
        sb = (f"Ingrese de que es la nota numero {i+1}: ")




subject = int(input("Ingrese cuantas materias esta viendo: "))
subjects = []
for i in range (subject):
    sub = input(f"Ingrese su materia numero {i+1}: ")
    subjects.append(sub)

