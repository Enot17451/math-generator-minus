from random import *

class Number:

    def __init__(self):
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])
        self.number = randint(1, 50)

    def __str__(self)->str:
        if self.sign == "+":
            return str(self.number)
        else:
            return f"(-{self.number})"


class Question:

    def __init__(self):
        self.result = 0
        self.a = Number()
        self.b = Number()
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "-", "-", "-", "-"])
        self.calk()

    def calk(self):
        a = self.a.number
        b = self.b.number
        if self.a.sign == "-":
            a *= -1
        if self.b.sign == "-":
            b *= -1
        match self.sign:
            case "+":
                self.result = a + b
            case "-":
                self.result = a - b

    def __str__(self)->str:
        return f"{self.a} {self.sign} {self.b}                                                                                                                                                      {self.result}"

n = 50
for x in range(n):
    print(Question())
