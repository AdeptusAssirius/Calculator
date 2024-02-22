import math

def сложение(first, second):

    return first + second


def вычитание(first, second):

    return first - second


def умножение(first, second):

    return first * second


def деление(first, second):

    return first / second


def калькулятор(first, second, oper):

    result = None

    if oper == '+':

        result = сложение(first, second)

    elif oper == '-':

        result = вычитание(first, second)

    elif oper == '*':

        result = умножение(first, second)

    elif oper == '/':

        if (second == 0):

            print('Деление на ноль запрещено!')

            return

        result = деление(first, second)

    elif oper == '%':

        result = first / second * 100

    elif oper == '**':

        result = first ** second

    elif oper == 'log':

        result = math.log(first, second)

    else:

        print('Некорректная операция!')

    return result


def operation():

    mes = input('Выберите операцию (Введите +, -, *, /, %, **, log):\n'

                '+ - сложение двух чисел\n'

                '- - вычитание двух чисел\n'

                '* - умножение двух чисел\n'

                '/ - деление двух чисел\n'

                '% - процент первого числа от второго\n'

                '** - возведение первого числа в степень второго\n'

                'log - логарифм первого числа по основанию второго\n')

    if mes == '+':

        print('Выбрано сложение')

    elif mes == '-':

        print('Выбрано вычитание')

    elif mes == '*':

        print('Выбрано умножение')

    elif mes == '/':

        print('Выбрано деление')

    elif mes == '%':

        print('Выбрано нахождение процента первого числа от второго')

    elif mes == '**':

        print('Выбрано возведение в степень')

    elif mes == 'log':

        print('Выбран логарифм')


    correct_operations = ['+', '-', '*', '/', '%', '**', 'log']

    while mes not in correct_operations:

        print('Такой операции нет в списке. Попробуйте ещё!')

        mes = input()


    return mes


def run():

    try:

        first = int(input('Укажите первое число: '))

    except ValueError:

        first = int(input('Вы ввели некорректные данные. Пожалуйста, введите целое число.'))

    try:

        second = int(input('Укажите второе число: '))

    except ValueError:

        second = int(input('Введены некорректные данные. Введите целое число!'))

    op = operation()

    result = калькулятор(first, second, op)

    print(f'Результат: {result}')


progam_is_running = True

while(progam_is_running):

    run()

    answer = input('Хотите продолжить?\n'

      'Если да, то введите +, если нет, то иной символ: ')

    if answer != '+':

        progam_is_running = False