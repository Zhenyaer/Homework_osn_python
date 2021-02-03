file = 'task2.txt'
my_f = open(file, "r")
content = my_f.readlines()
print(f'В файле {file} записано {len(content)} строк.')
for i in range(len(content)):
    print(f'В строке № {i+1} содержится {len(content[i].split())} слов(а).')
