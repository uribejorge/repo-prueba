
#While 1

alumnos_notas ={}  #Diccionario

while True:

    nombre= input("Nombre del alumno (o salir para terminar):")

    if nombre.lower() == "salir":  #salir del bucle
        break
    while True:
        try: 
            nota = float(input(f"Introduce la nota de {nombre}:"))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe de estar entre 0 y 10. Intente de nuevo")
        except ValueError:
                print("Ingrese numero valido ")
    
    alumnos_notas[nombre] = nota

print("\n Diccionario de alumnos y notas")
for alumno, nota in alumnos_notas.items():
    print(f"{alumno}: {nota}")


#------------------------------------------------------------------------------------------------------------------


# While 2.


import random

def adivinidar_numero():
    numero_secreto = random.randint(1,100) # COn este metodo se generea un número aleatorio
    intentos_restantes = 8

    print("¡Bienevenidos al juego adivina el número!")
    print("Tienes 7 intentos para adivinar un número entre 1 y 100.")


    while intentos_restantes> 0:   # Bucles que se ejecutan mientras haya intentos restantes
        try:
            intento = int(input("Ingrese su número : "))
        except ValueError:
            print("Por favor, ingrse número valido.")
            continue
    
        if intento < numero_secreto:
            print("El número es mayor.")

        elif intento > numero_secreto:
            print("El número es menor.")

        else:
            print(f"¡Felicidades Cabrón! Adivinaste el número {numero_secreto}.")
            break

    intentos_restantes -= 1
    print(f"Te quedan {intentos_restantes} intentos.")

    if intentos_restantes == 0:
        print(f"Se te acabron los intentos pendejo.. jjajajajaja, El número secreto era {numero_secreto}.")

# Ejecutar el juego
adivinidar_numero()


#------------------------------------------------------------------------------------------------------------------

 # While 3.


def contar_vocales(frase):

    indice = 0              # Aqui el indice de contador de vocales
    contador_vocales = 0
    vocales = "aeiouAEIOU" 

    while indice < len(frase):  # Bucle para recorrer la frase
        
        if frase[indice] in vocales:
            contador_vocales += 1
        indice += 1
    
    return contador_vocales

frase_usuario = input("Cual es tú frase Putito : ")

cantidad_vocales = contar_vocales(frase_usuario)

print(f"La frase contiene {cantidad_vocales} vocales.")


#------------------------------------------------------------------------------------------------------------------

# While 4.

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def calculadora():
    while True:
        print("Selecione una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplpicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Seleccione número (1,2,3,4,5):")

        if opcion =="5":
            print("Esta saliendo de la calculadora")
            break

        if opcion in ["1","2","3","4"]:
            numero1 = float(input("Ingrese numero 1: "))
            numero2 = float(input("Ingrese numero 2: "))

        if opcion == "1":
            print("La Suma es:", suma(numero1, numero2))  

        elif opcion =="2":
            print("La Resta es:", resta(numero1, numero2))
         
        elif opcion =="3":
            print("La Multiplicación es:", multiplicacion(numero1, numero2))
            
        elif opcion =="4":
            print("La División es:", division(numero1, numero2))
            
        else:   #si no nos da
            print("Opción no valida,intente de nuevo ")
            break

calculadora()


#------------------------------------------------------------------------------------------------------------------

#While 5.


def lista_numeros_pares():
    contador = 1
    lista_par =[]

    while contador <= 100:

        if contador % 2 == 0:
            lista_par.append(contador)

        contador += 1

    return lista_par

numeros_pares = lista_numeros_pares()

print(f"LIsta de números pares del 1 al 100:  {numeros_pares}")

