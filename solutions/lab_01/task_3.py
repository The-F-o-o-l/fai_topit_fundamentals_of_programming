import math

# эксперимент А
# прогноз:
# x + y: 22, int
# x - y: 12, int
# x * y: 85, int
# x / y: 3.4, float
# x // y: 3, int
# x % y: 2, int
# x ** y: 1419857, int

x = 17
y = 5

result = 0.1 + 0.2
print("result =", result)
print("result == 0.3:", result == 0.3)
print("result - 0.3 =", result - 0.3)
print("math.isclose(result, 0.3):", math.isclose(result, 0.3))

# эксперимент В
# прогноз: число выведется целиком

print("2**1000 =", 2**1000)

# эксперимент C
# прогноз:
# result: 0.3
# result == 0.3: True
# result - 0.3: 0.0
# math.isclose(result, 0.3): True

print("x + y =", x + y, type(x + y))
print("x - y =", x - y, type(x - y))
print("x * y =", x * y, type(x * y))
print("x / y =", x / y, type(x / y))
print("x // y =", x // y, type(x // y))
print("x % y =", x % y, type(x % y))
print("x ** y =", x ** y, type(x ** y))

# эксперимент D
# прогноз:
# int("42"): 42
# float(3.14): 3.14 + небольшая погрешность
# str(2026): "2026"
# bool(0): False/0
# bool(-1): -
# bool(""): -
# bool("False"): False/0
# complex(2,-3): 2 - 3i

print('int("42") =', int("42"), type(int("42")))
print('float("3.14") =', float("3.14"), type(float("3.14")))
print("str(2026) =", str(2026), type(str(2026)))
print("bool(0) =", bool(0), type(bool(0)))
print("bool(-1) =", bool(-1), type(bool(-1)))
print('bool("") =', bool(""), type(bool("")))
print('bool("False") =', bool("False"), type(bool("False")))

z = complex(2, -3)
print("complex(2, -3) =", z, type(z))
print("действительная часть:", z.real)
print("мнимая часть:", z.imag)