#coleccion que no tiene indices
colours={'red', 'blue', 'yellow'}
print(colours)
print ("El color red esta en la lista?", 'red'in colours)
#agregar violet
colours.add('violet')
print(colours)
#Borrar red
colours.remove('red')
print(colours)
#borrar el set
colours.clear()  #tambien se podria haber puesto DEL COLOURS
print(colours)
