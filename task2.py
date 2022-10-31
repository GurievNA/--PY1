def get_count_char(str_):  #Функция для пункта 2
    abc_dict = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for n in str_:
        if n.isalpha():
            if n in abc_dict:
                abc_dict[n] += 1
            else:
                abc_dict[n] = 1
    return abc_dict

main_str = """Данное предложение будет разбиваться на отдельные слова. В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!"""

def proc(dict_):    #Функция для пункта 5
    cba_dict = {}
    n = 0
    for i in dict_.values():
        n = n + i
    for i in dict_.items():
        perc = i[1] / n * 100
        perc = round(perc, 2)
        cba_dict.setdefault(i[0], perc)
    return cba_dict

print(get_count_char(main_str))
print(proc(get_count_char(main_str)))