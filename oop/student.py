class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def Say(self):
        print("%s: %s" % (self.name, self.score))


levon = Student("levon", 100)
xuanyuan = Student("xuanyuan", 10)
levon.Say()
xuanyuan.Say()
