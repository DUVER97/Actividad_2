ListaAlumnos=[]
continuar=True
while(continuar):
    nombre= input("Ingrese el nombre > ")
    apellido= input("Ingrese el apellido > ")
    edad= int(input("Ingrese la edad >"))
    ListaAlumnos.append([nombre,apellido,edad])

    print(ListaAlumnos)
    c=input("Desea Continuar S/N >")
    if(c=="n"):
        continuar=False
print(ListaAlumnos)