# Enunciado: Encontrar cuántos triángulos rectángulos hay en un conjunto de puntos. Recuerde que un triángulo rectángulo es un triángulo que tiene un ángulo recto. 
# Argumentos: Array de String // Condiciones de la entrada:
#   *Todos los puntos dados por (x, y) son coordenadas enteras con números no negativos menores o iguales a 1000. No habrá dos puntos repetidos en la entrada. 
#   *Todos los triángulos rectángulos que se deben contar son los que tienen dos lados paralelos a cada uno de los ejes. 
#   *Dos triángulos son considerados iguales si los tres puntos que lo forman son iguales.
#   *Habrá máximo 20 puntos en la entrada.

#Valor a imprimir: Cantidad de triángulos rectángulos encontrados. Todos los triángulos rectángulos que se deben contar son los que tienen un lado paralelo al eje x y otro lado paralelo al eje y. Cualquier triángulo que no cumpla eso no se debe contar. Por ejemplo: ["0,0","2,2","0,4"] 


def r2rightTriangle(strArr):
  newArr = sorted(set(strArr))
  newArr = list(map(lambda x: x.split(","),newArr))
  counter = 0

  for i in range (len(newArr)):
    for j in range (len(newArr)):
      if newArr[i] == newArr[j]:
        continue
      if newArr[i][0] == newArr[j][0]:
        for k in range (len(newArr)):
            if newArr[i] == newArr[k] or newArr[k] == newArr[j]:
              continue
            elif newArr[i][1] == newArr[k][1]:
              counter +=1
 
  return counter

# Pruebas en consola / test cases
print(r2rightTriangle(["0,0","0,3","0,6","3,0","6,0"])) #4
print(r2rightTriangle(["2,0", "2,2", "2,4","2,10", "2,12", "1000,14","2,14","3,14","4,14","5,14"])) #20
print(r2rightTriangle(["999,0", "998,2", "1,0", "1,2", "1,4" ,"1,10", "1,12", "1000,14","2,14","3,14","4,14","5,14"])) # 8
print(r2rightTriangle(["1,0", "1,2", "1,4","1,10", "1,12", "1,14"])) # 0

