"""Отчёт о потреблении памяти: список против range."""

import sys
import tracemalloc

# Часть 1: размеры отдельных объектов
objects = [
    ("пустой список", 0, []),
    ("список из 10 чисел", 10, list(range(10))),
    ("кортеж из 10 чисел", 10, tuple(range(10))),
    ("строка из 10 символов", 10, "abcdefghij"),
    ("целое число", "-", 42),
    ("None", "-", None),
]

sizes = []
for name, count, obj in objects:
    sizes.append({"name": name, "count": count, "size": sys.getsizeof(obj)})

results = []

# Сценарий 1: список
tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({"name": "list(range(100_000))", "count": len(numbers),
                "size": sys.getsizeof(numbers), "current": current, "peak": peak})

# Сценарий 2: range
tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({"name": "range(100_000)", "count": len(numbers),
                "size": sys.getsizeof(numbers), "current": current, "peak": peak})

# Вывод
print()
print("=== Размеры объектов ===")
for row in sizes:
    print(f"{row['name']}: элементов {row['count']}, размер {row['size']} байт")

print()
print("=== Список против range ===")
for row in results:
    print()
    print("Сценарий:", row["name"])
    print("Элементов:", row["count"])
    print("Размер внешнего объекта:", row["size"], "байт")
    print(f"Текущий объём: {row['current'] / 1024:.1f} КБ")
    print(f"Пиковый объём: {row['peak'] / 1024:.1f} КБ")

print()
list_peak = results[0]["peak"]
range_peak = results[1]["peak"]
if range_peak == 0:
    print("Отношение пиков: не определено, range не выделил памяти")
else:
    print(f"Отношение пиков list / range: {list_peak / range_peak:.0f}")