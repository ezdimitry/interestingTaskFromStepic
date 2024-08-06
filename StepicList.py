"""
Search
На вход программе подаются натуральное число n
n — количество строк, затем сами строки в указанном количестве, затем число k
k, затем сами поисковые запросы.
Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
"""
s = []
p = []
for _ in range(int(input())):
    s.append(input())
for _ in range(int(input())):
    p.append(input())
for i in s:
    n = 0
    for k in p:
        if k.lower() in i.lower():
            n += 1
    if n >= len(p):
        print(i)