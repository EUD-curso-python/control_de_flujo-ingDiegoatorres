"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
i = 1
naturales = list()
while i <= 100:
  naturales.append(i)
  i = i+1

"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
acumulado = list()
for i in range (1,51,1):  
  if i > 1:
    acumulado.append(acumulado[i-2] + ' ' + str(i))
  else:
    acumulado.append(str(i))

"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""

suma100 = 0
for i in range(1,101,1):
  suma100+=i

"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
tabla100 = ''
for i in range(1,11,1):
  tabla100 = tabla100 + ','if (i>1) else tabla100      
  tabla100 += str (134 * i) 

"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores o iguales a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]
multiplos3 = 0
for numero in (lista1):
  if numero >= 300:
    break
  if numero % 3 == 0:
    multiplos3+=1
    

"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""
regresivo50 = list()

for veces in range (1,51,1):
  salida = ''
  for numero in range (51-veces,0,-1):        
    salida += str(numero) + ('' if (numero == 1) else ' ' ) 
  regresivo50.append(salida)

"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
invertido = list()
i = 0;
for obj in lista2:
  if i > 0:
    invertido.insert(0, obj)
  else:
    invertido.append(obj)
  i+=1

"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""
def primo(numero):
  for i in range(2,int(numero/2)+1,1):
    if numero % i == 0:
      return False
  return True

primos = list()
for numero in range(37,301,1):
  if (primo(numero)):
    primos.append(numero)

"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
anterior1 = 0
anterior2 = 1
fibonacci = list()
for numero in range (1,61,1):
  fibonacci.append(anterior1)
  pivot = anterior1
  anterior1 = anterior2
  anterior2 = pivot + anterior2

"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""
factorial =1 
for i in range (30,1,-1):
  factorial*=i

"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]

pares = list()
for i in range(0,81,2):
  pares.append(lista3[i]);

"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""
cubos = list()
for i in range(1,101,1):
  cubos.append(i * i * i)

"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""
suma_2s = 0;
for i in range(1,11,1):  
  for j in range(0,i,1):
    suma_2s += (10**(j))*2          

"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""
patron = ''
caracteres = '*'
for i in range(0,30,1):  
  patron+= caracteres  +'\n'
  caracteres+= '*'

patron += patron[len(patron)-33::-1]