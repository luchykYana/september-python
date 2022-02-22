# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         return todo_list
#
#     return {'add': add_todo, 'get': get_all}
#
#
# add_1, get_1 = notebook().values()
# add_2, get_2 = notebook().values()
#
# add_1('Eat')
# add_1('Sleep')
# add_1('Programing')
#
# print(get_1())
#
# add_2('Eat2')
# add_2('Sleep2')
# add_2('Programing2')
#
# print(get_2())

# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    mas = list(str(num))
    length = len(mas)

    i = 0
    while i < length:
        if mas[i] == '0':
            mas.pop(i)
            length -= 1
            continue

        mas[i] += '0' * (length - i - 1)
        i += 1

    return ' + '.join(mas)


print(expanded_form(15070))
