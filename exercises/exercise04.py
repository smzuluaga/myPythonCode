# Diseña una función en javascript que recibe una cadena de texto y retorna como resultado cuantas palabras que empiezan por la letra 'a' hay en ella. Puede asumir que el argumento recibido es siempre una cadena de texto con al menos un carácter y hasta 10000 caracteres.
# Ejemplo: Prueba1P8(“Anita Lava La Tina con agua y Jabón”)=2 // Prueba1P8(“a A bbb aA aa Ax az”)=6 

def a_counter(string):
    array = string.lower().split(' ')
    return len(list(filter(lambda x : x.startswith('a'),array)))


print (a_counter('Anita Lava La Tina con agua y Jabón'))
print (a_counter('a A bbb aA aa Ax az'))
print (a_counter('Axion, Arbol, perro, almibar, hnsd, jimena'))