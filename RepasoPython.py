#funcion input ()
'''
hola = input("Esbriba su nombre ")
print (f'Hola {hola}, Bienvenido') #Template String Forma 2
'''

#Truthy Falsy
""" print (bool(['a']))
print (bool([1]))
print (bool([0]))
print (bool([]))
print (bool(()))
print (bool({}))
print (bool((not True)))
print (bool((not False))) """

#funcion type()
# print(type(4.3))

#Template Strings Forma 1
""" nombre = 'Santiago'
apellido = 'Zuluaga'
print ('Hola {} {}, eres Bienvenido'.format (nombre,apellido))
 """
#Template String Forma 2
""" hola = input("Esbriba su nombre ")
print (f'Hola {hola}, Bienvenido')  """

#Tipos de datos
#Primitivos (inmutables)
""" 
    *String str()
    *Entero int()
    *Flotante float()
    *boleano bool()
""" 
#Otros 
"""
    *Listas list()
    *Tuplas tuple()
    *Diccionario dict() 
"""

#Prueba Casteo
""" num = 1
string = '3'

print (f'el numero {num} es de tipo =>> "{type(num)}" y se convierte a "{type(str(num))}" = {str(num)} \n y el numero {string} es de tipo =>> "{type(string)}" y se convierte a "{type(int(string))}" = {int(string)}') """

#Operadoreds aritméticos
# +, -, *, /, //, ** =>> PRECEDENCIA P-E-M-D-A-S <De izquierda a derecha > (Parentesis, Exponentes, Multiplicaciones, Divisiones, Adiciones, Sustracciones)
# '+'  operador de concatenacion
# '*'  repetidor de strings
# // Division que solo captura el entero
""" print (round(3/2))
print (round(5/3))
print (abs(3.3000000000000003-(1.1+2.2)))
print (format(3.000000000003, ".2"))
 """

#Operadores de comparacion
""" < - Menor que
<= - Menor o Igual que
> - Mayor que 
>= - Mayor o Igual que
== - Igual que
!= - Diferente 
 """
#Operadores Lógicos
""" and / or / not  """ 

#CONDICIONALES -If
""" 
if True:
    print(True)
elif:
    print('condition')
else:
    print(False) 
"""

#METODOS DE STRINGS

string = "hola como estas, este es un texto para probar COMO los METODOS DE LOS STRINGS hola"
array = string.split(" ")
number = '2548'
""" 
print ('como' in array)
print ('hola' in string) - operador 'in', para verificar si existe un caracter o cadena de caracteres dentro de otra o dentro de una lista
print(len(string)) - conocer la longitud de una cadena, lista, diccionario o tupla
print(string.upper()) - convertir el string a mayuscula
print(string.lower()) - convertir el string a minuscula
print(string.lower().count('como')) - contar cuantas veces está un caracter o cadena de caracter dentro de una cadena o lista
print(string.count('como'))
print(string.count('a'))
print(array.count('hola'))
print(string.swapcase()) - cambia las mayusculas por minusculas y viceversa, dentro del string
print(string.endswith('S')) - validar si una cadena finaliza con un caracter o cadena de caracteres, devuelve un valor booleano.
print(string.startswith('hola'))  - validar si una cadena inicia con un caracter o cadena de caracteres, devuelve un valor booleano.
print(string.replace('a', '*',3)) - str.replace(arg1, arg2, arg3) // reemplaza los valores del argumento 1, por los valores indicados en el argumento 2. El argumento 3 es opcional, sin embargo, con este se puede indicar cuantas veces queremos hacer dicho reemplazo, si no se indica este argumento, por default el sistema reemplaza todas las coincidencias del argumento 1.
print(string.capitalize()) - convierte la primera letra del string en mayuscula.
print(string.title()) - convierte la primera letra de cada palabra del string en mayuscula, ejm para nombres propios.
print(string.isdigit()) - permite validar si un caracter es un digito, devuelve un booleano True para valores entre 0-9 y/o sus combinaciones.
print(number.isdigit()) -ESTO ES UN ERROR, es un método solo para strings
print('*****'*5)
print(string) 
"""

#Indexing
#las strings, listas, tuplas y diccionarios tienen acceso a cada uno de sus componentes a través de indexing, es decir, el numero de indices.
""" 
print(array[1])
print(string[-2])
"""

#Slicing
#permite sacar porciones de una cadena de strings, lista, tuplas o diccionarios, a partir de un par de índices [PI:PF:S] donde PI -> PosicionInicial / PF -> Posicion Final / S-> Saltos, es decir, cada cuantos indices debe retornar, si el valor es 1, ira caracter por caracter, si es 2, devuelve cada 2 caracteres, y así sucesivamente
""" 
print(string[5:9])
print(string[:5])
print(string[5:])
print(string[5::2])
print(array[-4:-2])
"""
#METODOS PARA MANEJO DE NUMEROS

#Enumerate - convierte a un numero en iterable y devuelve una lista de tuplas, separando el numero entregado en digitos y si indice  => (1,2) => 1. indice / 2. digito del numero. para pasar un numero como parametro, debemos convertirlo a string para que sea iterable
number = 8948758
""" print (list(enumerate(str(number)))) """
#   output => [(0, '8'), (1, '9'), (2, '4'), (3, '8'), (4, '7'), (5, '5'), (6, '8')]

#LISTAS (Mutables) - permite almacenar diferentes tipos de datos en una sola estructura de datos.
decimal_numbers =[0,1,2,3,4,5,6,7,8,9]
dif_data = ['hola', True, 2, 3.4,('a','b'), {'pais': 'Colombia'}, [1,2,3,4,5]]
desordered_num = [20,45,2,3,8,4,9,15]

#Operador x in list
""" 
print (3 in decimal_numbers)
print (5 in dif_data)
"""

#METODOS DE LAS LISTAS // C-R-U-D -> Create - Read - Update - Delete

#Append - (Create) - agrega un elemento en la ultima posición de la lista

decimal_numbers.append(10)
""" print (decimal_numbers) """
    #output -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Insert - (Create)
decimal_numbers.insert(3,'10') # list.insert(arg1,arg2) -> Argumento1 = indice donde se desea hacer la inserción / Argumento2 = valor a insertar
""" print (decimal_numbers) """
    #output -> [0, 1, 2, '10', 3, 4, 5, 6, 7, 8, 9, 10] 


#Contatenar 2 listas o mas con el operador de concatenación '+'
""" print (decimal_numbers + dif_data) """


#Index - (Read) - permite conocer el indice en que se encuentra un elemento pasado por prámetro.
""" print(decimal_numbers.index(3)) """
 #output -> 3


#Remove - (Delete) - permite remover un elemento de la lista apartir de su valor.
dif_data.remove(('a','b'))
dif_data.remove(('hola'))
""" print(dif_data) """
    #output ->  ['hola', True, 2, 3.4, {'pais': 'Colombia'}, [1, 2, 3, 4, 5]]
    #output -> [True, 2, 3.4, {'pais': 'Colombia'}, [1, 2, 3, 4, 5]]


#Pop - (Delete) - permite eliminar un elemento de una lista apartir de su indice, si no se le pasa un argumento como parámetro, el valor a eliminar será el último
dif_data.pop()
""" print(dif_data) """
    #output -> [True, 2, 3.4, {'pais': 'Colombia'}]

dif_data.pop(0)
""" print(dif_data) """
    #output -> [2, 3.4, {'pais': 'Colombia'}]


#Reverse - (Update) - cambia el orden de la lista, de atrás hacia adelante
decimal_numbers.reverse()
""" print (decimal_numbers) """
    #output -> [10, 9, 8, 7, 6, 5, 4, 3, '10', 2, 1, 0] 
#otra forma de hacer reverso a las palabras es usar la sintaxys de slicing y en el tercer argumento que indica los saltos, se pone el numero -1
#Ejem =
string = 'hola'
""" print (string[::-1]) """
    #output -> 'aloh'
#Ejemplo2=
array = ['hey', 'fellow', 'warriors']
""" print ([x[::-1] for x in array]) """

#Sort - (Update) - ordena la lista - si se tienen diferentes tipos de datos en la lista, no se puede usar esta opcion
desordered_num.sort()
""" print (desordered_num) """

#TUPLAS (Inmutables) - son estructuras de datos similares a las listas pero no pueden ser mutadas. tambien pueden almacenar diferentes tipos de datos, usualmente se usa como atributos o para consultas.
tuple1 = (1,2,3,4,5,6,7,1,2,3,4,5,6)
dif_data_tuple = ('hola', True, 2, 3.4,('a','b'), {'pais': 'Colombia'}, [1,2,3,4,5])

#METODOS DE TUPLAS

#Index - (Read) - permite conocer el indice en que se encuentra un elemento pasado por prámetro.
""" print(tuple1.index(3)) """
 #output -> 3

#Count (Read) - permite contar cuantas veces existe un caracter o cadena de caracteres pasado por parámetro, dentro de la tupla
""" print(tuple1.count(7)) """
    #output -> 1

#Convertir Listas a Tuplas / Tuplas a Listas
""" print(list(tuple1)) """ # Tupla a Lista
""" print(tuple(decimal_numbers)) """ # Lista a  Tupla

#ALETOREIDAD - se debe importar la librería random.
import random

#ejemplo
options = ('piedra', 'papel', 'tijera')

choice = random.choice(options) #Elige una opción al azar de una lista o tupla, de un set no se puede hacer esto.
""" print(choice) """
    #output -> papel // #output -> piedra // #output -> tijera

azar = random.randint(1,10) #Retorna un numero entero al azar entre un rango dado, en este caso entre 1 y 9, ya que 10 es el limite, pero no se incluye
""" print(azar) """
    #output -> 8 // #output -> 1 // #output -> 0


#DICCIONARIOS (Mutables) - estructura de datos que se compone de clave:valor, no permite ingresar claves repetidas, lo que hará será actualizar el valor si hay una entrada de una clave que ya existe

dictionary = {'name' : 'Camilo',
              'last_name': 'Perez',
              'age': 28,
              'nationality': 'colombian',
              'langs' : ['EN', 'ES', 'FR']}


#METODOS DICCIONARIOS

#(Read) len() - permite conocer la longitud (cantidad de elementos) de un diccionario, lista, tupla, set, string
""" print(len(dictionary)) """
    #output -> 4

#(Read) Acceder añ valor de una clave
#Forma 1 - bracket notation
""" print(dictionary['langs']) """ #de esta forma, si buscamos una clave que no existe, el sistema arroja un KeyError y suspendela ejecución del sistema.
    #output -> ['EN', 'ES', 'FR']

#Forma 2 - .get('clave')
""" print(dictionary.get('langs')) """ #de esta forma, si buscamos una clave que no existe, el sistema arroja 'None.
    #output -> ['EN', 'ES', 'FR']

#(Update)Cambiar valor de una propiedad a partir de su clave:
dictionary['age']=30
""" print(dictionary) """
    #output -> {'name': 'Camilo', 'last_name': 'Perez', 'age': 30, 'nationality': 'colombian'}

#(Create) Agregar nuevas propiedades al diccionario.
dictionary['email'] = 'camipe@gmail.com'
""" print(dictionary) """
    #output -> {'name': 'Camilo', 'last_name': 'Perez', 'age': 30, 'nationality': 'colombian', 'langs': ['EN', 'ES', 'FR'], 'email': 'camipe@gmail.com'}

#(Create-Update) Agregar nuevas propiedades a un elemento del diccionario, en este caso al elemento langs que es una lista de las lenguas que habla
dictionary['langs'].append('PT')
""" print(dictionary) """
    #output -> {'name': 'Camilo', 'last_name': 'Perez', 'age': 30, 'nationality': 'colombian', 'langs': ['EN', 'ES', 'FR'], 'email': 'camipe@gmail.com'}

#(Delete) - Eliminar una clave
#Forma 1 - con palabra reservada 'del'
"""
del dictionary['langs']
 print(dictionary) 
"""
    #output -> {'name': 'Camilo', 'last_name': 'Perez', 'age': 30, 'nationality': 'colombian', 'email': 'camipe@gmail.com'}

#Forma 2 - con método pop() - en este contexto siempre debe llevar un argumento que debe ser el nombre de la clave a eliminar, no recibe como parámetro un número de índice
"""
dictionary.pop('langs') 
print(dictionary)
"""
    #output -> {'name': 'Camilo', 'last_name': 'Perez', 'age': 30, 'nationality': 'colombian', 'email': 'camipe@gmail.com'}


#Items - Devuelve en forma de lista de tuplas, las clave y valor de cada elemento.
""" print(dictionary.items()) """
    #output -> dict_items([('name', 'Camilo'), ('last_name', 'Perez'), ('age', 30), ('nationality', 'colombian'), ('langs', ['EN', 'ES', 'FR', 'PT']), ('email', 'camipe@gmail.com')])

#Keys - Devuelve en forma de lista, unicamente las claves que tiene el diccionario.
""" print(dictionary.keys()) """
    #output -> dict_keys(['name', 'last_name', 'age', 'nationality', 'langs', 'email'])

#Values - Devuelve en forma de lista, unicamente los valores que tiene el diccionario.
""" print(dictionary.values()) """
    #output -> dict_values(['Camilo', 'Perez', 30, 'colombian', ['EN', 'ES', 'FR', 'PT'], 'camipe@gmail.com'])


#CICLOS

#WHILE
#Ejemplo 1
""" 
counter = 0
while counter < 10:
    counter += 1
    print (counter)
    if counter == 5:
        break #Palabra reservada para interrumpir forzosamente un ciclo
    #output -> 1
    #          2
    #          3
    #          4
    #          5     
"""

#Ejemplo 2
""" 
counter = 0
while counter < 10:
    counter += 1
    if counter < 5:
        continue #Palabra reservada para saltar iteraciones en un ciclo si una condicion se cumple o no y saltar a la siguiente iteracion
    print (counter) 
    #output -> 5
    #          6
    #          7
    #          8
    #          9
    #          10  
"""
#FOR - Se Puede iterar rangos, strings o estructuras de datos como tuplas, listas, conjuntos
string_ciclos = "esta estring es para probar ciclos"
array_ciclos = string_ciclos.split(" ")
tuplas_ciclos = tuple(array_ciclos)

#Rangos
for element in range(20): #Si solo se le da un argumento, el rango irá desde 1 hasta el numero indicado -1, puesto que el 20 es limite pero no se incluye.
    """ print (element) """
    #output -> 1 / 2 /3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 / 16 / 17 / 18 / 19

for element in range(5,20): #si se le pasan dos argumentos, se entiende que el primero es el rango desde donde empieza a iterar y el segundo hasta donde itera.
    """ print (element) """
    #output -> 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 / 16 / 17 / 18 / 19

#Strings - recorre un string y le podemos decir que queremos que haga con cada caracter
for char in string_ciclos:
    """ print(char*2) """

#Listas y tuplas
for element in array_ciclos:
    """ print (element) """

for element in tuplas_ciclos:
    """ print (element) """

#Diccionarios
for element in dictionary:
    """ print (element) #Retorna las claves del diccionario.
    print (dictionary[element]) #Retorna los values de las claves del diccionario """

for key, value in dictionary.items():
    """ print (f'key => {key} : "{value}"') """

prices = {
    'tv': '200',
    'cel' : '400',
    'lavadora' : '1000'
}
suma = 0
for value in prices.values():
    suma += int(value)
""" print (f'La suma es => {suma}') """

#SET (CONJUNTOS) (Mutable) 
# Propiedades:
#   *Se puede modificar
#   *no tiene un orden específico
#   *Puede contener diferentes tipos de datos
#   *NO PERMITE ELEMENTOS DUPLICADOS, si por error hay elementos duplicados,a l retornarlo, retorna valores únicos

sets = {1,2,3,4,5,61,1,4} 
""" print(sets) """
    #output -> {1, 2, 3, 4, 5, 61

#Se puede convertir un string, uuna tupla y una lista a set
""" print (set("Hola")) """
    #output -> {'H', 'a', 'l', 'o'}

""" print (list(set([4,5,8,6,9,4,2,5,8,1])))""" #este es el caso de una lista que se transforma a set para que queden los valores unicos y se imprime como valor de lista 
    #output -> [1, 2, 4, 5, 6, 8, 9]

""" print (set((4,5,8,6,9,4,2,5,8,1))) """
    #output -> {1, 2, 4, 5, 6, 8, 9}

#METODOS DE SET

#(Read) len() - permite conocer la longitud (cantidad de elementos) de un set, lista, tupla, dicconario, string
""" print(len(sets)) """
    #output -> 6

#(Read) Funcion 'in' - retorna un boleano indicando si un valor se encuentra en el conjunto
""" print (4 in sets) """
    #output -> True

#(Create) Add() - adiciona un elemento pasado por parámetro al set indicado
sets.add(40)
""" print (sets) """
    #output -> {1, 2, 3, 4, 5, 40, 61}

#(Update) Update() - permite agregar elementos al set por bloques de varios elementos. algo así como intertar un subconjunto en ese set existente
sets.update({1,4,80,9,60})
""" print (sets) """

#(Delete) Remove() - eliminar elementos de un conjunto, a partir de un valor. si se intenta eliminar un elemento que no existe, arroja error e interrumpe la ejecucion
sets.remove(80)
""" print (sets) """

#(Delete) Discard () - eliminar elementos de un conjunto, a partir de un valor. si el valor a eliminar no existe, no retorna nada, pero tampoco un error, ni interrumpe la ejecicion del programa.
sets.discard(100)
""" print (sets) """

#(Delete) Clear() - elimina todos los elementos del conjunto.
sets.clear()
""" print (sets)
print (len(sets)) """

#OPERACIONES CON CONJUNTOS
seta = {'col', 'mex', 'bol', 'bra'}
setb = {'mex', 'pe', 'col'}

#Union - retorna la union de ambos conjuntos
setc = seta.union(setb) #Forma con método
""" print(setc) """
    #output -> {'bra', 'bol', 'col', 'mex', 'pe'}
setc = seta | setb #Forma con operador matemático
""" print(setc) """
    #output -> {'bra', 'bol', 'col', 'mex', 'pe'}

#Interseccion - returna los elementos en común entre ambos elementos
setc = seta.intersection(setb) #Forma con método
""" print(setc) """
    #output -> {'mex', 'col'}
setc = seta & setb #Forma con operador matemático
""" print(setc) """
    #output -> {'mex', 'col'}

#Diferencia - retorna los elementos del conjunto a, quitando los que tiene en comun con el conjunto b
setc = seta.difference(setb) #Forma con método
""" print(setc) """
    #output -> {'bra', 'bol'}
setc = seta - setb #Forma con operador matemático
""" print(setc) """
    #output -> {'bra', 'bol'}
setc = setb - seta #Forma con operador matemático
""" print(setc) """
    #output -> {'pe'}

#Diferencia Simetrica - retorna la union de los conjuntos, quitando  los elementos que ambos tienen en comun
setc = seta.symmetric_difference(setb) #Forma con método
""" print(setc) """
    #output -> {'bra', 'bol', 'pe'}
setc = seta ^ setb #Forma con operador matemático
""" print(setc) """
    #output -> {'bra', 'bol', 'pe'}




#LIST COMPREHENSIONS - genera una lista con un ciclo for a partir de un iterable

#[element for element in iterable if condition]
# ______      _______    ________    _________
#    1           2          3             4
# 1. Accion que que queremos ejecutar sobre cada elemento del punto 2 para que su retorno quede en la lista 
# 2. Elemento del iterable sobre el que se va a aplicar la accion indicada en el punto 1 para que quede en la lista.
# 3. Iterable, elemento que va a iterar para ejecutar la accion de la parte 1. #PUEDE SER UN RANGO, UNA LISTA, UN DICCIONARIO, UNA TUPLA, UN ITERABLE
# 4. Condicion, es opcional, se puede determinar para que la accion de la parte 1 quede guardada en lista, segun se cumpla o no una condicion.

numbers = [element*2 for element in range(1,10)]
""" print(numbers) """
    #output -> [2, 4, 6, 8, 10, 12, 14, 16, 18]

numbers2 = [element * 2 for element in range(1,11) if element % 2 == 0]
""" print(numbers2) """
    #output -> [4, 8, 12, 16, 20]




#DICTIONARY COMPREHENSIONS - genera un diccionario con un ciclo for a partir de un iterable

#[key:value for element in iterable if condition]
# _________     _______    ________    _________
#    1             2          3             4
# 1. Accion que que queremos ejecutar sobre cada elemento del punto 2 para que su retorno quede en el diccionario 
# 2. Elemento del iterable sobre el que se va a aplicar la accion indicada en el punto 1 para que quede en la lista.
# 3. Iterable, elemento que va a iterar para ejecutar la accion de la parte 1. #PUEDE SER UN RANGO, UNA LISTA, UN DICCIONARIO, UNA TUPLA, UN ITERABLE
# 4. Condicion, es opcional, se puede determinar para que la accion de la parte 1 quede guardada el diccionario, segun se cumpla o no una condicion.

#Ejemplo1
dict_num = {i : i*2 for i in range(1,10)}
""" print(dict_num) """
    #output -> {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

import random
south_ame =['col', 'bol', 'bra', 'pe']
countries = ['col', 'mex', 'bol', 'bra', 'pe', 'usa','can']

#Ejemplo2
dict_population = {element: random.randint(1,1000)  for element in countries if (not element in south_ame)}
""" print(dict_population) """
    #output -> {'mex': 325, 'usa': 573, 'can': 586}

#Ejemplo3
dict_population = {element: random.randint(1,1000)  for element in countries if element in south_ame}
""" print(dict_population) """
    #output -> {'col': 478, 'bol': 317, 'bra': 164, 'pe': 188}

#Ejemplo4
text = 'Hola, soy nicolas'
unique = {c:c.upper() for c in text if c in 'aeiou'}
""" print(unique) """
    #output -> {'o': 'O', 'a': 'A', 'i': 'I'}

#FUNCION ZIP - permite unir dos listaS en forma de tuplas, se le puede dar formato de lista de tuplas con la funcion constructora de list()

names = ['Santi', 'Zule', 'Pedro']
ages = [28,22,45]
dates = list(zip(ages, names))
"""print(dates)"""
    #output -> [(28, 'Santi'), (22, 'Zule'), (45, 'Pedro')]

#combinar dicrionary comprehensions con zip
dict_dates = {name: age for (name,age) in zip (names, ages)}
""" print (dict_dates) """
    #output -> {'Santi': 28, 'Zule': 22, 'Pedro': 45}

dict_dates = {name: age for (name,age) in zip (names, ages) if age>25}
""" print (dict_dates) """
    #output -> {'Santi': 28, 'Pedro': 45}

#DIFERENCIAS ENTRE TUPLA, LISTA CONJUNTOS

#ESTRUCTURA    MUTABLE    ORDENADA   INDEXING/SLICING    DUPLICAR ELEMENTOS
# LIST          True        True            True                True
# TUPLE         False       True            True                True
# SET           True        False           False               False

#sets - funciones PENDIENTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE





# GESTOR DE PAQUETES DE PYTHON - Permite acceder a librerías y frameworks que podemos usar para nuestros proyectos para solucionar ciertos problems en específico.
# https://pypi.org/ -  SITIO WEB PARA VISUALIZAR LIBRERÍAS Y SUS DOCUMENTACIONES, VERSIONES, ETC

# DIRERENCIA ENTRE MODULO, PAQUETE, LIBRERIA, FRAMWORK Y DEPENDENCIA
#   *Módulo. La pieza más pequeña de software. Puede ser un conjunto de métodos o funciones para usarlo.
#   *Paquete. Colección de módulos.
#   *Librería. Colección de paquetes.
#   *Framework. Conjunto de librerías. No solo ofrecen funcionalidades, sino que también arquitectura. Uno no incluye un framework, uno incluye código dentro de un framework.
#   *Dependencia. Se refiere a cuán interconectados están los módulos. O sea, que tu software depende de módulos para funcionar.

# DESCARGAR WSL PARA USAR LAS FUNCIONALIDADES DE PIP
# 1. Ir a powershell y digitar:
#               'wsl --install
# 2. Esperar que descargue y reiniciar el pc.
# 3. Configurar ubuntu asignando usuario y clave:  }
#       User: smzuluaga1
#       Password: Zuluaga1
# 4. INSTALAR GESTOR DE PAQUETES PIP, con el comando:
#               'sudo apt install -y python3-pip'
# 5. INSTALAR LAS SIGUIENTES HERRAMIENTAS, con el comando:
#               'sudo apt install -y build-esential libssl-dev libffi-dev python3-dev '

# CÓMO USAR PIP
# Ir a la terminal (basada en linux), ubicarse en el directorio dondeva a descargar al librería y usar el comando:
#                'pip3 install numpy'
#                 ____________ _____
#                     1          2     => 1. Comando para Instalar / 2. Nombre de la librería que vamos a usar. 

# Una librería puede basarse de otras librerías para usarse, por ende, cuando se descarga una librería en específico, es normal que se descarguen otras librerías y cuando esto pasa, la terminal nos muestra las dependencias adicionales que la librería está descargando,

# Con este comando podemos ver el arbold e librerías que estamos usando en el entorno  general de Python en el PC, no se visualiza por proyecto.
#                 'pip3 freeze'
# 
# 
# AMBIENTES VIRTUALES EN PYTHON - 
# Cuando instalamos librerías y módulos, se instalaron de forma general para todos los proyectos ejecutados en el pc donde estamos descargando la librería. Esto hace que si se está trabajando en varios proyectos en el mismo pc, esta característica de generalidad de las librerías puede generar choques, puesto que un proyecto puede necesitar una version específica de x librería y otro proyecto puede necesitar una versión específica de la misma libreía.
# Como solucion a este problema,  LOS AMBIENTES VIRTUALES encapsulan la descarga de modulos y librerías a un proyecto específico para que cada proyecto tenga sus propias librerías y no colisione con otro proyecto cuando ambos necesitan versiones diferentes de la misma librería,

#COMO USAR AMBIENTES VIRTUALES-
# 1. Validar dónde se está corriendo python  y pip con el comando:
#                  'which python3'
#                  'which pip3' 
# 2. Para windos con WSL y Linux, se debe instalar el siguiente paquete desde terminal:
#                  'apt install -y python3-venv'
# 3. Ir a la carpeta donde queremos crear el ambiente virtual y ejecutamos el comando:
#                  'python3 -m venv env
#                   ______________  ___
#                          1         2    = 1. Comando para crear entorno virtual // 2. nombre que le queremos dar al entorno virtual
# 4. Activar el ambiente virtual con el comando:
#                   'source env/bin/activate
# Para salir del ambiente virtual, usamos el comando:
#                   'deactivate'
# cuando se correo 'pip3 freeze' desde el ambiente virtual, no saldrá nada a menos que ya hayamos descargado paquetes y librerias.

# REQUIREMENTS.TXT - es un archivo que se crea para gestionar todas las dependencias y modulos que usa un proyecto, es una automatizacion de ese importe de dependencias.
# Para esto se puede captar todos los requerimientos de un aplicativo y exportarlo a un txt, de la siguiiente forma:
#                    'pip3 freeze > requirements.txt
# Para descarar esos requerimientos del aplicativo en otro pc, nos situamos en ese pc y ejecutamos el comando:
#                    'pip3 install -r requirements.txt'


#DEPENDENCIA REQUESTS -nos permite hacer peticiones a otros sitios web
#                   'pip3 install requests'
#

#DEPENDENCIA PANDAS - sirve para anlizar y manipular archivos duros como .csv
# #                   'pip3 install pandas'

#PYTHON PARA BACKEND - LIBRERÍA FAST API y UVICORN
#                   'pip3 install fastapi'
#                   'pip3 install "uvicorn[standard]"'

#DOCKER - Herramienta que sirve para aislar entornos de ejecucion y versiones de python, para que cuando subimos proyectos a la nube, no generen choque si esta programado con diferentes versiones de python, esto lo hace con una tecnología de contenedores.

#MODULOS CHEVERES - IMPORTAR 

# string
import string
# método string.capwords(string, sep = None)  => permite poner en mayuscula cada palabra de un string, hace las veces dejuntar un split(' '), capitalize() en cada palabra iterada y luego un ' '.join
#       ______________  ______  __________
#             1           2         3        => 1. metodo capwords de la librería string // 2. string que vamos a aplicar el método // 3. indicador del separador que queremos que tome para hacer el split(), si no s epone el segundo argumento o se pone sep= None, el sistema por defecto lo toma como espacio en blanco.
# Example = 
sentence = 'Python-is one of the best programming languages.'
formatted = string.capwords(sentence, sep = None)
""" print (formatted) """
#       output =>  'Python-is One Of The Best Programming Languages.'

# collections
import collections
# método Counter collections.Counter(x) - retorna un diccionario con par clave: valor. la clave será cada elemento del string(caracter) o de la lista(elemento) y el valor será la cantidad de coincidencias de dicho elemento dentro del string o lista
#              _________________ _ 
#                      1         2  =>  1. método Counter de la librería collections // 2. string, o array que queremos poner como parametro para contar.
# Example =
array = [0,2,4,0,2,4,6,8,10]
""" print(collections.Counter(array)) """

# random
# método random
# método choise
