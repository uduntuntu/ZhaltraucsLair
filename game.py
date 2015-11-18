# -*- coding: utf-8 -*-

import functions.commands as command

f = open('ASCII/otsikko_unicode.asc', 'r')
print(f.read())
f.close()

print("You stand in a start of dungeon. You see a torch.")
c = input(">>> ").split()

while c[0] != "exit":
    if (command.isValid(c)):
        if c[0] == "go" or c[0] == "turn":
            command.go(c)
        elif c[0] == "help":
            command.help()
    else:
        print('Invalid command. Write "help" to get list of available commands.')
    c = input(">>> ").split()
