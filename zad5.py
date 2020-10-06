with open(r'C:\Users\HOME\Desktop\labone\steam_description_data.csv', encoding='utf-8') as f:
    k = 0
    s = ''
    for i in f:
        for j in i:
            if ord(j) != ord('.') & ord(j) != ord('!') & ord(j) != ord('?'):
                s = s + j
            # если считать предложением любую последовательность символов, оканчивающуюся '.' , '?' , '!' , '...',
            # но многоточие здесь не учитывается, потому что оно засчитается за точку,
            # а остальные точки просто пропустятся
            elif s != '':
                k += 1
                s = ''
print(k)
