# Diseña una función en javascript que reciba como parámetro un número entero positivo y retorna el número de la secuencia de fibonacci que es estrictamente menor que él. Recuerda que la sucesión de fibonacci es la secuencia de números donde cada término es la suma de los dos anteriores y empieza con los números 0 y 1. La secuencia es 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...Todas las pruebas serán con números menores o iguales a 10000. Puede asumir que todos los números con los que será probada la función están en el intervalo [0,10000]
# Ejemplos Prueba1P2(10) = 8 // Prueba1P2(55) = 34

def fibonacci (n):
    num1 = 0
    num2 = 1
    sum = 0

    while True:
        sum = num1 + num2
        num1 = num2
        num2 = sum

        if sum > n:
            break
    return num1

#Pruebas en consola
print(fibonacci(4))
print(fibonacci(10))
print(fibonacci(34))
    
    


