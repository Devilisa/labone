with open(r'C:\Users\HOME\Desktop\steam_description_data.csv', encoding='utf-8') as f:
    k = 0
    for i in f:
        for j in i:
            if ord(j) != 32:
                k += 1
print(k)
