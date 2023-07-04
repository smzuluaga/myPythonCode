#GOOD PRACTICES:

    # Write good comments.
    # Usin Dry code (Dont Repeat Yourself)
    # Namin variables well

# CONVENTION TO CREATE CLASSES:
    # CamelCase with CapWords => Example: YorkshireTerrier


# cuando se trabaja con clases, se recomienda que sus atributos sean ocultos y crear un metodo que imprima esos valores para poderlos consultar possteriormente. adicionalmente se considera buena practica encapsular los metodos tambien y dentro de un objeto property establecer los getters, setters and deletters para que queden como publicos.

"""     #FORMA 1 PARA UTILIZAR EL OBJETO PROPERTY:
        class Empleado:
            def __init__(self,nombre,salario):
                self.__nombre = nombre
                self.__salario = salario

            def __getnombre(self):
                return self.__nombre
            def __getsalario(self):
                return self.__salario
            

            def __setnombre(self, nombre):
                self.__nombre = nombre
            def __setsalario(self, salario):
                self.__salario = salario

            def __delnombre(self):
                del self.__nombre
            def __delsalario(self):
                del self.__salario


            nombre = property( fget= __getnombre,
                            fdel= __delnombre,
                            fset= __setnombre
                            )
            
            salario = property(fget = __getsalario,
                            fset = __setsalario)

        empleado = Empleado('Camilo', 3000)
        empleado.salario = 4000
        print (empleado.nombre)
"""
## ____________________________________
"""     #FORMA 2 PARA UTILIZAR EL OBJETO PROPERTY:
        class Animal:
            def __init__(self, nombre, edad):
                self.__nombre = nombre
                self.edad = edad
            
            def getname (self):
                return self.__nombre
            
            @property
            def nombre(self):
                return self.__nombre

            @nombre.setter
            def nombre(self, nombre):
                self.__nombre = nombre

            @nombre.deleter
            def nombre(self):
                del self.__nombre 
""" 


""" a = Animal ('dudy')
print(a.__dict__['nombre'])
print(a.nombre) """


class Perro:
    def __init__(self, nombre, sound):
        self.nombre = nombre
        self.sound = sound
       
class Mamifero:
    def __init___(self, tipo):
        self.tipo = tipo
        
class Proof(Perro):
    pass

p = Proof('locky', 'wow')
print (vars(p))

# print (vars(p))
print(p.__dict__)

tupl = tuple()

# print(isinstance(tuple(), object))


a = 'ab'
b = 'ab'
c= 3

f = [1,2,3,4,5]
g = [1,2,3,4,5]

""" print (id(a), id(b), id(c))
print(id(len(f)), id(5)) """

""" print(id(f), id(g)) """

fgh = round(2.345874152,2)
""" 
print(type(fgh))
print(round(fgh,2))
r = 2.35
print((id(fgh),id(r)))
print (fgh==r)

obj = {'1':1, '2':2, '3':3}
print(list(obj.items())) """



