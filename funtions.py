#las mas comunes
#print()
#dir()
#type()

#definicion de funcion DEF
def hello (name= "person"):
    print ("hello " + name)

hello ("joe")
hello ( "ryan")
hello ("fazt")

#otro ejercicio
def add(n1, n2):
    return n1+n2
print ( add (10,30))
print ( add (300,10))

#Otra forma
add= lambda n1, n2: n1+n2
print ( add (10,30))
print ( add (300,10))

#Saber la cantidad de caracteres de una palabra
print (len("hello"))

