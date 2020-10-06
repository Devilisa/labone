f = open(r'C:\Users\HOME\Desktop\labone\steam_description_data.csv', encoding='utf-8')
k = 0
for i in f:
    for j in i:
        k += 1
f.close()
print(k)
