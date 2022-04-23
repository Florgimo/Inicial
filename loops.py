#para listar una lista de elementos (Bucle)
comida= ['banana', 'naranja', 'uva', 'papa']

for elementos in comida:
    print (elementos)

#Cuando llega a determinado elemento da un mensaje
for elementos in comida:
    if elementos == "naranja":
        print ("tenes que comprar un kl de ...")
    print (elementos)

#Cuando llega a determinada validacion, deja de ejecutar
for elementos in comida:
    if elementos == "naranja":
        break
    print (elementos)
#Cuando llega a determinada validacion, salta el elemento y continua con lo siguiente
for elementos in comida:
    if elementos == "naranja":
        continue
    print (elementos)

#Dar una enumeracion hasta el numero anterior a
for number in range (1,8):
    print (number)

#Deletrear una palabra
for letter in "hello":
    print (letter)

#Mostrar un contador con una condicional
count=4
while count <=10:
    print (count)
    count= count +1