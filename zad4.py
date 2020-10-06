with open(r'C:\Users\HOME\Desktop\labone\steam_description_data.csv', encoding='utf-8') as f:
    k = 0
    s = ''
    for i in f:
        for j in i:
            if ord(j) != 32:
                s = s + j
            # если считать словом последовательность непробелов
            elif s != '':
                k += 1
                s = ''
print(k)
