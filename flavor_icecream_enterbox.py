import easygui
flavor_icecream = easygui.enterbox("Какой твой любимый вкус мороженого?")
your_favorit_flavor = easygui.msgbox("Ваш любимый вкус мороженого: " + flavor_icecream)
print(your_favorit_flavor)
