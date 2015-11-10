f = open('otsikko_test.asc',encoding='cp437',mode='r')
ascii = f.read()
f.close()

f = open('otsikko_unicode.asc', encoding='UTF-8', mode='w')
f.write(ascii)
f.close()