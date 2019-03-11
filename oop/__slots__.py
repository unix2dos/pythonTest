class Struct(object):
    __slots__ = ("name", "age")


s = Struct()
s.name = "levon"
s.age = 26
# s.abc = "abc" // restrict
print("name = %s, age = %s" % (s.name, s.age))
