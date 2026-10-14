a = 1000
b = a
c = int("1000")

# Прогноз:
# a == b: True
# a is b: True
# a == c: True
# a is c: False

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

c = None
print("c is None:", c is None)

# Прогноз:
# first == second: True
# first is second: False

first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)