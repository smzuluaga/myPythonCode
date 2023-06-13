# Diseñe e implemente una función en javascript que reciba un arreglo de números enteros y retorne el arreglo ordenado de la siguiente manera: Primero los números positivos ordenados de mayor a menor y luego los números no positivos ordenados de mayor a menor. Puede asumir que todos los números en el arreglo recibido por la función serán enteros en el intervalo [-1000,1000]
#Ejemplo: Prueba1P6([-1,2,3,4,-2,4,0)])=[4,3,2,0,-1,-2] // Prueba1P6([10,2,3,4,-2,4,0)])=[10,4,3,2,0,-2]

def ordered_numbers (array):
    array.sort()
    array.reverse()
    return array


print(ordered_numbers([-1,2,3,4,-2,4,0]))
print(ordered_numbers([10,4,3,2,0,-2]))
