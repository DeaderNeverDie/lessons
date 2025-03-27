# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
index = ''
normal_index = 0
mailing_address = ''
additional_information = ''
# business information
main_state_registration_number = 0
taxpayer_identification_number = 0
payment_account = 0
bank_name = ''
bank_identification_number = 0
correspondent_account = 0

def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter,
                      index_parameter, mailing_address_parameter, additional_information):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс:', index_parameter)
    print('Почтовый адрес:', mailing_address_parameter)
    print('Дополнительная информация:', additional_information)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for char in user_phone:
                    if char == '+' or ('0' <= char <= '9'):
                        phone += char

                email = input('Введите адрес электронной почты: ')

                index = input('Введите почтовый индекс:')
                for char in index:
                    if char == '0' <= char <= '9':
                        normal_index +=char

                mailing_address = input('Введите почтовый адрес (без индекса):')

                additional_information = input('Введите дополнительную информацию:')

            elif option2 == 2:
                # input business information
                while True:
                    main_state_registration_number = int(input('Введите ОГРНИП:'))
                    if len(str(main_state_registration_number)) == 15:
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр')
                taxpayer_identification_number = int(input('Введите ИНН:'))
                while True:
                    payment_account = int(input('Введите расчетный счет:'))
                    if len(str(payment_account)) == 20:
                        break
                    else:
                        print('Расчетный счет должен содержать 20 цифр')
                bank_name = input('Введите название банка:')
                bank_identification_number = int(input('Введите БИК:'))
                correspondent_account = int(input('Введите корреспондентский счет:'))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index, mailing_address, additional_information)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, mailing_address, additional_information)

                # print business information
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП', main_state_registration_number)
                print('ИНН', taxpayer_identification_number)
                print('Банковские реквизиты')
                print('Р/с', payment_account)
                print('Банк:', bank_name)
                print('БИК', bank_identification_number)
                print('К/с', correspondent_account)

            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')




