'''
На вход программе подаются два числа, каждое на отдельной строке.
Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и сумму его делителей.
'''
a = int(input())
b = int(input())
summdel = 0
maxdigit = 0
for i in range(a, b + 1):
    maxi = 0
    for j in range(1, i + 1):
        if i % j == 0:
            maxi += j
        if maxi >= summdel:
            summdel = maxi
            maxdigit = j
print(maxdigit, summdel)