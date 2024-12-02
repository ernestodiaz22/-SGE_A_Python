class colibri:
    #Constructor
    def __init__(self, color,edad,tamano,peso,sexo):
        self.color = color
        self.edad = edad
        self.tamano = tamano
        self.peso = peso
        self.sexo = sexo
    #setters
    def setColor(self, newColor):
        self.color = newColor
    def setEdad(self, newEdad):
        self.edad = newEdad
    def setTamano(self, newTamano):
        self.tamano = newTamano
    def setPeso(self, newPeso):
        self.peso = newPeso
    def setSexo(self, newSexo):
        self.sexo = newSexo
    #getters
    def getColor(self):
        return self.color
    def getEdad(self):
        return self.edad
    def getTamano(self):
        return self.tamano
    def getPeso(self):
        return self.peso
    def getSexo(self):
        return self.sexo
   