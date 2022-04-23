myStr= "Hello World"
#cls para borrar
print("My name is "+ myStr)   #Concatenacion 
print(f"My name is{myStr}")   #Citar con F
print("My name is {0}".format{myStr})

#Nos enseña que podemos hacer con esos caracteres
print(dir(myStr))
#Convertir a Mayuscula
print(
   myStr.upper() 
)
#Convertir a minuscula
print(
    myStr.lower()
)
# Si esta en minuscula, lo cambia a mayuscula, si esta en mayuscula, en minuscula
print(
    myStr.swapcase()
)
#Pone en mayuscula la primer letra
print(
    myStr.capitalize()
)
#Reemplaza un texto por otro indicado
print(
    myStr.replace('Hello', 'Bye')
)
#Contar un tipo de caracter en un dato
print("La cantidad de letras L son: ",
    myStr.count('l')
)

#Me dice si un texto empieza o no empieza con determinado dato (Tira true o False)
print("Quiero saber si la frase empieza con Hello: ",
    myStr.startswith('Hello')
)
print("Quiero saber si la frase empieza con hello: ",
    myStr.startswith('hello')
)
print("Quiero saber si la frase empieza con He: ",
    myStr.startswith('He')
)

#Quiero saber con que palabra termina mi texto
print("Quiero saber si la frase termina con World: ",
    myStr.endswith('World')
)

#Separar el texto basado en los espaciones de la frase
print( "El texto separado por espacios quedaria asi ",
    myStr.split()
)
print( "El texto separado por coma quedaria asi ",
    myStr.split(',') #En este caso se debe agregar una coma, se puede genrar con otros caracteres tales "y", "0"
)

#Encontrar una letra en su posicion en la frase
print ( "La letra W, tiene la posicion:",
    myStr.find('W')
)

#Saber la longitud de una frase (Cuenta tambien los espacios en blanco)
print("la frase mide:",
   len (myStr)
)

#El valor del indice
print( "El valor del indice e es:",
    myStr.index ('e')
)

#Para saber si la frase es numero (true/False)
print(
    myStr.isnumeric()
)

#para saber si es alfanumerico
print(
    myStr.isalpha()
)

print("En la posicision 4 esta:",
    myStr[4]
)
