class Layer:
    def __init__(self, number, name, description):
        self.number = number
        self.name = name
        self.description = description
    
    def getNumber(self):
        return self.number
    
    def getName(self):
        return self.name
        
    def getDescription(self):
        return self.description