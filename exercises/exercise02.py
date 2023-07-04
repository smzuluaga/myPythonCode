# Antiguamente las tarjetas de identificación colombianas estaban conformadas por números de 11 dígitos, de los cuales los primeros seis consistían en la fecha de nacimiento de la persona. Diseñe e implemente una función en javascript que recibe como argumento un número entero positivo de 11 dígitos y extrae la fecha de nacimiento y retorna una cadena de texto con la fecha en el formato dado en los ejemplos. Puede asumir que el número recibido por la función siempre será entero positivo, de 11 dígitos y no tendrá ceros a la izquierda.
#Ejemplos: Prueba1P4(86021951120)=”Nacimiento el 19 de febrero de 1986” // Prueba1P4(99120199999)=”Nacimiento el 1 de diciembre de 1999”

def identification(id):
    year = f'19{str(id)[0:2]}'
    months = ['cero', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    month = months[int(str(id)[2:4])]
    day = int(str(id)[4:6])
    
    return f'Nacimiento el {day} de {month} de {year}'


print(identification(86021951120))
print(identification(99120199999))

