import datetime
import functools


## decorator
def log(func):
    @functools.wraps(func)
    def wrap(*args, **kw):
        print("i am a log decorator")
        return func(*args, **kw)

    return wrap


@log
def now():
    return str(datetime.datetime.now())


print(now(), now.__name__)
