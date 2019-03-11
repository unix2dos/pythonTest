# coding: utf-8

# 1 __init__ 构造函数
# 2 __str__  string()
# 3 __repr__
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。
# __repr__ = __str__


# 4 __iter__
# 5 __next__ #自定义迭代 for in  #python3
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


# 6 __getitem__  #取第几个元素

# 7 __getattr__ #不存在的属性

class Chain(object):
    def __init__(self, path=""):
        self.__path = path

    def __str__(self):
        return self.__path

    def __getattr__(self, item):
        return Chain("%s/%s" % (self.__path, item))


print(Chain().a.b.c.d.e)


# 8 __call__ #对象当函数调用


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __call__(self, *args, **kwargs):
        print("my name is %s" % self.__name)


s = Student("levon")
s()
