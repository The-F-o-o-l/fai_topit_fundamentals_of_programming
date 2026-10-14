import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print()
print("=== Сборщик мусора ===")
print("Автоматический сборщик включён:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:")
for generation, stats in enumerate(gc.get_stats()):
    print(f"  поколение {generation}: {stats}")

print()
print("=== Удаление цикла ===")
first_id = id(first)
second_id = id(second)
print("id first:", first_id)
print("id second:", second_id)

gc.collect()

del first, second

collected = gc.collect()
print("gc.collect() собрал объектов:", collected)

print()
print("=== Сборщик выключен ===")
gc.disable()
print("Автоматический сборщик включён:", gc.isenabled())

gc.collect()

for _ in range(5):
    a = []
    b = []
    a.append(b)
    b.append(a)

del a, b

print("Объектов в поколении 0 до сборки:", gc.get_count()[0])
collected = gc.collect()
print("gc.collect() собрал объектов:", collected)

gc.enable()
print("Автоматический сборщик включён:", gc.isenabled())



print()
print("=== Граф ===")
collected_before = gc.collect()
print("Собрано до создания графа:", collected_before)

node_a = {"name": "A", "links": []}
node_b = {"name": "B", "links": []}
node_c = {"name": "C", "links": []}
node_d = {"name": "D", "links": []}

node_a["links"].append(node_b)
node_b["links"].append(node_c)
node_c["links"].append(node_a)

for node in (node_a, node_b, node_c, node_d):
    targets = [target["name"] for target in node["links"]]
    print(f"{node['name']} -> {targets}")

del node_a, node_b, node_c

collected_after = gc.collect()
print("Собрано после удаления графа:", collected_after)

assert node_d["name"] == "D"
print("Независимый узел доступен:", node_d)