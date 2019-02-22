import os
from collections import Iterable

d = {"key1": "value1", "key2": "value2"}
for k, v in d.items():
    print(k, v)

print(isinstance("abc", Iterable))

for k, v in enumerate(["a", "b", "c"]):
    print(k, v)

num = [x * x for x in range(1, 11)]
print(num)

word = [m + n for m in "abc" for n in "xyz"]
print(word)

files = [d for d in os.listdir(".")]
print(files)

name = ["levon", "xuanyuan", "ojbk"]
Name = [k.upper() for k in name]
print(name)
print(Name)
