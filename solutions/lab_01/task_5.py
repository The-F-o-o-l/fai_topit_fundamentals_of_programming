"""
Информационная карточка вычислительного эксперимента.

Программа запрашивает у пользователя данные об эксперименте, вычисляет
общую длительность запусков, комплексный коэффициент и квадрат его модуля,
выводит результаты в виде карточки.
"""


researcher = input("Имя исследователя: ")
experiment = input("Название эксперимента: ")
runs = int(input("Количество запусков: "))
run_duration = float(input("Длительность одного запуска, с: "))
real = float(input("Действительная часть коэффициента: "))
imag = float(input("Мнимая часть коэффициента: "))

total_seconds = runs * run_duration
total_minutes = total_seconds / 60
coefficient = complex(real, imag)
modulus_squared = real ** 2 + imag ** 2
has_runs = bool(runs)

total_seconds = runs * run_duration
total_minutes = total_seconds / 60
coefficient = complex(real, imag)
modulus_squared = real ** 2 + imag ** 2
has_runs = bool(runs)

line = "=" * 40
print(line)
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {modulus_squared:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print(line)
print("Типы введённых значений:", type(researcher), type(experiment), type(runs),
      type(run_duration), type(real), type(imag))