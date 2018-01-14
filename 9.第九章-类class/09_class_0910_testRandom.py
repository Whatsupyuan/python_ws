from random import randint
# 生成 1 到 6 之间的随机数
x = randint(1, 6)
print(x)


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, 6))


die = Die()
print("开始投掷骰子")
for num in range(1, 11):
    die.roll_die()
