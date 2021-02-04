import re

my_f = open("task6.txt", "r")
content = my_f.readlines()
schedule = {}
count = []

for i in range(len(content)):
    subject = (content[i].split()[0][:-1])
    total = sum(map(int, re.findall(r'\d+', content[i])))
    schedule[subject] = total

print(schedule)
