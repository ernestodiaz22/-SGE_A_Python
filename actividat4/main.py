from coche import coche
from colibri import colibri

#Instancias de coche
coche1 = coche("bmw","iX M60", 200, 2000, 2)
coche2 = coche("mercedes","coupé", 120, 3000, 3)
coche3 = coche("ferrari ","testarossa", 190, 1100, 1)

#Instancias de colibrí
colibri1 = colibri("rojo",5,3.5,4.6,"macho")
colibri2 = colibri("azulado",2,2.9,4.3,"hembra")
colibri2 = colibri("verde",3,3.2,4.5,"hembra")

#obtener con getters de coche
print("OBTENER INFORMACIÓN CON 3 GETTERS DE COCHE")
print("La marca del primer coche es un " + coche1.getMarca()+ ", del modelo " + coche1.getModelo() + " y tiene " + str(coche1.getCaballos()) + " caballos de potencia\n")

#obtener con getters de colibrí
print("OBTENER INFORMACIÓN CON 4 GETTERS DE COLIBRÍ")
print("El segundo colibrí tiene el plumaje " + colibri2.getColor() + ", tiene una edad de " + str(colibri2.getEdad()) + " años, mide " + str(colibri2.getTamano()) + "cm y pesa " + str(colibri2.getPeso()) + "g\n")

#cambiar con setters de coche
print("CAMBIAR INFORMACIÓN CON 2 SETTERS DE COCHE")
print("La marca del primer coche es un " + coche1.getMarca()+ " y es del modelo " + coche1.getModelo())
coche1.setMarca("seat")
coche1.setModelo("ibiza")
print("La marca del primer coche es un " + coche1.getMarca()+ " y es del modelo " + coche1.getModelo() + "\n")
print("CAMBIAR INFORMACIÓN CON 2 SETTERS DE COLIBRÍ")
print("El segundo colibrí tiene el plumaje " + colibri2.getColor() + " y tiene una edad de " + str(colibri2.getEdad()) + " años")
colibri2.setColor("amarillo")
colibri2.setEdad(4)
print("El segundo colibrí tiene el plumaje " + colibri2.getColor() + " y tiene una edad de " + str(colibri2.getEdad()) + " años\n")


