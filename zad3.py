with open(r'C:\Users\HOME\Desktop\labone\steam_description_data.csv', encoding='utf-8') as f:
    k = 0
    a = ord('0')
    b = ord('9')
    c = ord('A')
    d = ord('Z')
    e = ord('a')
    t = ord('z')
    for i in f:
        for j in i:
            g = ord(j)
            if (g >= a & g <= b) | (g >= c & g <= d) | (g >= e & g <= t) | g == 32:
                # если считать, что знаками препинания являются все символы кроме букв, цифр и пробелов
                k += 1
print(k)
# интерпретатор выдает: "Process finished with exit code 0" я так понимаю, что это из-за того,
# что данные слишком большие и он неможет столько процессов выполнить за короткое время и у него ошибка
# времени выполнения. Я пыталась сократить колическтво операций, присвоив отдельным переменным ord(), чтобы он
# не искал его каждый раз, но это не особо помогло.
