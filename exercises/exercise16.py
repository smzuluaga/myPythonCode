#Retorna el elemento de un array que solo tiene una ocurrencia, los demás elementos de la lista tendrán más de 1 ocurrencia.

def first_non_repeating_letter(s):
    s_compare = s.lower()
    
    for i in range(0,len(s)):
        if s_compare.count(s_compare[i]) == 1:
            return s[i]
    return ''


# Pruebas en consola / Test cases        
string = '~><#~><'
print(first_non_repeating_letter(string))


