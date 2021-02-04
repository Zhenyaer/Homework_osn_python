import re

my_f = open("task6.txt", "r")
content = my_f.readlines()
schedule = {}
count = []

for i in range(len(content)):
    schedule[(content[i].split()[0][:-1])] = sum(map(int, re.findall(r'\d+', content[i])))

print(schedule)
