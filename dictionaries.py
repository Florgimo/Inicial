#ejemplo de datos de un producto con llaves
producto={
    "name":"book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "first_name": "ryan",
    "last name": "ray"
}
#Ver tipo de datos
print (type(producto))
#Que acciones puedo realizar
print (dir(producto))
#obtener los valores de las llaves (tipos)
print(person.keys())
print (producto.keys())
#obtener los item y su valor
print(person.items())
print (producto.items())

#mas elementos dentro de un mismo diccionario
product= [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 10000}
]
print(product)