# REGULAR EXPRESIONS - REGEX

# Patrones de caracteres (formulas) para dar manejo a cadenas de caracteres o strings. la intencion de las regex es que los strings cumplan ciertas condiciones o patrones para poder retornarlos y dichas condiciones estaran determinados por el patron de caracteres o la formula que determinemos con la regular expression. Con las regex quitamos de un string lo que no nos sirve y dejamos lo que nos es util de acuerdo a la logica del problema. por ejemplo con las regex podemos limpiar la basura de un csv para dejarlo con la informacion extrictamente necesaria para operarcion.

# el proposito principal de las regex es busqueda/filtrado.


# CLASES DE REGEX 

# CLASE . - (punto) denota cualquier caracter(numero, letra, espacio, símbolo, tab, caracter invisible) - cuando buscamos por ejemplo con el punto, pareciera que esta señalando toda la linea completa o todo el archivo completo, sin embargo, esta señalando caracter por caracter. 
    ## se puede poner por ejemplo la sig. expresion '. =' la cual nos buscará cualquier caracter que seguidamente tenga un espacio y posteriormente un signo igual.
    ## se puede poner por ejemplo la sig. expresion '. ' la cual nos buscará cualquier caracter que seguidamente tenga un espacio'.
    ## se pueden poner varios puntos segidos '..' por ejemeplo 2 puntos seguidos, indicando que busque un caracter que tenga dos caracteres seguidos, cuando una linea queda señalada completamente, es porque la cantidad de caracteres es multiplo de la cantidad de puntos, entonces por ejemplo en una linea de 10 digitos, quedarían 5 parejas de digitos de a 2.

    ## del punto nacen 3 tipos de clases principales predefinidas por la sintaxis de regex.
        ## digito
        ## palabra (cualquier caracter que pueda ir en una palabra)
        ## espacio (espacio simple, tab)

    ## \d - (CLASE digit) buscar un digito
        ## se puede poner varias veces seguidas, por ejemplo '\d\d' para indicar que busque los numeros que tengan dos digitos consecutivos 
        ## otra notacion para buscar digitos sería [0-9], nos permite hacer búsquedas mucho más potentes y personalizadas ya que le podemos indicar el rango de numeros que queremos buscar, por ejemplo [6-9]

    ## \w - (CLASE word) (all word characters) buscar una palabra que contenga los siguientes caracteres:  'a-z' 'A-Z' '_' '0-9'
        ## otra notacion para buscar palabras sería [a-z], nos permite hacer búsquedas mucho más potentes y personalizadas ya que le podemos indicar el rango de letras que queremos buscar, por ejemplo [a-m] buscaría las letras minusculas entre la a y la m, tambien se puede buscar solo mayusculas [A-Z] o mayusculas y minusculas al mismo tiempo y tambien buscaría los guines bajos [a-zA-Z_] - finalmente podemos buscar tambien digitos y letras al mismo tiempo [a-zA-Z0-9_]
        ## cuando estamos usando la notacion de corchetes, tambien podemos buscar el punto(como caracter, no como clase, para ello debemos escaparlo con backslash asi  [a-zA-Z0-9_\.]

    ## \s (CLASE white spaces) - busca todos los espacios en blanco. los saltos de linea '\n\r' '\n' tambien son espacios en blanco

# ESCAPADO - cuando queremos buscar un caracter que a su vez es un caracter reservado de las regex, debemos pasarlo con un backslash antes, como por ejemplo le punto\. 
    # se puede escapar varios caracteres,se puede abrir corchete [\.\-], sin embargo, cada caracter debe tener su propio escapado. 

    # CARACTERES QUE DEBEN SER ESCAPADOS:
        # \+
        # \[ \]
        # \-
        # \.
        # \\
        # \/caracter
        # \(
        # \)
        # \?

# NEGACION - (^) se usa para expresar una busqueda, pero que retorne todo lo contrario a pasado por parámetro. por ejemplo, si expresamos'[^0-9]' el sistema retornará todo lo que sea diferente de los números del 0 al 9 

# AGRUPACION - se usa para agurpar expresiones, para ello se utilizan los parentesis '()'. esta heramienta es muy potente, ya que despues se puede reemplazar todo lo que no este en grupos, por nada y dejar unicamente lo que estaba dentro de grupos con la notacion '$1,$2,...' y asi sucesivamente, dependiendo la cantidad de grupos que hayamos declarado. posteriormente esto se  puede llevar a SQL o JSON
    # en los agrupadores se pueden usar cosas como el pipe, para indicar que busque una cosa u otra, por ejemplo (a|b) buscará a o b.

# DELIMITADORES - son contadores, indican si algo existe o no existe
    # SI DEBEN APARECER, SE DEBE USAR +
    ## + (uno o mas) - indica que el caracter anterior se puede repetir entre 1 y más veces. 

    # SI PUEDEN APARECER O NO, SE USA * ó ?
    ## * (greedy) - indica que el caracter anterior se puede repetir entre 0 y más veces.
    ## ? (cero o uno) - indica que el caracter anterior es opcional, se puede repetir entre cero y una vez
    ## +? /lazy) se pueden combinar +? para hacer el match lo más pequeño o concreto posible. por ejemplo: dado el sig string 'csv1,csv2,csv3,csv4,csv5' si usamos la expresion '.+?,' el programa buscará todo lo que termine con una ',' pero el sistema siempre prioriza a la búsqueda más grande y luego a la más pequeña. con +? busca la coincidencia más pequeña, en ese caso cada match sería 'csv2,' antes de encontrar la coma anterior, si le quitamos el ?, el sistema traera de la coma hacia atrás todo hasta el inicio de la linea.

# CONTADORES - cuando necesitamos una cantidad X precisa de apariciones de un caracter.
    # {n1,n2} se usa expresion de llaves, donde n1 es el numero minimo de apariciones que queremos encontrar y n2 es el numero maximo de apariciones que queremos encontrar, si queremos que sea un numero especifico, ponemos n1 y n2 el mismo valor {1,1}. primero evalua los matches superiores y luego evalua los inferiores.

# REGEX DE LINEA COMPLETA - es una forma  en la cual la linea completa debe cumplir con la expresion regular o se descarta, no existen coincidencias parciales.  ^ ------------- $
    ## (^) - denota el inicio de la linea
    ## ($) - denota el final de la linea
    # por ejemplo. la siguien
    # te expresion '^[^\d].*$' solo hace match las lineas que no inicien con un digito.

# REGEX EN LOGS
    # LOS LOGS o registros en el sector IT hacen referencia a los archivos de texto en los que se incluyen de forma cronológica los acontecimientos como cambios, actualizaciones y demás que han ocurrido dentro de un sistema informático, como puede ser un servidor, una aplicación o un programa.
    # ^\[LOG.*\[ERROR\].*$
    # ^\[LOG.*\[WARN\].*$
    # con los anteriores ejemplos podemos ver como con regex de linea completa podemos explorar en logs inmensos, y pedirle que nos traiga solo lo que necesitamos, retornando lineas completas

# REGEX EN PYTHON - https://docs.python.org/3/library/re.html#functions (OFFICIAL DOCUMENTATION)

    # 1. se debe importar la librería re
         # import re
    # se usa (r'regex') => donde regex es la expresion regular
    # se puede almacenar envariables, ejemplo regex = r'expresion_regular'

# METACARACTERES EN PYTHON
    # [] - indica un conjunto de caraacteres - Exmpl - [a-m] encuentra todas las coincidencias de letras entre la a y la m // [ar] encuentra todas las coincidencias a o r
    # \ - señala una secuencua especial - Exmpl - \d \w \s
    # . - indica cualquier caracter
    # ^ - comienza con..
    # $ - termina con..
    # * - cero o mas ocurrencias
    # + - una o más ocurrencias
    # ? - cero o una ocurrencia
    # {} - especifica el numero exacto de ocurrencias
    # | - indica si se busca x o y - Exmpl - (a|b) 
    # () - termino de agrupacion.

# SECUANCIAS ESPECIALES EN PY
    # \A retorna un match si el caracter/es especificado esta al INICIO del STRING/CADENA (se debe usar con metodo, por ejemplo con findall) Exmp - re.findall("\AThe", txt)

    # \Z retorna un match si el caracter/es especificado esta al FINAL del STRING/CADENA (se debe usar con metodo, por ejemplo con findall) Exmp - re.findall("Spain\Z", txt)

    # \b retorna un match si el caracter/es especificado  esta al inicio o al final de una PALABRA (se debe usar con metodo, por ejemplo con findall) Exmp - 
        # Para validar si se encuentra al inicio de una palabra, se  usa => re.findall(r"\bain", txt) 
        # Para validar si se encuentra al final de una palabra, se  usa => re.findall(r"ain\b", txt) 

    # \B retorna un match si el caracter/es especificado NO ESTA al inicio o al final de una PALABRA (se debe usar con metodo, por ejemplo con findall) Exmp - 
        # Para validar si NO se encuentra al inicio de una palabra, se  usa => re.findall(r"\Bain", txt) 
        # Para validar si NO se encuentra al final de una palabra, se  usa => re.findall(r"ain\B", txt) 

    #SECUENCUAS ESPECIALES TRANSVERSALES (ALL LANGUAGES)
    # \d - retorna match si el caracter especificado contine un digito entre [0-9]
    # \D - retorna match si el caracter especificado NO contine un digito entre [0-9]
    # \s - retorna match si el caracter especificado contine un espacio en blanco (otros caracteres de espacios en blanco es \r \n \t \f)
    # \S - retorna match si el caracter especificado NO contine un espacio en blanco
    # \w - retorna match si el caracter especificado contine un caracter de palabras ([a-z][A-Z][0-9]_)
    # \W - retorna match si el caracter especificado NO contine un caracter de palabras ([a-z][A-Z][0-9]_)

# SETS
    # [arn] - retorna un match si uno de los caracteres especificados (a, r o n) esta presente en el string 
    # [^arn] - retorna un match de cualquier coincidencia en els tring de caracteres diferente a los especificados (a, r o n)
    # [a-n] - retorna un match para cualquier coincidencia de letra en minuscula entre la a y la n
    # [012] - retorna un match si uno de los digitos especificados (0,1 o 2) estan presentes en el string
    # [0-9] - retorna un match si un digito entre 0 y 9 esta presente en el string
    # [0-9][0-9] - retorna un match si encuentra una coincidencia entre numeros que contengan más de 2 digitos, la condicion del primer digito estará condicionada por el primer argumento de cada set, y el segundo digito estará condicionado por el argumento del segundo set. si se necesita buscar numero de 3 cifras, se buscaría [0-9][0-9][0-9] y así sucesivamente.
    # [+, *, ., |, (), $,{}] - retorna un match si enceuntra uno de los caracteres. como estos son caracteres reservados, si estan en un set, no asumiran su papel en el lenguaje, sino que se buscará coincidencias en el string con estos parmaetros. en algunos lenguajes dichos caracteres deben ser escapados
    # (A|B) - busca una de las alternativas separadas por pipe operator.

# SPECIAL CASES
    # negative lookbehind (?<!regex2)regex1 - indica que regex 1 no debe ir precedido por el patron que determinemos en regex2
    # positive lookbehind (?<=regex2)regex1 - indica que regex 1 debe ir precedido por el patron que determinemos en regex2
    # loosahead regex(?=\=) - busca las coincidencias que cumplan con el regex y que terminen por ejemplo con =, pero retorna la coincidencia sin traer el caracter =

# METODOS REGEX EN PYTHON (primer parámetro = regex, segundo parámetro = string donde queremos buscar)


    # FIND ALL -  retorna UNA LISTA['match', 'match', 'match'] con todos los matches, la lista retorna en el orden en que cada caracter es encontrado, si no encuentra matches retorna una lista vacia[]
"""
        x = re.findall("[a-m]", txt)
        #              ______   ____
        #                 1       2   => 1. regex // 2. string donde va a evaluar el regex
        print(x)
        # Output => ['h', 'e', 'a', 'i', 'i', 'a', 'i']
""" 
    # MATCH - retorna un match object encuentra una coincidencia al inicio de la linea, de lo contratio retorna None
"""
    x = re.match("s.+", txt) # en este caso para retornar match object, la linea tendria que empezar con un +
"""    

    # SEARCH - retorna un match object con la primera coincidencia que encuentre en el string pasado como segundo parámetro,  que haga match con el regex pasado como primer parámetro.
"""
    x = re.search("\s", txt)
"""    

    # MATCH OBJECT - retorna informacion sobre la buqueda, informa el indice de inicio y fin donde encontro la primera coincidencia, y los caracteres que se encuentran en ese rango de indices. sino encuentra un match, retornara 'None'. el string object tiene propiedades y métodos para retornar informacion precisa del objeto:

        #Example = con el string txt = "The rain in Spain" y  regex 'x = re.search(r"\bS\w+", txt)' 
        #                                                                          ________   ____
        #                                                                               1       2  => 1. regex // 2. string donde va a evaluar el regex

        # Propiedad x.string - retorna el string que se paso como parámetro para hacer la busqueda del regex. Retorna =>  "The rain in Spain"
        # Método x.group() -  retorna el slice del string en las posiciones que indica el span, que fue la parte del string donde encontró la primera coincidencia. Retorna => 'Spain'
        # Método x.span() - retorna una tupla con la posicion inicial y final donde encontro la primera coincidencia de búsqueda. => Retorna => (12, 17)
        # Método x.start() - retorna el indice de la posicion inicial donde  encontro la primera coincidencia de búsqueda. => Retorna => 12
        # Método x.end() - retorna el indice de la posicion final donde encontro la primera coincidencia de búsqueda. => Retorna => 17

    # SPLIT - Retorna una lista con los elementos del string separados donde encuentra la coincidencia, de acuerdo al patron determinado en el regex. recibe 3 paramatros:

        # x = re.split("\s", txt, 1)
        #    _________ ___   ___  _ 
        #               1     2   3 => 1. regex // 2. string donde va a evaluar el regex // 3. maxsplit = numero máximo de veces que queremos que haga la separacion, si por ejemplo el regex encuentra 3 coincidencias, pero le pasamos como parámetro maxsplit 1, solo hará la division en la primera coincidencia y la lista quedará con 2 elementos.
        # Example:
"""
        txt = "The rain in Spain"
        x = re.split("\s", txt,1)
        print(x)
        #Output => ['The', 'rain in Spain']
"""

    # SUB - reemplaza los mateches, por el texto que le pasemos como parámetro

    # x = re.sub("\s", "9", txt, max)
    #            ___   ___  ___  ___
    #            1     2     3    4  => 1. regex // 2. texto por el que queremos reemplazar la coincidencia // 3. string en el que vamos a evaluar el  regex y hacer los cambios // 4. numero máximo de veces que queremos que haga el reemplazo.
    #Example:
""" 
        txt = "The rain in Spain"
        x = re.sub("\s", "9", txt,1)
        print(x)
        # Output => 'The9rain in Spain'
"""

    #PURGE - limpia el cache del regex
    # re.purge()


