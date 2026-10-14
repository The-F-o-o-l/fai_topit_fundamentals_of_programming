import sys
import weakref


data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print()
print("=== Слабый реестр ===")
registry = weakref.WeakValueDictionary()

first = Record()
second = Record()
temp = Record()

registry["first"] = first
registry["second"] = second
registry["third"] = temp

print("Сначала в реестре:", sorted(registry.keys()))

del temp
print("После del temp:", sorted(registry.keys()))

del second
print("После del second:", sorted(registry.keys()))