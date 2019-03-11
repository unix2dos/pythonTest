class Student(object):
    def say(self):
        print("i am a student")


class FlyableMixIn(object):
    def fly(self):
        print("i can fly fly fly!!!")


class Levon(Student, FlyableMixIn):
    pass


l = Levon()
l.say()
l.fly()
