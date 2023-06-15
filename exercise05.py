# Diseña un script en javascript que imprima los primeros 10 formas siguiendo el siguiente patrón (Se muestran sólo las primeras 2). Tener en cuenta que el valor del argumento será un entero y estará siempre en el intervalo [0,9]. No usar switch ni una secuencia de condicionales para cada caso. Debe usar creativamente las otras herramientas del lenguaje como ciclos, arreglos y cadenas.
#Ejemplos: Prueba1P1(0)=["123","804","765"] // Prueba1P1(1)=["234","915","876"]

def number_pattern(n):
    array = []
    pattern = []
    
    while len(array) < 10:
        if n > 9:
            n = 0
        array.append(n)
        n+=1 
    
    pattern.append(f'{array[1]}{array[2]}{array[3]}')
    pattern.append(f'{array[8]}{array[0]}{array[4]}')
    pattern.append(f'{array[7]}{array[6]}{array[5]}')
    return pattern

#Pruebas en consola  
print(number_pattern(0))
print(number_pattern(1))
print(number_pattern(2))
print(number_pattern(3))
print(number_pattern(4))
print(number_pattern(5))
print(number_pattern(6))
print(number_pattern(7))
print(number_pattern(8))    
print(number_pattern(9))