"""1.Comparar 2 números
Crear dues variables i comparar-les indicant quina és més gran, quina és més petita o si son iguals.
"""
def ejercicio1(num1,num2):
    if(num1 > num2):
        print("El número " + str(num1) + " es más grande que el número " + str(num2))
    elif (num1 < num2):
        print("El número " + str(num2) + " es más grande que el número " + str(num1))
    else:
        print("El número " + str(num1) + " y el número " + str(num2) + " son iguales")

""" Dia de la setmana
Crear un arxiu nou per a que retorni per pantalla la resposta adeqüada. Crear 1 variable per dia de la setmana. 
Exemple: dia_setmana = “dilluns” Si dia_setmana és dilluns, haurà de sortir un print indicant 
“Avui és dilluns”. Si dia_setmana és dimarts, haurà de sortir per pantalla el text Avui és dimarts, etc. 
Per tant, caldrà utilitzar l’expressió if de manera que si la variable dia_setmana es modifica indiqui el 
dia adeqüat."""
def ejercicio2(dia_setmana):
    dia_setmana = dia_setmana.lower()
    dias = ["dilluns", "dimarts", "dimecres", "dijous", "divendres","dissabte","diumenge"]
    for dia in dias:
        if dia == dia_setmana:
            print("Avui es " + dia_setmana)

"""En aquest exercici caldrà modificar la nota en número i mostrar-la en text. 
Es crearà una variable on es guardarà la nota numèrica i amb condicionals es mirarà la nota i 
segons la nota numèrica sortirà per pantalla la nota (S - suspès, A - aprovat, N - notable, E - excel·lent) """
def ejercicio3(nota):
    if nota > -1 and nota < 5:
        print("S - suspès")
    elif nota >= 5 and nota <= 6.5:
        print("A - aprovat")
    elif nota >= 6.6 and nota <= 8:
        print("N - notable")
    elif  nota >= 8 and nota <= 10:
        print("E - excel·lent")
    else:
        print("nota inválida. Introduzca un número entre 1 y 10") 

"""Aplicar IVA segons el salari
En aquest exercici, s’aplicarà un IVA (0, 10, 21) segons el salari que s’indiqui.
Crear una variable de nom salari. Si el salari és menor de 15.000, s’aplica un 0% d’IVA. Si el 
salari és menor de 30.000 s’aplica un 10% de l’iva. Si el salari és menor a 60.000 s’aplica un IVA del 21%.

Exemple càlcul si el salari son 5000 => 5.000 * 0/100
"""
def ejercicio4(salario):
    if salario >=15000 and salario < 30000:
        salario -=  salario * 0.1
    elif salario >= 30000:
        salario -=  salario * 0.21
    print("Su salario con el IVA incluido es " + str(salario))


print("EJERCICIO 1")
print("Inserte el primer número: ")
num1 = int(input())
print("Inserte el segundo número: ")
num2 = int(input())
ejercicio1(num1,num2)


print("\nEJERCICIO 2")
print("Inserte el día de la semana: ")
dia_setmana = input()
ejercicio2(dia_setmana)

print("\nEJERCICIO 3")
print("Inserte la nota: ")
nota = float(input())
ejercicio3(nota)


print("\nEJERCICIO 4")
print("Inserte su salario: ")
salario = float(input())
ejercicio4(salario)




