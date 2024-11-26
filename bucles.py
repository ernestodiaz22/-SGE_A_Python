def rango100and400(num):
    i=100
    rango = False
    while i <  401:
        if num == i:
            rango = True
        i+=1
    if rango:
        print(str(num) + " está entre 100 y 400") 
    else:
        print(str(num) + " no está entre 100 y 400") 

print("1.Imprimir números de l’1 al 10 (amb for i amb while): ")
print("Bucle while: ")
i = 1
while i < 11:
    print(i)
    i+=1
print("Bucle for: ")
for i in range(1,11):
    print(i)

print("\n2.Sumar els primers 10 números utilitzant for i range().")
suma = 0
for i in range(1,11):
    suma += i
print("La suma de los 10 primeros números es " + str(suma))
print("\n3.Imprimir els elements d'una llista amb for. fruits = [“poma”,”pera”,”raïm”,”plàtan”]")
fruits = ["poma","pera","raïm", "plàtan"]
for fruta in fruits:
    print(fruta)
print("\n4.Imprimir els números parells i els imparells continguts en la següent llista. Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]")
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
pares = []
impares = []
sumaPares = 0
sumaImpares = 0
for numero in num:
    if numero % 2 == 0:
        pares.append(numero)
        sumaPares += numero
    else:
        impares.append(numero)
        sumaImpares += numero
print("Los números pares de la lista son: ")
for numero in pares:
    print(numero)
print("Los números impares de la lista son: ")
for numero in impares:
    print(numero)
print("\n5.Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.")
print("La suma de los números pares es: " + str(sumaPares))
print("La suma de los números ipares es: " + str(sumaImpares))
print("\n6.Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.")
i=1
suma = 0
while i < 101:
    suma += i
    i+=1
print("La suma de los números incluidos entre el 0 y el 100 es: " + str(suma)) 
print("\n7.Amb while indicar si el número guardat a una variable està entre 100 i 400.")
rango100and400(202)
rango100and400(99)





