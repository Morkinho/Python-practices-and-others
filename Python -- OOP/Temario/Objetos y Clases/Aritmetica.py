class aritmetica:
    """
    Clase Aritmetica para realizar las operaciones
    sumar, restar, etc.
    
    """
    def __init__(self, operandoA, operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB
    
    def multi(self):
        return self.operandoA * self.operandoB

    def div(self):
        return self.operandoA / self.operandoB

    def resdiv(self):
        return self.operandoA % self.operandoB

PrimerNumero = int(input('Coloca el primer numero: '))
SegundoNumero = int(input('Coloca el segundo numero: '))

aritmetica1 = aritmetica(PrimerNumero, SegundoNumero)

print(f'La suma entre {PrimerNumero} y {SegundoNumero} es: ')
print(aritmetica1.sumar())

print(f'La resta entre {PrimerNumero}y{SegundoNumero} es: ')
print(aritmetica1.restar())

print(f'La multiplicación entre {PrimerNumero} y {SegundoNumero} es: ')
print(aritmetica1.multi())

print(f'La division entre {PrimerNumero} y {SegundoNumero} es: ')
print(aritmetica1.div())
