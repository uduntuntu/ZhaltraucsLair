# -*- coding: utf-8 -*-

import functions.commands as command

f = open('ASCII/otsikko_unicode.asc', 'r')
print(f.read())
f.close()

print("You stand in a start of dungeon. You see a torch.")
c = input(">>> ").lower().split()

while c[0] != "exit":
    if (command.isValid(c)):
        command.execute(c)
    else:
        print('Invalid command. Write "help" to get list of available commands.')
    c = input(">>> ").split()
