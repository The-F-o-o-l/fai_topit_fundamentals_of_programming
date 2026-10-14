import copy

a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10, 20, 30]
print(id(first), id(second))

print("first == second:", first == second)
print("first is second:", first is second)

second.append(40)
print(first, second)

# ПРАКТИЧЕСКОЕ ЗАДАНИЕ

config_a = {
    "name": "учебный проект",
    "students": ["Иван Итмо","Артём"],
    "launch_parameters": [["parameter 1", 10], ["parameter 2", 32]],
}

config_b = config_a
print("До изменения:")
print("  A:", config_a)
print("  B:", config_b)


config_b["students"].append("Ольга Нежелательная")
config_b["launch_parameters"][0][1] = 20

print("После изменения B:")
print("  A:", config_a)
print("  B:", config_b)
print("  config_a is config_b:", config_a is config_b)

## нормальное копирование

config_c = copy.deepcopy(config_a)
print("До изменения C:")
print("  A:", config_a)
print("  C:", config_c)


config_c["students"].append("Ольга Желательная")
config_c["launch_parameters"][1][1] = 64

print("После изменения C:")
print("  A:", config_a)
print("  C:", config_c)

assert config_c is not config_a
assert config_c["students"] is not config_a["students"]
assert config_c["launch_parameters"] is not config_a["launch_parameters"]
assert config_c["launch_parameters"][0] is not config_a["launch_parameters"][0]
assert "Ольга Желательная" not in config_a["students"]
assert config_a["launch_parameters"][1][1] == 32

print("Итог:")
print("  A и B - один и тот же объект, общими оказались все части конфигурации")
print("  A и C - разные объекты, независимы и словарь, и все вложенные списки")