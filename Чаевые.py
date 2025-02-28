while True:
    try:
        a = float(input('Введите сумму счета: '))
    except ValueError:
        print("Неверный ввод, попробуйте заново ввести сумму")
    else:
        print('Вы ввели сумму счета -', a)
        break
d = a / 100
while True:
    b = input('Желаете ли вы оставить чаевые? (да/нет): ').lower()
    match b:
        case 'да' | 'yes':
            while True:
                try:
                    c = int(input('Сколько чаевых вы хотите оставить?\n1. 10%\n2. 15%\n3. 20%\nВведите номер варианта: '))
                    if c in [1, 2, 3]:
                        c = [10, 15, 20][c - 1]  
                        break
                    else:
                        print('Некорректный выбор чаевых. Пожалуйста, попробуйте снова.')
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите номер варианта.")
            f = d * c
            j = (d * c) + a
            a = j
            print('Чаевые составляют - {:.2f}'.format(f))
            break
        case 'нет' | 'no':
            print('Хорошо')
            break
        case _:
            print('Некорректный ответ. Пожалуйста, введите "да" или "нет".')
while True:
    g = input('Желаете ли вы разделить счет? (да/нет): ').lower()
    match g:
        case 'да' | 'yes':
            while True:
                try:
                    m = int(input('Сколько вас человек? '))
                    if m > 0:
                        v = a / m
                        print('{:.2f} - Сумма к оплате с человека'.format(v))
                        break
                    else:
                        print("Количество человек должно быть положительным. Пожалуйста, введите корректное число.")
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")
            break
        case 'нет' | 'no':
            print('Хорошо. Вот сумма к оплате - {:.2f}'.format(a))
            break
        case _:
            print('Некорректный ответ. Пожалуйста, введите "да" или "нет".')
