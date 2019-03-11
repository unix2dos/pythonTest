class Student(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


levon = Student("levon")
print(levon.getName())  # levon
levon.__name = "xuanxuan"
print(levon.getName())  # levon(ineffective)
levon._Student__name = "haha"
print(levon.getName())  # haha
