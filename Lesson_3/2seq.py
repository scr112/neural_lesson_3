spisok = input('Введите любые числа списка используя один из разделителей  запятую, точку с запятой или слэш: : ')
result_list = []
numbers_list = []
##### меняем разделитель в записимости от разрешенных #####
if ',' in spisok:
    numbers_list = spisok.split(',')
elif ';' in spisok:
    numbers_list = spisok.split(';')
elif '/' in spisok:
    numbers_list = spisok.split('/')
else:
    print("Некорректный формат ввода. Используйте один из разделителей: запятая, точка с запятой или слэш.")
for i in numbers_list: #### если при вводе указать , то падал с ошибоку т к сортировал и это был пустой элемент. удаляем его.
    if i == '':
        numbers_list.remove(i)
count_1 = 0
for i in numbers_list:
    count = numbers_list.count(i) #### подсчитывает колчество одинаковых элементов в списке.
    if int(i) == 1: #### не считал коунтом количество 1, прилошлось написать собственнный обработчик.
        count_1 += 1
        if count_1 == 1:
            result_list.append(i)
        elif count_1 > 1:
            result_list.remove('1')
    else:
        if count == 1: ### остальные элементы, котоыре не являются 1
            result_list.append(i)
print("Результат:", ", ".join(result_list))
print(type(result_list))
