# створити пустый список users_list = []
#
# стврорити меню в якому потрібно реалізувати:
#
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
#
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}

users_list = list()

while True:
    print('1. Add new user')
    print('2. Print all users')
    print('3. Print all users by age')
    print('4. Delete user by id')
    print('5. Change status')
    print('6. Exit\n')
    n = int(input('Enter a number of action: '))

    if n == 1:
        name = input('Enter name of new user: ').strip()
        age = int(input('Enter age of new user: ').strip())
        status = input('Enter status of new user (False or True): ').strip()

        status = False if status == 'False' else True

        users_list.append({'id': len(users_list) + 1, 'name': name, 'age': age, 'status': status})
        print('You successfully add user with name "' + name + '", age "' + str(age) + '" and status "' + str(
            status) + '"\n')

    elif n == 2:
        for i in users_list:
            print(i)
        print()

    elif n == 3:
        users_list2 = users_list.copy()
        users_list2.sort(key=lambda x: x['age'])

        for i in users_list2:
            print(i)
        print()

    elif n == 4:
        user_id = int(input('Enter id for delete user: '))

        if user_id > len(users_list):
            print('User with this id does not exist\n')
            continue

        pop_user = users_list.pop(user_id - 1)

        index = 1
        for i in users_list:
            i['id'] = index
            index += 1

        print('You successfully delete user with id: ' + str(user_id))

    elif n == 5:
        user_id = int(input('Enter id for change user status: '))

        if user_id > len(users_list):
            print('User with this id does not exist\n')
            continue

        users_list[user_id - 1]['status'] = not users_list[user_id - 1]['status']

        print('You successfully change status for user with id: ' + str(user_id))
    elif n == 6:
        break
    else:
        print('Incorrect number. Please, try again')
