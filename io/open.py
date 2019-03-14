try:
    f = open("1.txt", "r")
    print(f.read())
finally:
    f.close()

with open("1.txt", "r") as f:
    print(f.read())

with open("2.txt", "w") as f:
    f.write("hello\n")
