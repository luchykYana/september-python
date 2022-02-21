# strings

# # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# # наприклад:
# # st = 'as 23 fdfdg544' введена строка
# # 2,3,5,4,4        #вивело в консолі.
#
# def get_numbers_from_string(str=''):
#     return ','.join([i for i in str if i.isdigit()])
#
# print(get_numbers_from_string('as 23 fdfdg544'))

# # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# # так як вони написані
# # наприклад:
# #   st = 'as 23 fdfdg544 34' #введена строка
# #   23, 544, 34              #вивело в консолі
#
# def get_full_numbers_from_string(str_num=''):
#     for i in [i for i in str_num if not i.isdigit()]:
#         str_num = str_num.replace(i, ' ')
#
#     return ','.join(str_num.split(),)
#
#
# print(get_full_numbers_from_string('as 23 fdfdg544 34'))


# list comprehension

# # 1)есть строка:
# # greeting = 'Hello, world'
# # записать каждый символ в лист поменяв его на верхний регистр
# # пример:
# # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# def str_to_list(str=''):
#     return list(str.upper())
#
#
# print(str_to_list('Hello, world'))

# # 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
#
# res_list = [i**2 for i in range(51) if i % 2]
# print(res_list)

# function

# # - створити функцію яка виводить ліст
#
# def print_list(l):
#     print(l)

# # - створити функцію яка приймає три числа та виводить та повертає найменьше.
#
# def three_num_with_min(a, b, c):
#     print(a, b, c)
#     return min(a, b, c)

# # - створити функцію яка приймає три числа та виводить та повертає найбільше.
#
# def three_num_with_max(a, b, c):
#     print(a, b, c)
#     return max(a, b, c)

# # - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
#
# def numbers(*args):
#     print(max([i for i in args if str(i).isdigit()]))
#     return min([i for i in args if str(i).isdigit()])

# # - створити функцію яка повертає найбільше число з ліста
#
# def max_list(l):
#     return max([i for i in l if str(i).isdigit()])

# # - створити функцію яка повертає найменьше число з ліста
#
# def min_list(l):
#     return min([i for i in l if str(i).isdigit()])

# # - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
#
# def sum_list(l):
#     return sum([i for i in l if str(i).isdigit()])

# # - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
# def mid_list(l):
#     mas = [i for i in l if str(i).isdigit()]
#     return sum(mas) / len(mas)


# #################################################################################################
# # 1)Дан лист:
# #   list = [22, 3,5,2,8,2,-23, 8,23,5]
# #   - найти min число в листе
# #   - удалить все дубликаты в листе
# #   - заменить каждое четвертое значение на "Х"
#
# list_num = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# print(min(list_num))
#
# print(list(set(list_num)))
#
# for i in range(len(list_num)):
#     list_num[i] = 'X' if (i+1) % 4 == 0 else list_num[i]
#
# print(list_num)

# # 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
#
# def square(n):
#     if n < 4:
#         return print('Too small square')
#
#     print('*' * n)
#     for i in range(n - 2):
#         print('*', ' ' * (n - 4), '*')
#
#     print('*' * n)
#
#
# square(10)

# # 3) вывести табличку умножения с помощью цикла while
#
# def multiplication_table():
#     i = 1
#     j = 1
#
#     while i < 10:
#         if j < 10:
#             print(j * i, end='\t')
#             j += 1
#         else:
#             print()
#             i += 1
#             j = 1
#
#
# multiplication_table()

# # 4) переделать первое задание под меню с помощью цикла
# while True:
#     print('Дан лист: [22, 3,5,2,8,2,-23, 8,23,5]')
#     print('1. найти min число в листе')
#     print('2. удалить все дубликаты в листе')
#     print('3. заменить каждое четвертое значение на "Х"')
#     n = int(input('Enter number of action: '))
#
#     list_num = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     list_num2 = list()
#
#     if n == 1:
#         print('1 answer: ', min(list_num))
#     elif n == 2:
#         print('2 answer: ', list(set(list_num)))
#     elif n == 3:
#         for i in range(len(list_num)):
#             list_num2.append('X' if (i + 1) % 4 == 0 else list_num[i])
#         print('3 answer: ', list_num2)
#     else:
#         print('Incorrect number. Please, try again')
