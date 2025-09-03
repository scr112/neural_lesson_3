from os import remove

spisok = list((input('Введите элементы первого списка через , цифру: ')))
spisok = ''.join(char for char in spisok if char.isalnum())

spisok2 = (input('Введите элементы второго списка через , цифру: '))
spisok2 = ''.join(char for char in spisok2 if char.isalnum())
print (list(set(spisok) - set(spisok2)))




