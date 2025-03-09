import sys
from decimal import Decimal, getcontext

x = int(input("Number of correct decimal places: "))
if x > 0:
    getcontext().prec = x + 1
else:
    print("Value must be positive")
    sys.exit()

def Fctrl(n):
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k
 
inpt = getcontext().prec + 3

def Calculate(n):
    e_num = Decimal(0)
    for i in range(0, n + 1):
        e_num += Decimal(1) / Decimal(Fctrl(i))
    return e_num

print(Calculate(inpt))
