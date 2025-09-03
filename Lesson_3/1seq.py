col_elem = range(int(input("введите количество элементов в списке: ")))
spisok = []
for i in col_elem:
   spisok.append(int(input("Введите любую цифру: ")))
   spisok.sort(key=int)
#spisok = range(col_elem)
print(spisok)

