#3==3 ¿3 es igual a 3? Doble signo de igual

color= "blue"

if color == "red":
    print ("el color es rojo")
elif color=="blue":
    print(" el color es azul")
else:
    print("No hay color registrado")

#otro ejemplo
nombre="Florencia"
apellido="Monje"

if nombre== "Florencia":
    if apellido=="Monje":
        print ("Sos Florencia Monje")
    else:
        print ("No sos Florencia Monje")

else:
    print ("No sos Florencia Monje")

#otro ejemplo AND OR NOT
x=10
y=5
if x>2 and x<=10:
    print ("x es mayor a 2 y menor a 10")
if x>2 and x<=20:
    print ("x es mayor a 2 y menor a 20")
if (not (x==y)):
    print ("x no es igual a Y")

