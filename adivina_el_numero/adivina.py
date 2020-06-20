import random  

intentos = 0
numeromin = 1
numeromax = 20

print("hola! cual es tu nombre?: ")
usuario = input()

numero = random.randint (numeromin, numeromax)
print("Bien, " + usuario + '. debes adivinar un numero entre ' + str (numeromin) + ' y ' + str(numeromax))

while intentos < 6:
    print("ingresa un numero: ")
    intento = input()
    intento = int (intento)

    intentos = intentos + 1
    if intento < numero:
        print("Tu numero esta por debajo")
    if intento > numero:
        print("Tu numero esta por encima")
    if intento == numero:
        break


if intento == numero:
    intentos = str(intentos)
    print("buen trabajo " + usuario + ' adivinaste mi numero en ' + intentos + ' intentos')
if intento != numero:
    numero = str(numero)
    print ("no el numero que estaba pensando era " + numero)