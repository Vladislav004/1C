def substrings(s):

    #s = list(s)

    i = 0 #Счетчик для перебора символов по индексу
    word = []
    k_open_count = s.count('[') #Подсчет (закрытых, открытых = 1) символов [
    k_closed_count = s.count(']') #Подсчет (закрытых = 1, открытых) символов ]

    k_open = [] #Индексы [
    k_closed = [] #Индексы ]

    while i < len(s): #Заполнение массивов индексами
        char = s[i]
        if char == '[':
            k_open.append(i)
        elif char == ']':
            k_closed.append(i)
        i += 1

    k_closed.reverse()


    while k_open or k_closed:
        if len(k_open) == len(k_closed): #Проверка на состыковки открытых и закрытых символов
            i_open = k_open[0]
            i_closed = k_closed[0]

            #Удаление индексов из массивов
            k_open.pop(0)
            k_closed.pop(0)

            s_word = s[i_open+1:i_closed] #Срез подстрок

            word.append(s_word)
        else:
            return "Состыковок:\nНе обнаружено"


    return word

#input_s = input(str("Строка: "))
input_s = '[это[тес[тов]а]я][ст]р[о[ка]]!'
result = substrings(input_s)
print(result)