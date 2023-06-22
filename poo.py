# PARADIGMAS DE LA PROGRAMACION:
# Paradigma = Teoria que suministra la base y modelo para resolver problemas.
    #   * Programacion Funcional (paradigma de la programacion declarativa - está basado en funciones (ciudadanas de primera clase) y prioriza el uso de la recursividad y HOF)
    #   * Programacion Estructurada (Secuencial - basado en las 3 estructuras de control básicas Secuencia, Condicionales, Ciclos)
    #   * PROGRAMACION ORIENTADA A OBJETOS - POO/ OOP

# PROGRAMACION ORIENTADA A OBJETOS.

    # Es uno de los paradigmas de la programación que permite programar mucho más rápido, puesto que el análisis que se debe hacer antes de implementar el código debe ser mayor.
    # Permite dejar de copiar y pegar código,  y permite tomar el control del proyecto, del código y generar código de más calidad 'CLEAN CODE'
    # La programación a objetos viene orientada a cubrir huecos que la programación estructurada ha dejado.
    # Esta orientado a descomponer un problema en la abstraccion de objetos, para poder buscar una solucion en codigo.

# VENTAJAS vs la programación estructurada:
    #   * Código más corto y facil de mantener.
    #   * Da soluciones precisas.
    #   * Simplifica la programación.
    #   * Si se rompe algo no necesariamente deja de funcionar como en programacion estructurada, puesto que allí como se ejecuta línea por línea, de forma secuancial, si no funciona una linea, el sistema deja de correr.

# COMPONENTES / ELEMENTOS:
    #   * Clases
    #   * Propiedades/Atributos
    #   * Métodos/Comportamientos
    #   * Objetos


# CLASES - es un modelo sobre el cual se construirá el objeto. parte del análisis de un objeto en su forma más general, de esta manera, podremos crear muchos  objetos a partir de dicha clase, con sus respectivos atributos y métodos. posteriormente, luego de definida la clase, podemos crear instancia de dicha clase con los objetos.

    # MODULARIDAD - esta muy relacionado con las clases, y es uno de los principios de OOP. Diseño modular es subdividir el sistema en partes más pequeñas (módulos), los cuales pueden funcionar de manera independiente pero en pro del sistema.
    # ayuda que cuando hay un error, solo se afecte el módulo, más no todo el sistema, como es el caso de la programación estructurada.
    # permite reutilizar código, evitar colapsos, hacer un código más mantenible, legibilidad, y resolución rápida de problemas.
    # en ese orden de ideas, la clases provocan la modularidar las diferentes partes de un objeto y de esta forma goza de las ventajas de la  modularizacion.
    # las clases deben estar en archivos separados para generar la modularidad y mantener el código aislado.

    # REUTILIZACION / DRY - Dont Repeat Yourself - la reutilizacion es un principio de OOP que promueve la reduccion de duplicados en la programación, puesto que la duplicidad incrementa la dificultad en los cambios y en la evolucion.

# 4 PILARES DE LA POO:
    #   * Encapsulamiento
    #   * Abstracción
    #   * Herencia
    #   * Polimorfismo

    #ENCAPSULAMIENTO / ENCAPSULACIÓN - hacer que un dato sea inviolable o inalterable cuando se le asigna un modificador de acceso. es la práctica de esconder informacion dentro de una 'caja negra' para que cuando otros desarrolladores trabajen con el codigo no tengan de que preocuparse. no solo los datos pueden ser encapsulados, sino tambien comportamientos.

        #MODIFICADOR DE ACCESO. - determina un nivel de acceso a los datos. 
            #*Public - Todas las clases, es el más permisivo de todos.
            #*Protected - puede ser accedido anivel de la clase y los paquetes de la clases y subclases.
            #*Default - permite el acceso a clases internas y paquetes, en la herencia no podemos ver este atributo.
            #*Private - Puede ser accedido solo a nivel de clase. (se usa un '__' antes del nombre de la propiedad que queremos hacer privada => Example: self.__height = height)

    # ABSTRACCION - cuando abstraemos los datos de un objeto y construimos un molde (clase). busca manejar la complejidad escondiendo elementos innecesarios de los objetos. en la abstraccion se identifica que informacion y comportamientos deben ser encapsulados

    # HERENCIA (Inheritance) Main Pilar - permite crear nuevas clases a partir de otras. existe una jerarquía y una relación padre e hijo. en este escenario, un padre puede tener muchos hijos.:
    #   *clase padre - (SUPERCLASE)
    #   *clases hijas - (SUBSCLASES)
    # usualmente la herencia sucede en un contexto donde tenemos variaas clases con propiedades repetidos, entonces se crea una super clase con esos atributos en comun y las subclases heredan dichas propiedades, que pueden ser complementados por otras propiedades propias de cada clase. es propia de lenguajes como Python,  JS, Java y Ruby.
    #no obstante lo anterior, tambien pueden existir super clases a partir de la logica del negocio, apesar de que dichas subclases no compartan propiedades en comun, por ejemplo, solo el id.
    # Usa el método super() para extender las propiedades de una super clase a una subclase. Example:
"""     class Animal:
            def __init__(self, num_legs):
                self.num_legs = num_legs

        class Cow(Animal):
            def __init__(self):
                # call the parent constructor to
                # give the cow some legs
                super().__init__(4) #En esta linea se esta extendiendo las propiedades de la superclase Animal a la subclase Cow.
"""
    #POLIMORFISMO - (muchas formas) es cuando tenemos un metodo heredado de una super clase a varias subclases y cada sub-clase, le da el comportamiento que ella necesita. es decir, construit métodos con el mismo nombre, pero con diferente comportamiento. esposiblemente el pilar más poderoso de OOP. esla habilidad de una variable, funcion o objeto de tomar múltiples formas. Example:
"""
        class Creature():
            def move(self):
                print("the creature moves")

        class Dragon(Creature):
            def move(self):
                print("the dragon flies")

        class Kraken(Creature):
            def move(self):
                print("the kraken swims")

        for creature in [Creature(), Dragon(), Kraken()]:
            creature.move()
"""


# OBJETOS - son instancias de las clases, es decir, ES el resultado del modelado que creamos como clase a partir de la abstraccion de un objeto y con los objetos ya le damos vida a las clases.

# INSTANCIA DE LAS VARIABLES DE OBJETOS vs. INSTANCIA DE LAS VARIABLES DE LAS CLASES -  La instancia de las variables varian entre objeto y objeto, y a pesar de que sean declaradas en el metodo constructor con un valor, una vez instaciada la clase en un nuevo objeto, dicho valor puede ser cambiado. sin embargo, cuando  cambiamos un valor de una variable a nivel clase, se cambia en todas los objetos donde esta ha sido instanciada, hay que tener mucho cuidado con el uso de esta ultima.

# LENGUAJES QUE USAN POO:
    #   * Python - JavaScript / Java / Php / C++ / C# / Ruby / Kotlin / etc.

    #  * JAVA - Orientado a objetos por naturaleza (creado con ese fin) // muy usado en desarrollo movil (Android) // es Server Side. // extension = .java

    #  * PHP - Lenguajeinterpretado // pensado para la web // extension = .php

    #  * PYTHON - Diseñado para ser fácil de usar // múltiples usos: web (D-Jango), server side, análisis de datos // extension = .py // OOP

    #  * JAVASCRIPT - Lenguaje interpretado // OOP - pero su naturaleza son los prototipos // pensado para la web pero tambien se puede correr servr side (node.js) // extension = .js

# PASOS DE LA POO
    # 1. Análisis (observacion, entendimiento, lectura) -> # 2. Diagramación (graficar bosetos) -> 3. Programación 

    # 1. ANÁLISIS - Observar el problema e identificar los objetos, estos objetos deben ser analizados dentro de un 'CONTEXTO'. estos siempre van a ser SUSTANTIVOS (ejm: un mouse, una manzana, un pc, etc) y van a tener propiedades(atributos) y comportamientos (métodos). los objetos pueden ser físicos (ejm: una persona, una fruta) o conceptuales (no son físicos).
    # los atributos tambien son sustantivos (tamaño, nombre, forma, estado) son características de ese objeto.
    # los comportamientos son verbos o sustantivos y verbos, ya que son las acciones que puede hacer el objeto.
    # Ejemplo. un usuario es un objeto físico y un inicio de sesión puede ser un objeto conceptual (propiedades: fecha de inicio de sesion, restricciones pra usuario y clave / comportamientos: login, log out, etc).

    # 2. DIAGRAMAS DE MODELADO.

    # OMT - Object Modeling Techniques - metodología para el análisis orientado a objetos.
    # luego del análisis identificar y nombrar los objetos, se debe crear cada objeto en un recuadro y plasmar sus atributos y métodos y posteriormente, establecer una relación entre los objetos. (esta en desuso) es un antecesor de UML.

    # UML - Unified Modeling Languge - Lenguaje de modelado unificado. es una version mejorada de OMT. acá podemos modelar clases, bojetos, casos de uso, actividades, iteraciones, estados, implementacion.

    # GRAFICAR UNA CLASE EN UML - através de este proceso, le asignamos a las clases una identidad (nombre de la clase), estado (atributos) y comportamientos (métodos), ver anexo1 para visualizar la imágen en UML.

        # Representacion de clases en  UML:

            #   En la parte superior se colocan los atributos o propiedades, y debajo las operaciones de la clase.  el primer caracter con el que empiezan es un símbolo. Este denotará la visibilidad del atributo o método esto es un término que tiene que ver con Encapsulamiento.
            # Estos son los niveles de visibilidad que puedes tener:
            # - private // + public // # protected // ~ default

        # Representacion de relaciones:

            # Asociacion (→) : cada vez que esté referenciada este tipo de flecha significará que ese elemento contiene al otro en su definición. La flecha apuntará hacia la dependencia.
            # Example:
            #    A  → B (Indica que la clase A esta asociada y depende de la claseB)

            # Herencia (🠚) : estará expresando la herencia. La dirección de la flecha irá desde el hijo hasta el padre.
            # Example:
            #   A 🠚 B (indica que A hereda de B)

            # Agregacion (◇-) : Este se parece a la asociación en que un elemento dependerá del otro, pero en este caso será: Un elemento dependerá de muchos otros. Aquí tomamos como referencia la multiplicidad del elemento. Lo que comúnmente conocerías en Bases de Datos como Relaciones uno a muchos.
            # Example:
            # A ◇- B (Indica que la clase A contiene varios elementos de la clase B)

            # Composicion (◆-) : Este es similar al anterior solo que su relación es totalmente compenetrada de tal modo que conceptualmente una de estas clases no podría vivir si no existiera la otra.
            # Example:
            # A ◆- B (Indica que la clase A contiene varios elementos de la clase B)


# 3. PROGRAMAR LOS PASOS ANTERIORES (PYTHON & JAVASCRIPT)

    # DEFINIR UNA CLASE
        # palabra revervada class:
"""     * Python => 
                        class Person:
                            name = '' #Atributos.(Estado)
                            def Walk (self): #Métodos. (Comportamientos)
    """ 
     
"""     * JavaScript => 
                        class Car {
                                constructor(license, driver) {
                                    this.id;
                                    this.license = license;
                                    this.driver = driver;
                                    this.passenger;
                                } 
                            }
    """  

        #los metodos de las clases en python siempre deben llevar la como primer argumento la plaabra self para hacer referencia al objeto en si mismo. por lo tanto a través de su uso, podemos leer y actualizar las propiedades del objeto.

        #Para llamar a un metodo de un objeto, basta con usar el nombre del objeto y con notacion de punto la propiedad:
        #       ' object.method() '

        # Los métodos usualmente no retornan nada porque mutan las propiedades del objeto, pero ellos tambien pueden retornar un valor.

    #METODO CONSTRUCTOR. da un estado inicial a cada objeto // tiene el mismo nombre de la clase // los argumentos que le pasamos al metodo constructor cuando estamos dando vida a una nueva instancia de la clase, son los parámetros mínimos que necesita el objeto para que pueda vivir. esto significa que estamos instanciando e inicializando el objeto en la misma linea. 
    # Pyhon usa el metodo:  ' __init__() ' que se llama automáticamente cuando un nuevo objeto es creado.

"""    * PYTHON => 
                def _init_(self,name):
                    self.name = name 
                    self.__height = height # Encapsulamiento (Private)
"""

"""    * JAVASCRIPT => ORGANIZAR CON EL NUEVO METODO CONSTRUCTOR DE ES6-2015
                    function Person(name) {
                        this.name = name
                       }
"""

    # DECLARACION DE OBJETOS / (Instanciar una clase) - usualmente se instancian nuevos objetos de una clase en una nueva variable y se utiliza su método constructor:

        #   * PYTHON => 
        #            person = Person()
        #   * JAVASCRIPT =>
        #            let person = new Person();

    # EXAMPLE = 
    # Declaracion de la clase.
"""    class Soldier:
            
            def __init__(self, armor, num_weapons): # Método Constructor
                self.armor = armor
                self.num_weapons = num_weapons 

            def take_damage(self, damage): #Método
                self.health -= damage
"""
"""
        soldier_one = Soldier()
        soldier_one.take_damage(2)
        print(soldier_one.health)
            #Output => prints "3"
"""







# 3. PROGRAMAR LOS PASOS ANTERIORES (PHP & JAVA)

# DEFINIR UNA CLASE
# palabra revervada class:

"""     * Java => 
                    class Person {
                        String name = '';
                        void Walk () {}
                    } """

"""     * Php => 
                    class Person {
                        $name = ''
                        function Walk () {}
                    } """

# DECLARACION DE OBJETOS - usualmente se instancian nuevos objetos de una clase en una nueva variable y se utiliza su método constructor:

    #   * JAVA - Person person = new Person ('Ann');
    #   * PHP - $person = new Person('Ann');


# METODO CONSTRUCTOR -  da un estado inicial a cada objeto // tiene el mismo nombre de la clase // los argumentos que le pasamos al metodo constructor cuando estamos dando vida a una nueva instancia de la clase, son los parámetros mínimos que necesita el objeto para que pueda vivir. esto significa que estamos instanciando e inicializando el objeto en la misma linea.

"

"""    * JAVA - public Person(String name) {
                        this.name = name;
                       }"""

"""    * PHP - public function_constructor($name) {
                        $this->name = name;
                       }"""

# EJEMPLO CREACION OBJETO EN PY

""" from car import Car # lo primero es importar el módulo y la clase, debe estar en la misma carpeta donde esta el archivo que vamos a llamar

car = Car () # luego instanciamos el objeto en una nueva variable y empezamos a inicializar los atributos de la clase asignandoles valores.
car.license = "AMS587"
car.driver = "Camila Gomez"
print(vars(car)) # esta es la forma de imprimir en consola  las priedades que ya hemos inicializado """












