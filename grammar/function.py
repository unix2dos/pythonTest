# 普通函数
def add(a, b):
    return a + b


print(3 + 4)


# 多返回值
def add2(a, b):
    return a + 1, b + 1


print(add2(3, 4))


# 可变参数
def cala(*nums):
    sum = 0
    for x in nums:
        sum += x
    return sum


print(cala(1, 2, 3))


# 关键字参数 python3

def word(name, age, **kw):
    print('name:', name, 'age:', age, "kw:", kw)


word("levon", 26, test1="string", test2=3)


# 命名关键字参数 python3
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 注意
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


# 递归
def digui(n):
    if n == 1:
        return 1
    return n * digui(n - 1)


print(digui(1))
print(digui(3))
