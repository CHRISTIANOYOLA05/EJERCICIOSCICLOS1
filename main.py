#ejercicios ciclos 

ejercicios = 0




while ejercicios < 99:
  
  ejercicios = int(input("ingrese el numero de ejercicio que quieres realizar: "))
  # Imprimir todos los múltiplos de 3 que hay entre 1 y 100.
  if ejercicios == 1: 
    for _ in range (3, 100, 3):
      print(_)
  # Imprimir los números impares entre 0 y 100.
  elif ejercicios == 2:
    for _ in range (1, 101, 2):
      print(_)

  # Imprimir los números pares entre 0 y 100.
  elif ejercicios == 3:
    
    for _ in range (2, 101, 2):
      print(_)
  # Escribir un programa en Python que imprima por pantalla los números del 1 al 3.
  elif ejercicios == 4:
    for _ in range(1, 4):
      print(_)
  # Escribir un programa en Python que imprima por pantalla los números del 10 al 1.
  elif ejercicios == 5:
    for _ in range(10, 0, -1):
      print(_)
  #Escribir un programa en Python que imprima en pantalla los cuadrados de los números del 1 al 30.
  elif ejercicios == 6:
    for _ in range(1, 31):
      print(_ ** 2)
    #Escribir un programa en Python que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla.
  elif ejercicios == 7:
    suma = 0
    for _ in range(1, 101):
      suma += _ ** 2

    print(suma)
  #Escribir un programa en Python que lea un número entero desde teclado y realice la suma de los cien números siguientes, mostrando el resultado en pantalla.
  elif ejercicios == 8:
    numero = int(input("Ingrese un número entero: "))
    suma = 0
    for _ in range(numero + 1, numero + 101):
      suma += _
  
    print(suma)
     
  # Halle el número factorial de un número ingresado por el usuario.
  elif ejercicios == 9:

    numero = int(input("Ingrese un número: "))
    factorial = 1
  
    for _ in range(1, numero + 1):
      factorial *= _
  
    print("El factorial de", numero, "es", factorial)
  #Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y lasconvierta a grados Celsius. El programa finalizará cuando lea un valor de temperaturaigual a 999. La fórmula c = 5/9(f -32)
  elif ejercicios == 10:
    
    while True:
      temperatura = float(input("Ingrese una temperatura en grados Fahrenheit (999 para finalizar): "))
      if temperatura == 999:
        break
    celsius = (temperatura - 32) * 5/9
    print("La temperatura en grados Celsius es:", celsius)
     
   #Programa para imprimir los números primos hasta un número ingresado por el usuario:
  
  elif ejercicios == 11:
    numero = int(input("Ingrese un número: "))

    print("Números primos hasta", numero, ":")
    for numero in range(2, numero + 1):
      es_primo = True
      for _ in range(2, int(numero ** 0.5) + 1):
        if numero % _ == 0:
          es_primo = False
          break
        if es_primo:
          print(numero, end=" ")

  #Programa para mostrar la tabla de multiplicar solicitada por el usuario:
    
  elif ejercicios == 12:
  
    numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
  
    print("Tabla de multiplicar del", numero, ":")
    for i in range(1, 11):
      resultado = numero * i
      print(numero, "x", i, "=", resultado)


  # Programa para calcular el promedio de un conjunto de números positivos:

  elif ejercicios == 13:

    numeros = []
    while True:
      numero = float(input("Ingrese un número positivo (ingrese un número negativo para finalizar): "))
      if numero < 0:
          break
      numeros.append(numero)
  
    if len(numeros) > 0:
      promedio = sum(numeros) / len(numeros)
      print("El promedio de los números ingresados es:", promedio)
    else:
      print("No se ingresaron números positivos.")
    
#Programa para generar y mostrar todos los números comprendidos entre dos números en secuencia ascendente:

  elif ejercicios == 14:
  
  
    numero1 = int(input("Ingrese el primer número (menor): "))
    numero2 = int(input("Ingrese el segundo número (mayor): "))
    
    print("Números comprendidos entre", numero1, "y", numero2, "en secuencia ascendente:")
    for num in range(numero1 + 1, numero2):
        print(num, end=" ")
  #Realizar un algoritmo que muestre los valores de todas las piezas del dominó de formaordenada: 0-0 0-1 1-1 ...
  elif ejercicios == 15:
    print("Valores de las piezas del dominó de forma ordenada:")
    for i in range(7):
      for j in range(i, 7):
          print(i, "-", j)
  