# Task:
# Implement a Complex class in Python to perform arithmetic operations (+, -, *, /)
# and modulus (|z|) between two complex numbers. The output must be formatted
# to two decimal places and printed in the form: a±bi.

# Input:
# Two lines of input:
# - Each line contains two space-separated numbers: real and imaginary parts of a complex number.

# Output:
# Print the result of:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulus of the first number
# 6. Modulus of the second number
# Each result on a new line in the format: x.xx±y.yyi

# Notes:
# - Implement special methods: __add__, __sub__, __mul__, __truediv__, __abs__, __str__
# - Handle formatting to ensure correct display of signs and zero values
# - Use object-oriented programming concepts like operator overloading



import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        
        real_part = self.real + no.real
        imag_part = self.imaginary + no.imaginary
        return Complex(real_part,imag_part)
        
    def __sub__(self, no):
        
        real_part = self.real - no.real
        imag_part = self.imaginary - no.imaginary
        return Complex(real_part,imag_part)
    
    def __mul__(self, no):
        
        real_part = self.real * no.real - self.imaginary*no.imaginary
        imag_part = self.real * no.imaginary + self.imaginary*no.real
        return Complex(real_part,imag_part)

    def __truediv__(self, no):
        
        
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / (no.real**2 + no.imaginary**2)
        imag_part = (self.imaginary * no.real - self.real * no.imaginary) / (no.real**2 + no.imaginary**2)
        return Complex(real_part, imag_part)
    
    def mod(self):
        
         real_part=(self.real**2 +self.imaginary**2)**0.5
         return Complex(real_part,0)
         
        

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


# Example:
# Input:
# 2 1
# 5 6
#
# Output:
# 7.00+7.00i
# -3.00-5.00i
# 4.00+17.00i
# 0.26-0.11i
# 2.24+0.00i
# 7.81+0.00i
