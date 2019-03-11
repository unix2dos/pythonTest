from enum import Enum, unique

EMOTION = Enum("EMOTION", ("None", "Happy", "Sad"))

print(EMOTION.Happy, EMOTION.Happy.value)

for k, v in EMOTION.__members__.items():
    print(k, v, v.value)


@unique  # 检测重复
class Week(Enum):
    Sun = 0  # 注意此处没有逗号
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Week.Fri)
print(Week.Fri.value)
print(Week(1))
