import sys
import tracemalloc

print("=== Часть 1. Размеры объектов ===")
numbers = list(range(10))

print("Пустой список:", sys.getsizeof([]))
print("Список из 10 чисел:", sys.getsizeof(numbers))
print("Кортеж из 10 чисел:", sys.getsizeof(tuple(numbers)))
print("Строка из 10 символов:", sys.getsizeof("abcdefghij"))
print("Целое число:", sys.getsizeof(42))
print("None:", sys.getsizeof(None))

print()
print("=== Часть 2. Рост списка ===")
growing = []
last_size = sys.getsizeof(growing)
print(f"длина {len(growing)}: {last_size} байт")

for i in range(100):
    growing.append(i)
    size = sys.getsizeof(growing)
    if size != last_size:
        print(f"длина {len(growing)}: {size} байт")
        last_size = size


print()
print("=== Часть 3. tracemalloc ===")

tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"list(range(100_000)): текущий {current / 1024:.1f} КБ, пиковый {peak / 1024:.1f} КБ")

tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"range(100_000): текущий {current / 1024:.1f} КБ, пиковый {peak / 1024:.1f} КБ")