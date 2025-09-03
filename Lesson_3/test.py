import re

s1 = re.sub(' ','',input("Введите последовательность чисел: "))
delims = re.sub('[0-9]','',s1)
if delims.count(delims[0]) == len(delims) and delims[0] in [',','.','/']:
    list_clean = s1.split(delims[0]) # по ТЗ :)
    list_uniq = list(filter(lambda s: s and list_clean.count(s) == 1, list_clean))
    print(', '.join(list_uniq))
else:
    raise "Incorrect delimiter"
print(type(list_uniq))