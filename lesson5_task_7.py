import json

# Построчно читает файл
my_f = open("task7.txt", "r")
content = my_f.read()
print(content)
my_f.close()
print('\n')

# Вычисляет прибыль каждой прибыльной компании и среднее значение прибыли этих компаний
profit = 0
av_profit = 0
k = 0
pr = {}
loss = {}
av_pr = {}
my_f = open("task7.txt", "r")
content = my_f.readlines()
for i in range(len(content)):
    prof = int(content[i].split()[2]) - int(content[i].split()[3])
    if prof >= 0:
        print(f'Прибыль компании {content[i].split()[0]} составила {prof} тугриков')
        av_profit += prof
        k += 1
        pr[content[i].split()[0]] = prof
    else:
        loss[content[i].split()[0]] = prof

if k != 0:
    print(f'Средняя прибыль прибыльных компаний составляет {av_profit / k}')

# Реализация списка с фирмами и их прибылью, а также словарь со средней прибылью, фирмами их убытками
li = [pr, av_pr, loss]
av_pr['average_profit'] = av_profit / k

with open('task7.json', 'w') as new_f:
    json.dump(li, new_f)
    js_str = json.dumps(li)
    print(f'\n{js_str}')
