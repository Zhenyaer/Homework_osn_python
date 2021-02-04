file = 'task4.txt'
my_f = open(file, "r")
rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new = []

for i in my_f:
    if i.split()[0] in rus_dict:
        new.append(f'{rus_dict[i.split()[0]]} - {i.split()[-1]}\n')

new_f = open("task4_rus.txt", "w")
new_f.writelines(new)
new_f.close()

my_f_rus = open("task4_rus.txt", 'r')
content = my_f_rus.read()
print(content)
