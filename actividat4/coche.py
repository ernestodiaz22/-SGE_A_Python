class coche:
    #Constructor
    def __init__(self, marca,modelo,caballos,kilometros,anos):
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
        self.kilometros = kilometros
        self.anos = anos
    #setters
    def setMarca(self, newMarca):
        self.marca = newMarca
    def setModelo(self, newModelo):
        self.modelo = newModelo
    def setCaballos(self, newCaballos):
        self.caballos = newCaballos
    def setKilometros(self, newKilometros):
        self.kilometros = newKilometros
    def setAnos(self, newAnos):
        self.anos = newAnos
    #getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getCaballos(self):
        return self.caballos
    def getKilometros(self):
        return self.kilometros
    def getAnos(self):
        return self.anos
   
        
    