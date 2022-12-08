from utility import *
from color_print import style

class belay4(belay3):
    def test(self, correct_numbers):
        print(f'Result user_numbers:' + style.MAGENTA + f"{self.user_numbers}", style.YELLOW + f'{self.user_powerball}')
        print(style.RESET+f'Result Lucky_numbers:' + style.MAGENTA + f"{self.todays_numbers}",
              style.YELLOW + f' {self.td_powerball}')
        print(style.RESET + f'You got {self.correct_numbers} correct numbers')
        if self.user_powerball == self.td_powerball and correct_numbers == 0:
            print("you got 4$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 1:
            print("you got 4$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 2:
            print("you got 7$ ")
        elif self.user_powerball == self.td_powerball and correct_numbers == 3:
            print("you got 7$ ")
        elif self.user_powerball == self.td_powerball and correct_numbers == 3:
            print("you got 100$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 4:
            print("you got 100$ ")
        elif self.user_powerball == self.td_powerball and correct_numbers == 4:
            print("you got 10000$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 5:
            print("you got 1000000$")
        elif self.user_powerball == self.td_powerball and correct_numbers == 5:
            print("you got $324000000")


