# Programa para verificar si un numero es negativo o positivo

# input

x= int(input("Digite el valor de x: "))

# processing

if x > 0:
    rta= "Positivo"
elif x == 0:
    rta= "Neutro"
else:
    rta= "Negativo"

# output
    
print("El numero " + str(x) + " es " + rta)