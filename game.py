'''

f = open('ASCII/otsikko_test.asc',encoding='cp437',mode='r')
ascii = f.read()
f.close()

f = open('ASCII/otsikko_unicode.asc', encoding='UTF-8', mode='w')
f.write(ascii)
f.close()
'''

f = open('ASCII/otsikko_unicode.asc', 'r')
print(f.read())
f.close()