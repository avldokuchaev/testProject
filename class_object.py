class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Сырая"
        self.condiments = []
    def __str__(self):
        msg = "сосиска"
        if len(self.condiments) > 0:
            msg = msg + " с "
        for i in  self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg
    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Сгоревшая"
        elif self.cooked_level > 5:
            self.cooked_string = "Хорошо прожаренная"
        elif self.cooked_level > 3:
            self.cooked_string = "Средней прожарки"
        else:
            self.cooked_string = "Сырая"
    def addCondiments(self, condiment):
        self.condiments.append(condiment)
myDog = HotDog()
print(myDog)
print("Готовим сосиску 4 минуты")
myDog.cook(4)
print(myDog)
print("Готовим сосиску еще 3 минуты")
myDog.cook(3)
print(myDog)
print("Что произойдет, если я буду ее готовить еще 10 минут?")
myDog.cook(10)
print(myDog)
print("Сейчас я добавлю в хот-дог другие компоненты")
myDog.addCondiments("кетчуп")
myDog.addCondiments("горчица")
print(myDog)