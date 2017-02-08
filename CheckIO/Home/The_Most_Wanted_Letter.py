import re
def checkio(text):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    text_sign=' !/.,+-=?()[]{}#@^&*"$;:\|%1234567890'
    # Переводим текст в нижний регистр
    text_lower=text.lower()
    result_dict={}
    text = ''
    text_alphabet = ''
    text_result = []
    y=0
    x_i=1
    #Убираем с текста все лишнее
    for i in range(len(text_lower)):
        # Сравниваем с масивом знаков
        if text_lower[i] not in text_sign:
            # Создаем чистый текст
            text += text_lower[i]
    # Считаем количество каждого символа
    for i in range(len(text)):
        # Собираем регулярное выражение для поиска
        pattern_x = re.compile(text[i])
        # Создаем словарь с регулярним выражением и его количеством
        result_dict[text[i]] = len(pattern_x.findall(text))
    # Создаем ключ для сортировки словаря
    l = lambda x: x[1]
    # Сортировка
    result=sorted(result_dict.items(), key=l, reverse=True)
    # Берем первый елемент значный елементов кортежа
    result_x = result[0]
    # Создаем список новые одинаковые елементы
    for x_i in range(len(result)):
        # Берем второй елемент для сравнения
        result_y=result[x_i]
        # Сравниваем вторые елементы взятих елементов
        if result_x[1]==result_y[1]:
            # Создаем счетчик для среза максимальных елементов
            y+=1
        else:
            # Если нет прерываем цыкл
            break
    # Создаем новый список из найбольшего елемента
    text_result=result[0:y]
    # Проверям длину масива с результатами
    if len(text_result)!=1:
        # Выбираем буквы с масива результатов
        for i in range(len(text_result)):
            # Берем первый елемент масива результатов
            result_x=text_result[i]
            # Создаем строку с букв елементов масива результатов
            text_alphabet+=result_x[0]
        # проверяем какой из елементов первым входит в алфавитку
        for j in range(len(alphabet)):
            if alphabet[j] in text_alphabet:
                result_alphabet=alphabet[j]
                break
        # Присваеваем результату первый фходящий елемент
        result=result_alphabet
    else:
        # Если елемент один то берем его буквенные елемент
        result_x=text_result[0]
        result=result_x[0]
    return result
print(checkio("How do you do?"))