# -*- coding: utf-8 -*-

import functions.commands as command

prompt = ">>> "
view = {
    '0.0' : "Tutorial. You see a rat attacking you, fight!",
    '1.0' : "You stand in a start of dungeon. You see a torch."
}

position = '1.0'
c = 0

f = open('ASCII/otsikko_unicode.asc', 'r')
print(f.read())
f.close()

menuSelectionIsValid = False

command.doMenu(0)

while not menuSelectionIsValid:
    try:
        c = int(input(prompt))
        command.doMenu(c)
    except ValueError as e:
        print(e)

    if c in command.menu:
        menuSelectionIsValid = True

print(view[position])
c = input(prompt).lower().split()

while c[0] != "quit":
    if (command.isValid(c)):
        command.execute(c)
        print(view[position])
    else:
        print(
            'Invalid command. Write "help" to get list of available commands.'
        )
    c = input(prompt).lower().split()
