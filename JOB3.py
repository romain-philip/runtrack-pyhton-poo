class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def afficher(self):
        print(f"Le nombre1 est {self.nombre1}")
        print(f"Le nombre2 est {self.nombre2}")

    def addition(self):
      return  self.nombre1 + self.nombre2

        
        
operation = Operation()

operation.afficher()
print(operation.addition()) 