import guizero
import random
from guizero import App, Text, PushButton, info, Box, Picture

class Vandana:
    def __init__(self, total_money):
        self.money_counter = total_money
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.nextbutton = None
        self.moneyvalue = None
        self.moneyvalue = None


    def rand_nums(self):

        fruit_list = ["apple.gif", "pear.gif", "banna.gif", "straw.gif", ]
        n1 = random.choice(fruit_list)
        n2 = random.choice(fruit_list)
        n3 = random.choice(fruit_list)
        return n1, n2, n3

    def next_turn(self):
        self.bet_money(1)
        print("money = ", self.money_counter)
        n1, n2, n3 = self.rand_nums()
        self.button1.image = n1
        self.button2.image = n2
        self.button3.image = n3
        self.money_counter = self.money_counter-1
        self.check_jackpot(n1, n2, n3, 10)

    def bet_money(self, money):
        self.money_counter -= money
        if self.moneyvalue:
            self.moneyvalue.value = self.money_counter


    def check_jackpot(self, n1, n2, n3, jackpot_value):
        if n1 == n2 and n2 == n3:
            self.money_counter += jackpot_value
            print("Won jackpot!  money = ", self.money_counter)
            info("Welldone", "Wowwww you did it! From a 1/10 chance!")
            if self.money_counter:
                self.moneyvalue.value = self.money_counter

    def drawgame(self):
        self.bet_money(1)
        print("money = ", self.money_counter)
        self.app = App(title="Vandana game for Nanny", layout="grid")
        n1, n2, n3 = self.rand_nums()
        self.button1 = Picture(self.app, image=n1, width=500, height=300, grid=[0, 0])
        self.button2 = Picture(self.app, image=n2, width=500, height=300, grid=[1, 0])
        self.button3 = Picture(self.app, image=n3, width=500, height=300, grid=[2, 0])
        self.nextbutton = PushButton(self.app, command=self.next_turn, text="Bet $1", grid=[1,1])
        box = Box(self.app, border=True, grid=[1,2])
        moneytext = Text(box, text="Your Money")
        self.moneyvalue = Text(box, text=self.money_counter, bg="red")
        self.check_jackpot(n1, n2, n3, 10)
        self.app.display()
        print(self.money_counter)

game = Vandana(50)
game.drawgame()
