lista = [10, 20, 30, 40, 50]
suma = 0
x = 0

while x < len(lista):
    suma = suma + lista[x]
    x = x + 1

print("Los elementos de la lista")
print(lista)
print("La suma de sus elementos")
print(suma)

# Calculate and print the average
promedio = suma / len(lista)
print("El promedio de los elementos")
print(promedio)