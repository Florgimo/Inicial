demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colours = ['red','green', 'blue']

#Creacion de tupla para que entre todo en una misma lista
numbers_list= list ((1, 2, 3, 4))
print ("El tipo de lista es", type(numbers_list))
print (numbers_list)

#Creacion de rango de lista
#Te devuelve un numero antes de el numero mas grande, es este caso 10
#r= list ("La lista es", range (1,10))
#print (r)

#Que puedo hacer con la lista? Operaciones
#Imprimir la lista colores
print (colours)
print(dir(colours))
#print (type(colours))
#Cambiar el color green por el color yellow
colours [1]= 'yellow'
print (colours)
#Agregar un color en determinada posicion
colours.insert(2, 'pink')
#agregar un nuevo elemento a una lista
colours.append ('violet')
print (colours) 
#Agregar dos nuevos elementos con una tupla pero que lo tomen como elementos separados
colours.extend(['yellow','black'])
print (colours)
#insertar colores a lo ultimo con el largo que tiene
colours.insert(len(colours), 'white')
print (colours)
#ordenarlos alfabeticamente
colours.sort()
print(colours)
#Ordenarlos alfabeticamente de forma inversa
colours.sort(reverse=True)
print(colours)
#imprimir el indice del color red
print("el indice del color es:", colours.index('yellow'))
#quitar el ultimo color dado
colours.pop()
print (colours)
#quitar dos ultimos elementos, si quiero remover determinado elemento agrego el numero de la posicion en el parentesis
colours.pop()
colours.pop()
print (colours)
#Cuando solo queres quietar un unico color en especifico
colours.remove('red')
print(colours)
#Para eliminar todos los elementos de la lista
colours.clear ()
#cuantos elementos tengo en colours
#print (len (colours))

#print(len (demo_list))

#Dar el segundo elemento de colours (Si quiero el primero es el 0)
print (colours[1])
#Dar el valor de verdadero o falso si green esta en la lista de colours
print ('green' in colours)
print ('Violeta' in colours)

#VI HASTA 1:53:54
