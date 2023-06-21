# Encontrar la subcadena palíndroma más larga 
# Argumentos: Una cadena de texto.
# Condiciones de la entrada:
#   Tendrá al menos un símbolo y estará compuesto sólo por espacios, puntos y letras del alfabeto inglés.
#   Para este problema puede ignorar los espacios, mayúsculas/minúsculas y los puntos. Ver los ejemplos para más claridad.
# Ejemplo de entrada: “xxAbc cb a x y z” ==> output = 8
# Ejemplo de entrada: “Una frase con una palindroma Anita lava la tina muy muy larga” ==> output = 15

def r2longestPalindrome(strParam):
  str_amen = strParam.lower().replace(' ', '')
  max_len_ev = len(str_amen)
 
  if str_amen == str_amen[::-1]:
    return max_len_ev
  else:
    while True: 
      max_len_ev-= 1
      for i in range(0,len(str_amen)-max_len_ev+1):
        ev_range = str_amen[i:i+max_len_ev]
        rev_range = ev_range[::-1]
        if ev_range == rev_range:
          return (max_len_ev)

print(r2longestPalindrome('Oso'))
print(r2longestPalindrome('Anita lava la tina'))
print(r2longestPalindrome('Radar'))
print(r2longestPalindrome('civic'))
print(r2longestPalindrome("Una frase con una palindroma Anita lava la tina muy muy larga"))
print(r2longestPalindrome("A b cde"))