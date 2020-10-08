with open(r'C:\Users\HOME\Desktop\labone\steam_description_data.csv', encoding='utf-8') as f:
    k1 = 0
# общее количество символов
    k2 = 0
# количество пробелов
    k3 = 0
# количество букв и цифр
    k4 = 0
# количество слов при условии, что слово это последовательность символов до ".", ",", "!", "?" или " "
    k5 = 0
# количество предложений
    s = ''
    p = ''
    for i in f:
        for j in i:
            k1 += 1
            if j == ' ':
                k2 += 1
            if j.isalnum() == 1:
                k3 += 1
            if s.isalnum() == 1 and (j == ' ' or j == '.' or j == ',' or j == '!' or j == '?'):
                k4 += 1
            s = j
            if j != '.' and j != '!' and j != '?':
                p += j
            elif p != '':
                k5 += 1
                p = ''
print(k1)
print(k1 - k2)
print(k3 + k2)
print(k4)
print(k5)
