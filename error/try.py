import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar("0")
    except Exception as e:
        logging.exception(e)
    finally:
        print("finally")


main()
print("END")

'''
ERROR:root:integer division or modulo by zero
Traceback (most recent call last):
  File "try.py", line 14, in main
    bar("0")
  File "try.py", line 9, in bar
    return foo(s) * 2
  File "try.py", line 5, in foo
    return 10 / int(s)
ZeroDivisionError: integer division or modulo by zero
finally
END
'''

# raise 抛出错误


# raise语句如果不带参数，就会把当前错误原样抛出


# 还可以把一种类型的错误转化成另一种类型
'''
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
'''
