import random, easygui
secret = random.randint(1, 99)
guess = 0
tries = 0
hello_text = easygui.msgbox('Эй, на палубе! Я ужасный пират Робертс, и у меня есть секрет! '
                            'Это число от 1 до 99. Я дам тебе 6 попыток.')
print(hello_text)
while (guess != secret and tries < 6):
    guess = int(easygui.enterbox('Твой вариант?'))
    if (guess < secret):
        few_number = easygui.msgbox('Это слишком мало, презренный пес!')
        print(few_number)
    elif (guess > secret):
        lot_number = easygui.msgbox('Это слишком много, сухопутная крыса!')
        print(lot_number)

    tries = tries + 1

if (guess == secret):
    that_number = easygui.msgbox('Хватит, ты угадал мой секрет!')
    print(that_number)
else:
    alles_caput = easygui.msgbox('Попытки кончились. Это число: ' + str(secret))
    print(alles_caput)
