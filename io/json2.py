import json

d = dict(name="levon", age=20)
print(json.dumps(d))


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.Age = age


s = Student("levon", 26)
str = json.dumps(s, default=lambda obj: obj.__dict__)
print("1", str)

print("2", json.loads(str)["name"])
