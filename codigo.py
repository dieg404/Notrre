#Notas
#V1.1: Se agrega contador de posicioon de fila y columna, tambien se impelmenta una matriz

#Matriz donde van los datos de las materias
subjectt = [
           ]

#Posicion de fila
rp = 0 

#posicion de columna
cp = 1

#contador de porcentaje
qstc = 0

#Identificar la cantidad de notas que tiene una materia, pregunta el porcentaje de la nota y agrega valor final de la nota a la lista
def notes():
    global rp, cp, qstc, qst, sb
    nt = int(input("Ingrese cuantas notas tiene esta materia: "))
    for i in range(nt):
        sb = float(input(f"Ingrese la nota numero {i+1}: "))
        qst = int(input("Ingrese el porcentaje de valor de la nota: "))
        qstc = qst + qstc
        if qstc <= 100:
            conditional()
        elif qstc > 100:
            print("La suma de los porcentajes de sus notas superal el 100%, intentelo nuevamente")
            break
        cp += 1

#Valida el porcentaje de la nota y se genera el nuevo resultado
def conditional():
    global qst, sb
    if qst == 10:
        sb = sb * 0.10
        subjectt[rp].insert(cp, sb)
    elif qst == 20:
        sb = sb * 0.20
        subjectt[rp].insert(cp, sb)
    elif qst == 30:
        sb =sb * 0.30
        subjectt[rp].insert(cp, sb)
    elif qst == 40:
        sb = sb * 0.40
        subjectt[rp].insert(cp, sb)
    elif qst == 50:
        sb = sb * 0.50
        subjectt[rp].insert(cp, sb)
    elif qst == 60:
        sb = sb * 0.60
        subjectt[rp].insert(cp, sb)
    elif qst == 70:
        sb = sb * 0.70
        subjectt[rp].insert(cp, sb)
    elif qst == 80:
        sb = sb * 0.80
        subjectt[rp].insert(cp, sb)
    elif qst == 90:
        sb = sb * 0.90
        subjectt[rp].insert(cp, sb)
    elif qst == 100:
        sb = sb * 0.100
        subjectt[rp].insert(cp, sb)
    else:
        print("Hay algo mal en condicional de notas, revisar")


#Inicio de codigo preguntando cuantas materias esta viendo
print("-" *30)
subject = int(input("Ingrese cuantas materias esta viendo: "))
for i in range (subject):
    print("-" *30)
    sub = input(f"Ingrese el nombre de su materia numero {i+1}: ")
    subjectt.append([sub])
    notes()
    rp += 1
    cp = 1
    qstc = 0
     

for i in subjectt:
    print(i)