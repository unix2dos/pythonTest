from io import StringIO, BytesIO

f = StringIO()
f.write("hello")
f.write(" ")
f.write("world")
print(f.getvalue())

f = BytesIO()
f.write("刘威".encode("utf-8"))
print(f.getvalue())
