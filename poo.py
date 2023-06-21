# PARADIGMAS DE LA PROGRAMACION:
#   * Programacion Funcional (paradigma de la programacion declarativa - está basado en funciones (ciudadanas de primera clase) y prioriza el uso de la recursividad y HOF)
#   * Programacion Estructurada (Secuencial - basado en las 3 estructuras de control básicas Secuencia, Condicionales, Ciclos)
#   * PROGRAMACION ORIENTADA A OBJETOS - POO/ OOP

# PROGRAMACION ORIENTADA A OBJETOS.

# Es uno de los paradigmas de la programación que permite programar mucho más rápido, puesto que el análisis que se debe hacer antes de implementar el código debe ser mayor.
# Paradigma = Teoria que suministra la base y modelo para resolver problemas.
# Permite dejar de copiar y pegar código,  y permite tomar el control del proyecto, del código y generar código de más calidad.
# La programación a objetos viene orientada a cubrir huecos que la programación estructurada ha dejado.
# Esta orientado a descomponer un problema en la abstraccion de objetos, para poder buscar una solucion en codigo.


# VENTAJAS vs la programación estructurada:
#   * Código más corto y facil de mantener.
#   * Da soluciones precisas.
#   * Simplifica la programación.
#   * Si se rompe algo no necesariamente deja de funcionar como en programacion estructurada, puesto qeu allí como se ejecuta línea por línea, de forma secuancial, si no funciona una linea, el sistema deja de correr.

# COMPONENTES / ELEMENTOS:
#   * Clases
#   * Propiedades
#   * Métodos
#   * Objetos

# 4 PILARES DE LA POO:
#   * Encapsulamiento
#   * Abstracción
#   * Herencia
#   * Polimorfismo

# LENGUAJES QUE USAN POO:
#   * Python - JavaScript / Java / Php / C++ / C# / Ruby / Kotlin / etc.

#  * JAVA - Orientado a objetos por naturaleza (creado con ese fin) // muy usado en desarrollo movil (Android) // es Server Side. // extension = .java

#  * PHP - Lenguajeinterpretado // pensado para la web // extension = .php

#  * PYTHON - Diseñado para ser fácil de usar // múltiples usos: web (D-Jango), server side, análisis de datos // extension = .py // OOP

#  * JAVASCRIPT - Lenguaje interpretado // OOP - pero su naturaleza son los prototipos // pensado para la web pero tambien se puede correr servr side (node.js) // extension = .js

# PASOS DE LA POO
# Análisis (observacion, entendimiento, lectura) -> 
# Diagramación (graficar bosetos) -> Programación 

# 1. ANÁLISIS - Observar el problema e identificar los objetos, estos objetos deben ser analizados dentro de un 'CONTEXTO'. estos siempre van a ser SUSTANTIVOS (ejm: un mouse, una manzana, un pc, etc) y van a tener propiedades(atributos) y comportamientos (métodos). los objetos pueden ser físicos (ejm: una persona, una fruta) o conceptuales (no son físicos).
# los atributos tambien son sustantivos (tamaño, nombre, forma, estado) son características de ese objeto.
# los comportamientos son verbos o sustantivos y verbos, ya que son las acciones que puede hacer el objeto.
# Ejemplo. un usuario es un objeto físico y un inicio de sesión puede ser un objeto conceptual (propiedades: fecha de inicio de sesion, restricciones pra usuario y clave / comportamientos: login, log out, etc).

# 2. DIAGRAMAS DE MODELADO.

# OMT - Object Modeling Techniques - metodología para el análisis orientado a objetos.
# luego del análisis identificar y nombrar los objetos, se debe crear cada objeto en un recuadro y plasmar sus atributos y métodos y posteriormente, establecer una relación entre los objetos. (esta en desuso)

# UML - Unified Modeling Languge - Lenguaje de modelado unificado. es una version mejorada de OMT. acá podemos modelar clases, bojetos, casos de uso, actividades, iteraciones, estados, implementacion.

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

# GRAFICAR UNA CLASE EN UML - através de este proceso, le asignamos a las clases una identidad (nombre de la clase), estado (atributos) y comportamientos (métodos), ver anexo1 para visualizar la imágen en UML.


# 3. PROGRAMAR LOS PASOS ANTERIORES

# palabra revervada class:
"""     * Java => class Person {
                        String name = '';
                        void Walk () {}
                    } """

"""     * Php => class Person {
                        $name = ''
                        function Walk () {}
                    } """

"""     * Python => class Person:
                        name = ''
                        def Walk (): """

"""     * Js => #forma1 class Person {
                        String name = '';
                        void Walk () {}
                    } """
"""             #forma2 Person.prototype.walk = function () {}"""

# CLASES - es un modelo sobre el cual se construirá el objeto. parte del análisis de un objeto en su forma más general, de esta manera, podremos crear muchos  objetos a partir de dicha clase, con sus respectivos atributos y métodos. posteriormente, luego de definida la clase, podemos crear instancia de dicha clase con los objetos.

# ABSTRACCION - cuando abstraemos los datos de un objeto y construimos un molde (clase)

# MODULARIDAD - esta muy relacionado con las clases, y es uno de los principios de OOP. Diseño modular es subdividir el sistema en partes más pequeñas (módulos), los cuales pueden funcionar de manera independiente pero en pro del sistema.
# ayuda que cuando hay un error, solo se afecte el módulo, más no todo el sistema, como es el caso de la programación estructurada.
# permite reutilizar código, evitar colapsos, hacer un código más mantenible, legibilidad, y resolución rápida de problemas.
# en ese orden de ideas, la clases provocan la modularizar las diferentes partes de un objeto y de esta forma goza de las ventajas de ña , modularizacion.
# las clases deben estar en archivos separados para generar la modularidad y mantener el código aislado.

# REUTILIZACION / DRY - Dont Repeat Yourself - la reutilizacion es un principio de OOP que promueve la reduccion de duplicados en la programación, puesto que la duplicidad incrementa la dificultad en los cambios y en la evolucion.

# HERENCIA - permite crear nuevas clases a partir de otras. existe una jerarquía y una relación padre e hijo. en este escenario, un padre puede tener muchos hijos.:
#   *clase padre - (SUPERCLASE)
#   *clases hijas - (SUBSCLASE)
# usualmente la herencia sucede en un contexto donde tenemos variaas clases con propiedades repetidos, entonces se crea una super clase con esos atributos en comun y las subclases heredan dichas propiedades, que pueden ser complementados por otras propiedades propias de cada clase.

#no obstante lo anterior, tambien pueden existir super clases a partir de la logica del negocio, apesar de que dichas subclases no compartan propiedades en comun, por ejemplo, solo el id.


# OBJETOS - son instancias de las clases, es decir, el resultado del modelado que creamos como clase, a partir de la abstraccion de un objeto y con los objetos ya le damos vida a las clases.

# DECLARACION DE OBJETOS - usualmente se instancian nuevos objetos de una clase en una nueva variable y se utiliza su método constructor:

#   * PYTHON - persona = Person('Ann')
#   * JAVASCRIPT - var person = new Person('Ann');
#   * JAVA - Person person = new Person ('Ann');
#   * PHP - $person = new Person('Ann');

# METODO CONSTRUCTOR -  da un estado inicial a cada objeto // tiene el mismo nombre de la clase // los argumentos que le pasamos al metodo constructor cuando estamos dando vida a una nueva instancia de la clase, son los parámetros mínimos que necesita el objeto para que pueda vivir. esto significa que estamos instanciando e inicializando el objeto en la misma linea.

"""    * PYTHON - def _init_(self,name):
                    self.name = name """

"""    * JAVASCRIPT - function Person(name) {
                        this.name = name
                       }"""

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







