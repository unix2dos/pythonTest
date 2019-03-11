from types import MethodType


class A(object):
    pass


def setAge(self, age):
    self.age = age


a = A()
a.setAge = MethodType(setAge, a)
a.setAge(20)
print(a.age)
