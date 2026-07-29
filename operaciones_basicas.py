class OperacionesBasicas:
    def __init__(self):
        self.num1=0.0
        self.num2=0.0
        self.resultado=0.0
    def suma(self):
        self.resultado=self.num1+self.num2
        return self.resultado
    def resta(self):
        self.resultado=self.num1-self.num2
        return self.resultado
    def multiplicacion(self):
        self.resultado=self.num1*self.num2
        return self.resultado
    def division(self):
        if self.num2==0:
            return"ERROR: No se puede dividir entre cero"
        self.resultado=self.num1/self.num2
        return self.resultado