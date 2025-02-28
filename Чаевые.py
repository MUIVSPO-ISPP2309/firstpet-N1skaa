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
    if b == 'да' or b == 'yes':
        while True:
            c = int(input('Сколько чаевых вы хотите оставить?\n1. 10%\n2. 15%\n3. 20%\nВведите номер варианта: '))
            if c == 1:
                c = 10
                break
            elif c == 2:
                c = 15
                break
            elif c == 3:
                c = 20
                break
            else:
                print('Некорректный выбор чаевых. Пожалуйста, попробуйте снова.')
        f = d * c
        j = (d * c) + a
        a = j
        print('Чаевые составляют - {:.2f}'.format(f))
        break  
    elif b == 'нет' or b == 'no':
        print('Хорошо')
        break  
    else:
        print('Некорректный ответ. Пожалуйста, введите "да" или "нет".')
while True:
    g = input('Желаете ли вы разделить счет? (да/нет): ').lower()
    if g == 'да' or g == 'yes':
        m = int(input('Сколько вас человек? '))
        v = a / m
        print('{:.2f} - Сумма к оплате с человека'.format(v))
        break
    elif g == 'нет' or g == 'no':
        print('Хорошо. Вот сумма к оплате - {:.2f}'.format(a))
        break
    else:
        print('Некорректный ответ. Пожалуйста, введите "да" или "нет".')
