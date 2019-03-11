class Student(object):

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("must be integer!")

        if value < 0 or value > 100:
            raise ValueError("socre between 0 and 100")

        self.__score = value


a = Student()
a.set_score(69)
print(a.get_score())


# a.set_score(1000)# error
# print(a.get_score())


class Teacher(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("must be integer!")

        if value < 0 or value > 100:
            raise ValueError("socre between 0 and 100")

        self.__score = value


b = Teacher()
b.score = 60
print(b.score)

# b.score = 6000 #error
# print(b.score)
