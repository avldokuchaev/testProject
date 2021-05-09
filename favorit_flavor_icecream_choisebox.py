import easygui
flavor_icecream = easygui.choicebox("Какой твой любимый вкус мороженого?",
                                    choices = ["Ванильный", "Клубничный", "Шоколадный"])
your_favorit_flavor = easygui.msgbox("Вы выбрали: " + flavor_icecream)
print(your_favorit_flavor)
