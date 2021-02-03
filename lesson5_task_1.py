my_f = open("task1.txt", "w")
flag = True
while flag:
    text = input('Введите текст: ')
    if text == '':
        flag = False
    else:
        my_f.writelines(text + '\n')

my_f.close()
my_f = open("task1.txt", "r")
content = my_f.read()
print(content)
my_f.close()
