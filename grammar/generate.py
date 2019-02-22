g = (x for x in range(1, 11))

for n in g:
    print(n)


# 另外一种形式 python3
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

def odd():
    yield 1
    yield 3
    yield 5


for n in odd():
    print(n)

print(type((x for x in range(1, 11))))
print(type([x for x in range(1, 11)]))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。


# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
