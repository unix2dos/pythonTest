import os

print(os.name)
print(os.uname())
# print(os.environ)

# print(os.path.abspath("."))
# print(os.path.join("liuwei", "levon"))
# os.mkdir("testDir")

a = [x for x in os.listdir(".") if os.path.isdir(x)]
print(a)

b = [x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == ".py"]
print(b)
