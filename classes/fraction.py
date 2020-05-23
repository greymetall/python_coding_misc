# -*- coding: utf-8 -*-

# Программа для операций с обыкновенными дробями: сложение, вычитание, умножение, перевод в десятичную дробь (с
# плавающей точной), скоращение дробей, выделение целой части и поиск НОД


class Fraction:
    """Обыкновенные дроби и операции с ними"""

    def __init__(self, a, b):
        self.num, self.den = int(a), int(b)
        if self.den == 0:
            self.num, self.reduced_num = 0, 0
        elif self.den < 0:
            self.den, self.num = abs(self.den), -self.num
        else:
            # self.int = abs(self.num) // abs(self.den)
            # self.reduced_num = abs(self.num) % abs(self.den)
            # if self.reduced_num == 0:
            #     self.res = -self.int if self.negative else self.int
            # if abs(self.num) == abs(self.den):
            #     self.res = -1 if self.negative else 1
            # if self.num == 0:
            #     self.res = 0
            pass

    def gcd(self, num, den):
        num = abs(num)
        while num % den:
            num, den = den, num % den
        return den
        # for com_factor in range(abs(self.num) if abs(self.num) < abs(self.den) else abs(self.den), 1, -1):
        #     if self.reduced_num % com_factor == 0 and self.den % com_factor == 0:
        #         self.reduced_num //= com_factor
        #         self.den //= com_factor if self.den > 0 else -(abs(self.den) // com_factor)
        #         self.num //= com_factor if self.num > 0 else -(abs(self.num) // com_factor)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(a=other * self.den, b=self.den)
        if abs(self.den) == abs(other.den):
            sum_den = self.den
            sum_num = self.num + other.num
        else:
            sum_den = self.den * other.den
            sum_num = self.num * other.den + other.num * self.den
        return Fraction(a=sum_num, b=sum_den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(a=other * self.den, b=self.den)
        if abs(self.den) == abs(other.den):
            sub_den = self.den
            sub_num = self.num - other.num
        else:
            sub_den = self.den * other.den
            sub_num = self.num * other.den - other.num * self.den
        return Fraction(a=sub_num, b=sub_den)

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        if isinstance(other, int):
            mul_den = self.den
            mul_num = self.num * other
        else:
            mul_den = self.den * other.den
            mul_num = self.num * other.num
        return Fraction(a=mul_num, b=mul_den)

    def __rmul__(self, other):
        return self * other

    def __int__(self):
        if 0 <= abs(self.num) < abs(self.den):
            return 0
        elif self.den == 0:
            print('Error')
            return 0
        elif abs(self.num) > abs(self.den):
            integer = abs(self.num) // abs(self.den)
            return integer if self.num > 0 else -integer
        elif abs(self.num) == abs(self.den):
            return 1 if self.num > 0 else -1
        else:
            pass

    def __float__(self):
        if self.den == 0:
            print('Error')
            return 0.0
        else:
            return self.num / self.den

    def __str__(self) -> str:
        gcd = self.gcd(self.num, self.den)
        self.num, self.den = self.num // gcd, self.den // gcd
        integer = self.num // self.den if self.num >= 0 else -(abs(self.num) // self.den)
        reduced_num = self.num % self.den if self.num >= 0 else -(abs(self.num) % self.den)
        if 0 < abs(self.num) < abs(self.den):
            return f"{reduced_num}{chr(0x2044)}{self.den}"
        elif abs(self.num) > abs(self.den):
            return f"{integer} {abs(reduced_num)}{chr(0x2044)}{self.den}" if reduced_num else str(integer)
        elif abs(self.num) == abs(self.den):
            return str(1) if self.num > 0 else str(-1)
        elif self.num == 0:
            return str(0)
        elif self.den == 0:
            return "Error"
        else:
            pass

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"


class OperationsOnFraction(Fraction):
    """Операции с обыкновенными дробями"""

    def getint(self):
        return super().__int__()

    def getfloat(self):
        return super().__float__()


fraction1 = Fraction(-8, 6)
fraction2 = Fraction(-3, 6)
sum_fraction1 = fraction1 + fraction2
sum_fraction2 = fraction1 + 2
sum_fraction3 = 3 + fraction1
sub_fraction1 = fraction1 - fraction2
sub_fraction2 = fraction2 - fraction1
sub_fraction3 = fraction1 - 1
sub_fraction4 = 4 - fraction2
mul_fraction1 = fraction1 * fraction2
mul_fraction2 = fraction1 * 2
mul_fraction3 = 3 * fraction2
int_fraction = int(fraction1)
float_fraction = float(fraction2)
print(f'{fraction1} + {fraction2} = {fraction1 + fraction2}')
fraction3 = OperationsOnFraction(-8, 6)
print(fraction3.getint())
print(fraction3.getfloat())
print(fraction3)
