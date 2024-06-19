import math
from fibonacci import Fib

myFib = iter(Fib())

fibList = list(myFib)

print(fibList)
print(max(fibList))
print(min(fibList))
print([str.format('{:,.2f}', pow(x, 5)) for x in fibList if x % 2 == 0])
print([str.format('{:,.2f}', math.sqrt(x)) for x in fibList])
