

class trasacao:
    def __init__(self, tipo, data, fonte, valor):

        self.tipo = tipo
        self.data = data
        self.fonte = fonte
        self.valor = valor

    def to_dict(self):
        
        dicionario = {}

        dicionario["tipo"] = self.tipo
        dicionario["data"] = self.data
        dicionario["fonte"] = self.fonte
        dicionario["valor"] = self.valor

        return dicionario 

class entry(trasacao):
    def __init__(self, tipo, data, fonte, valor):
        super().__init__(tipo, data, fonte, valor)

class exit(trasacao):
    def __init__(self, tipo, data, fonte, valor, metodo, status):
        super().__init__(tipo, data, fonte, valor)
        self.metodo = metodo
        self.status = status

    def to_dict(self):
        
        dicionario = super().to_dict()

        dicionario["metodo"] = self.metodo
        dicionario["status"] = self.status

        return dicionario
    
    

