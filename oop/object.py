class Student(object):
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


levon = Student("levon")
print(dir(levon))

# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'name', 'sub']

print(getattr(levon, "name"))

# levon
