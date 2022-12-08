
from random import randint

class belay():
    def __init__(self):
        self.user_numbers = []
        self.user_powerball = []

    def genrerate(self):
        print('Enter 5 unduplicated Numbers  vertically:')
        for num in range(0, 5):
            user_num = int(input())
            if 1 <= user_num<= 20:
                self.user_numbers.append(user_num)
            else:
                user_num2 = int(input("Please not enter above 20: "))
                self.user_numbers.append(user_num2)
        pball = int(input("Enter power ball num: "))
        if 0 < pball < 10:
            self.user_powerball.append(pball)

class belay2(belay):
    def __init__(self):
        super().__init__()
        self.todays_numbers = []
        self.td_powerball = []

    def belly(self):
        for num in range(0, 5):
            user_num = randint(1, 20)
            self.todays_numbers.append(user_num)
        tpball = randint(1, 10)
        self.td_powerball.append(tpball)


class belay3(belay2):

    def be(self):
        self.correct_numbers = len(set(self.user_numbers).intersection(set(self.todays_numbers)))
        return self.correct_numbers