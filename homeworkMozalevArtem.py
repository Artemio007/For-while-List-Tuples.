import math

# '''task 1 '''

# num = int(input("Введите целое число "))
# if num > 0:
#     fib_1 = 0
#     fib_2 = 1
#     count = 0
#     while count < num - 3:
#         fib_1, fib_2 = fib_2, fib_2 + fib_1
#         count += 1
#     print("Число фибоначчи под № " + str(num) + " = "+ str(fib_2 + fib_1), end=" ")
# elif num < 0:
#     fib_1 = 0
#     fib_2 = -1
#     count = 0
#     while count > num + 3:
#         fib_1, fib_2 = fib_2, fib_2 + fib_1
#         count -= 1
#     print("Число фибоначчи под № " + str(num) + " = "+ str(fib_2 + fib_1), end=" ")
# elif num == 0:
#     print("0")

# '''task 2(1)'''

# hi = "Hello world"
# hi_1 = hi.lower().replace("o", "a")
# print(hi_1.lower().replace("l", "e"))


# '''task 2(2) '''
# hi = "Hello world"
# print([i.replace("o", "a") and i.replace("l", "e")for i in hi])

# '''task 3 '''

# line = "Ham is tasty"
# print(line)
# a = ""
#
# for i in range(len(line)):
#
#     if i % 2 == 0:
#         a += "_"
#     elif i % 2 != 0 and line[i] == "a":
#         a += "b"
#     else:
#         a += line[i]
# print(a)

# '''task 4 '''

# num = 100
# for i in range(num):
#     if i % 3 == 0:
#         print(i)

# '''task 5(1) '''

# for i in range(1, 19):
#     if i != 4:
#         print(i)

# '''task 5(2) '''

# num = 0
# while num < 100:
#     num += 1
#     if num == 4:
#         continue
#     if num == 19:
#         break
#     print(num)


# '''task 6 (1) '''

# list = []
# for i in range(int(input())):
#     list_el = input()
#     list.append(list_el)
# print(list)
# print(max(list))

# '''task 6 (2) '''

# list = []
# N = int(input())
# i = 0
# while i < N:
#     list_el = input()
#     list.append(list_el)
#     i += 1
# print(list)
# print(max(list))

# '''task 7 '''

# list = []
# list_count = []
# for i in range(int(input())):
#     new_list = int(input())
#     list.append(new_list)
# print(list)
# for j in list:
#     if list.count(j) >= 2:
#         a = list.count(j)
#         for k in range(a):
#             list_count.append(k)
#         print("Количество повторений числа " + str(j) + " = " + str(a))
#         print("Количество пар числа " + str(j) + " = " + str(sum(list_count)))
#         list_count = []
#     else:
#         print("Нет пар для числа " + str(j))

# '''task 8 '''

# N = float(input())
# if N % N == 0 and N % 1 == 0:
#     print(1)
# else:
#     print(0)

# '''task 9 '''

# N = int(input())
# a = 0
# list = []
# while a < int(N):
#     a += 1
#     if a % 2 == 0:
#
#         list.append(- math.factorial(a))
#     if a % 2 != 0:
#
#         list.append(math.factorial(a))
# print(list)
# print(sum(list))

# ''' task 10 '''

# line = "1_2,40_5,5_32"
# list = ([sum([int(i) for i in j.split("_")]) for j in line.split(",")])
# print(list)