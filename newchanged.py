with open(r'C:\Users\HOME\Desktop\labone\steam_description_data.csv', encoding='utf-8') as f:
    sym_num = 0
# общее количество символов
    space_num = 0
# количество пробелов
    letters_num = 0
# количество букв и цифр
    words_num = 0
# количество слов при условии, что слово это последовательность символов до ".", ",", "!", "?" или " "
    sentences_num = 0
# количество предложений
    s = ''
    p = ''
    for line in f:
        for j in line:
            sym_num += 1
            if j == ' ':
                space_num += 1
            if j.isalnum():
                letters_num += 1
            if s.isalnum() and j in ',.!? ':
                words_num += 1
            s = j
            if j not in '!?.':
                p += j
            elif p != '':
                sentences_num += 1
                p = ''
print('Количество символов всего: ', sym_num)
print('Количество символов без пробелов: ', sym_num - space_num)
print('Количество символов без знаков препинания: ', letters_num + space_num)
print('Количество слов: ', words_num)
print('Количество предложений: ', sentences_num)
