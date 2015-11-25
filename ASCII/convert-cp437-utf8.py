# -*- coding: utf-8 -*-

def convertCP437toUTF8(inputFile, outputFile):
    f = open(inputFile,encoding='cp437',mode='r')
    original = f.read()
    f.close()

    f = open(outputFile, encoding='UTF-8', mode='w')
    f.write(original)
    f.close()
    return

convertCP437toUTF8('StartScreen.asc','StartScreen_UTF-8.asc')