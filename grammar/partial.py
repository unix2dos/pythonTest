import functools

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
# 调用这个新函数会更简单。
# python3

# 下面等价
int2 = functools.partial(int, base=2)
print(int2('10010'))
# ===========================#
kw = {'base': 2}
print(int('10010', **kw))

# ********************************
# 下面等价
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
# ===========================#
args = (10, 5, 6, 7)
print(max(*args))
