student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[:1],student[-1:])
print(student[:4],student[-8:])
print(student.upper(),student.lower())
print(student[0] + "." + student[5] + ".")
print(course[::-1])

percent = completed / total * 100
result_percent = "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
result_format = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent)
result_fstring = f"{student} — {course}: {completed}/{total} ({percent:.1f}%)"
print(result_percent)
print(result_format)
print(result_fstring)

symbol = "Я"
code = ord(symbol)
encoded = symbol.encode("utf-8")
print("Символ:", symbol)
print("Кодовая позиция:", code)
print("Восстановленный символ:", chr(code))
print("UTF-8:", encoded)
print("Длина в байтах:", len(encoded))
print("Длина в символах:", len(symbol))

# student[0] = "а"