# https://coderbyte.com/editor/Min%20Window%20Substring:Python3
# Subcadena de ventana mínima. Haga que la función MinWindowSubstring(strArr) tome la matriz de cadenas almacenada en strArr, que contendrá solo dos cadenas, siendo el primer parámetro la cadena N y el segundo parámetro una cadena K de algunos caracteres, y su objetivo es determinar el más pequeño subcadena de N que contiene todos los caracteres en K. 
# Por ejemplo: si strArr es ["aaabaaddae", "aed"] entonces la subcadena más pequeña de N que contiene los caracteres a, e y d es "dae" ubicada al final de la cuerda Entonces, para este ejemplo, su programa debería devolver la cadena dae.
# Otro ejemplo: si strArr es ["aabdccdbcacd", "aad"], entonces la subcadena más pequeña de N que contiene todos los caracteres en K es "aabd", que se encuentra al principio de la cadena. Ambos parámetros serán cadenas con una longitud de 1 a 50 caracteres y todos los caracteres de K existirán en algún lugar de la cadena N. Ambas cadenas solo contendrán caracteres alfabéticos en minúsculas.

def MinWindowSubstring(strArr):
  size_counter = 0
  counter = 0
  range_ev = strArr[1]
  str_ev = strArr[0]
  ev_size = len(range_ev)
  
  while ev_size <= len(str_ev):
    ev_size = len(range_ev)+size_counter

    for i in range (0, len(str_ev)-ev_size+1):
        sub_str_ev = str_ev[i:i+ev_size]
        counter = compare(sub_str_ev, range_ev,counter)
        if counter >= len(set(range_ev)):
            return sub_str_ev
        else:        
            continue
    size_counter +=1       

def compare(sub_str_ev, range_ev,counter):
    import collections
    dict_b = collections.Counter(range_ev)
    counter = 0

    for i in dict_b:
        if dict_b[i] <= sub_str_ev.count(i):
            counter+=1
    return counter
    
# Test en consola // Test cases
print(MinWindowSubstring(["aaffhkksemckelloe", "fhea"]))
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
