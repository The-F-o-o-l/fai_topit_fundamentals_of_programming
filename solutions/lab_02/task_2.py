import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)


structures = {"original": original, "alias": alias, "shallow": shallow, "deep": deep}


def show(title):
    print(f"=== {title} ===")
    for name, value in structures.items():
        print(f"{name}: {value}")
    print("id внешнего списка:")
    for name, value in structures.items():
        print(f"{name}: {id(value)}")
    print("id первого вложенного списка:")
    for name, value in structures.items():
        print(f"{name}: {id(value[0])}")
    print("id первой оценки:")
    for name, value in structures.items():
        print(f"{name}: {id(value[0][1])}")
    print()


show("Исходное состояние")

original.append(["Databases", 5])
show("После original.append")

original[0][1] = 3
show("После original[0][1] = 3")

print("=== Матрицы ===")
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print("wrong_matrix:", wrong_matrix)
print("строки - один объект:", wrong_matrix[0] is wrong_matrix[1] is wrong_matrix[2])

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print("correct_matrix:", correct_matrix)
print("строки - один объект:", correct_matrix[0] is correct_matrix[1])

# прогноз
#wrong_matrix: единица появится во всех трёх строках.
#correct_matrix: только в первой строке.