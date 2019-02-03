class Calculations:
    def __init__(self):
        self.mathematics = []

    def multiplication(self):
        return [i*3 for i in self.mathematics]

    def subtraction(self):
        return [i-5 for i in self.mathematics]

    def division(self, x):
        return [i/x for i in self.mathematics if x!=0]


calculation = Calculations()
calculation.mathematics.append(1)
calculation.mathematics.append(3)
calculation.mathematics.append(5)
calculation.mathematics.append(7)
calculation.mathematics.append(9)
calculation.mathematics.append(11)

print (calculation.multiplication())
print (calculation.subtraction())
print (calculation.division(1))
