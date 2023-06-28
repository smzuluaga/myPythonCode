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
    sound = 'watever'

p = Perro()
p.sound = 'waf'
print (p.sound)
s = Perro ()
print(s.sound)
