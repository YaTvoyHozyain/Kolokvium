class Natural:
    """
    Натуральное число

    ввод числа:
    xy = Natural(input())
    """

    def __init__(self, number='0'):
        """
        Конструктор натурального числа: преобразовывает входные данные
        в массив цифр в обратном порядке.

        """
        # преобразуем данные в строку и переворачиваем, так как в будущем так удобнее работать с числом
        number = str(number)
        number = number[::-1]
        # удаление лишних нулей
        if number[-1] == '0' and len(number) > 1:
            raise Exception("Invalid initial data entered")
        # Запись массива цифр в обратном порядке как атрибут класса
        self.numbers = []
        for i in number:
            if i in "0123456789":
                self.numbers.append(int(i))
            else:
                raise Exception("Invalid initial data entered")

    # возвращает строковое представление объекта для функций print() и str()

    def __str__(self):
        """Возврщает значение натурального числа строкой"""
        return ''.join([str(i) for i in reversed(self.numbers)])


# N-1 Счастливая
# Сравнение натуральных чисел: 2 - если первое больше второго,
# 0 - если равно, иначе 1
def COM_NN_D(a, b):
    # копирование данных
    C1 = Natural(str(a))
    C2 = Natural(str(b))
    # изначально сравниваем по длине
    if len(C1.numbers) > len(C2.numbers):
        return 2
    if len(C1.numbers) < len(C2.numbers):
        return 1
    # если длина одинаковая, то сравниваем посимвольно, начиная со старшего разряда
    else:
        for i in range(len(C1.numbers) - 1, -1, -1):
            if C1.numbers[i] < C2.numbers[i]:
                return 1
            elif C1.numbers[i] > C2.numbers[i]:
                return 2
        return 0


# N-2 Булацкий
# Проверка на ноль
# i - массив цифр числа
# Если длина числа 1 и оно-ноль - выдаем 1, если нет - выдаем 0
def NZER_N_B(i):
    i = Natural(str(i))
    if i.numbers[0] == 0 and len(i.numbers) == 1:
        return False
    else:
        return True


# N- 3 Михайлова
# Добавление 1 к натуральному числу
# a - массив цифр числа
def ADD_1N_N(a):
    # копируем данные
    C1 = Natural(str(a))
    # Если в первой же цифре получилось переполнение обрабатываем число по алгоритму
    if C1.numbers[0] + 1 > 9:
        # обработка случая, когда C1 это девять, заменяется на ноль, а к массиву добавляется единица
        if len(C1.numbers) == 1:
            C1.numbers[0] = 0
            C1.numbers.append(1)
        # если же это не девять, то заменяем первую цифру на ноль и начинаем проверять на переполнение следующие цифры
        else:
            C1.numbers[0] = 0
            i = 1
            while C1.numbers[i] + 1 > 9:
                C1.numbers[i] = 0
                i += 1
                # Если переполнение дошло до последней цифры числа, то добавляем еще 1 разряд.
                if i == len(C1.numbers):
                    C1.numbers.append(0)
            C1.numbers[i] = C1.numbers[i] + 1
    # Если же переполнения не случилось, то просто прибавляем единицу к первой цифре
    else:
        C1.numbers[0] = C1.numbers[0] + 1
    return C1


# N-4 Селиверстов
# Сложение натуральных чисел
def ADD_NN_N(a, b):
    # копирование данных
    C1 = Natural(str(a))
    C2 = Natural(str(b))
    # сравнение, чтобы C1 было меньше
    if COM_NN_D(C1, C2) == 2:
        C1, C2 = C2, C1
    # Переменная, отвечающая за перезагрузку символа, т.е. место для 1 в следующем разряде
    overflow = 0
    # Добавление разряда в большее число
    C2.numbers.append(0)
    for i in range(len(C1.numbers)):
        # Складываем поочередно числа столбиком и добавляем единицу переполнения, если она есть
        C2.numbers[i] = C1.numbers[i] + C2.numbers[i] + overflow
        # Обработка случая переполнения
        if C2.numbers[i] > 9:
            C2.numbers[i] = C2.numbers[i] % 10
            overflow = 1
        else:
            overflow = 0
        if i == len(C1.numbers) - 1:
            # случай, когда число C1 уже прибавлено к C2, но осталось переполнение в последнем прибавленном разряде
            j = i
            # пока есть переполнение в свободных разрядах С2 прибавляем к текущему разряду 1
            # если разряд стал > 9 то обнуляем его и идем к следующем разряду
            while overflow == 1:
                C2.numbers[j + 1] = C2.numbers[j + 1] + 1
                if C2.numbers[j + 1] > 9:
                    C2.numbers[j + 1] = C2.numbers[j + 1] % 10
                    j += 1
                else:
                    # выходим из цикла увеличения свободных разрядов С2
                    overflow = 0
            # нет необходимости добавления нового разряда, так как он в любом случае добаляется в начале функции
            # удаление лишнего нуля, если он есть
            if len(C2.numbers) > 1 and C2.numbers[-1] == 0:
                C2.numbers.pop()
    return C2


# N- 5 Счастливая
# Вычитание из первого большего натурального числа
# второго меньшего или равного
def SUB_NN_N(a, b):
    # копирование данных
    C1 = Natural(str(a))
    C2 = Natural(str(b))
    # если первое число меньше второго то ошибка
    if COM_NN_D(C1, C2) == 1:
        raise Exception("The first number is less than the second")
    # Поочередно проходим по цифрам
    for i in range(len(C2.numbers)):
        # Если цифра, которую необходимо отнять больше уменьшаемого, то ищем разряд, у которого можно занять 10
        if C2.numbers[i] > C1.numbers[i]:
            # занимаем 10 из другого разряда, j присваиваем i для поиска разряда у которого заняли 10
            j = i
            C1.numbers[j] = C1.numbers[j] + 10
            # собственно поиск разряда у котогоро заняли 10
            while C1.numbers[j + 1] == 0:
                C1.numbers[j + 1] = 9
                j += 1
            C1.numbers[j + 1] = C1.numbers[j + 1] - 1
        # вычитаем
        C1.numbers[i] = C1.numbers[i] - C2.numbers[i]

    # удаление незначающих нулей в старших разрядах разности
    while len(C1.numbers) > 1 and C1.numbers[-1] == 0:
        C1.numbers.pop()

    return C1


# N-6 Махаев
# Умножение натурального числа на цифру:
def MUL_ND_N(a, dig):
    # копируем данные
    C1 = Natural(str(a))
    # обработка ошибки
    if dig < 0 or dig > 9 or type(dig) is not int:
        raise Exception('Wrong number')

    # добавляем один разряд и обнуляем счетчик займа для разряда
    C1.numbers.append(0)
    res = 0
    # проходим поочередно по цифрам
    for i in range(len(C1.numbers)):
        C1.numbers[i] = C1.numbers[i] * dig + res
        # получаем остаток который надо прибавить к слеующему разряду
        res = C1.numbers[i] // 10
        C1.numbers[i] = C1.numbers[i] % 10

    # удаление незначащих нулей
    while len(C1.numbers) > 1 and C1.numbers[-1] == 0:
        C1.numbers.pop()

    return C1


# N-7 Махаев
# Умножение натурального числа на 10^k
def MUL_Nk_N(a, k):
    # копируем данные
    C1 = Natural(str(a))
    k = Natural(str(k))

    key = Natural('0')
    # пока счетчик не будет равен необходимому k добавляем нули в начало массива цифр
    while COM_NN_D(key, k) != 0:
        C1.numbers = [0] + C1.numbers
        key = ADD_1N_N(key)

    # удаление незначащих нулей
    while len(C1.numbers) > 1 and C1.numbers[-1] == 0:
        C1.numbers.pop()

    return C1


# N-8 Селиверстов
# Умножение натуральных чисел
def MUL_NN_N(a, b):
    # копирование данных
    C1 = Natural(str(a))
    C2 = Natural(str(b))
    # создаем переменную, в которую будем сохранять результат
    ret = Natural('0')
    # идем по порядку по цифрам одного из числа
    for i in range(len(C1.numbers)):
        # сначала умножаем второе число на цифру текущего разряда
        C3 = MUL_ND_N(C2, C1.numbers[i])
        # затем умножаем получившееся число на 10 в степени номера позиции той цифры на которую умножали
        # P.S. счет позиции начинается с 0
        C3 = MUL_Nk_N(C3, i)
        # добавляем полученное число к результатут и так для каждой цифры
        ret = ADD_NN_N(ret, C3)

    return ret


# N-9 Моисеев
# Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
def SUB_NDN_N(a, b, n):
    # копируем данные
    C1 = Natural(str(a))
    C2 = Natural(str(b))

    # домнажаем C2 на цифру
    C2 = MUL_ND_N(C2, n)

    # если домноженное число больше C1 то выдаем ошибку, так как ответ будет отрицательным
    if COM_NN_D(C1, C2) == 1:
        raise Exception('The first number is less than the second')

    # вычитаем из C1 уже домноженное C2
    C1 = SUB_NN_N(C1, C2)

    return C1


# N-10 Булацкий
# Вычисление первой цифры деления, умноженное на 10^k, k - номер позиции цифры.
# Преобразование массивов в числа, перемещение большего числа на первое место,
# нахождение самого числа, ее позиции и результата.
def DIV_NN_Dk(i, y):
    # копируем данные
    C1 = Natural(str(i))
    C2 = Natural(str(y))
    # обработка ошибок
    if not (NZER_N_B(C2)):
        raise Exception("The divisor must be different from zero")
    if COM_NN_D(C1, C2) == 1:
        raise Exception('The first number is less than the second')

    dig = Natural('0')
    ret = Natural('0')
    # пока длина второго числа не будет равна длине первого, вставляем нули в начало второго числа, а счётчик
    # увеличиваем на единицу
    while len(C2.numbers) != len(C1.numbers):
        C2.numbers.insert(0, 0)
        dig = ADD_1N_N(dig)
    # Если при увеличение длины второго числа, оно стало больше первого, удаляем один символ и вычитаем единицу из
    # счётчика
    if COM_NN_D(C1, C2) == 1:
        C2.numbers.pop(0)
        dig = SUB_NN_N(dig, 1)
    # Пока первое число не меньше второго, отнимаем от C1 полученный ранее C2 и увеличиваем новый счётчик на единицу
    while COM_NN_D(C1, C2) == 2 or COM_NN_D(C1, C2) == 0:
        C1 = SUB_NN_N(C1, C2)
        ret = ADD_1N_N(ret)

    # Добавляем к новому счётчику dig нулей
    ret = MUL_Nk_N(ret, dig)

    return ret


# N-11 Михайлова
# Частное от деления большего натурального числа на
# меньшее или равное натуральное с остатком(делитель отличен от нуля)
def DIV_NN_N(a, b):
    # копируем данные
    C1 = Natural(str(a))
    C2 = Natural(str(b))
    # Если второе число 0, то выдаем ошибку
    if not (NZER_N_B(C2)):
        raise Exception("The divisor must be different from zero")

    ret = Natural('0')
    # если первое числа меньше второго, то целое = 0
    if COM_NN_D(C1, C2) == 1:
        return Natural('0')
    # если числа равны, то целое = 1
    elif COM_NN_D(C1, C2) == 0:
        return Natural('1')
    else:
        # пока C1 не меньше С2 ищем первые цифры деления как в функции DIV_NN_Dk, постоянное уменьшая делимое
        # складывая их получаем целое
        while COM_NN_D(C1, C2) == 2 or COM_NN_D(C1, C2) == 0:
            res = DIV_NN_Dk(C1, C2)
            ret = ADD_NN_N(ret, res)
            res = MUL_NN_N(res, C2)
            C1 = SUB_NN_N(C1, res)

        return ret


# N-12 Михайлова
# Остаток от деления большего натурального числа на меньшее
# или равное натуральное с остатком(делитель отличен от нуля)
def MOD_NN_N(a, b):
    # копируем данные
    C1 = Natural(str(a))
    C2 = Natural(str(b))
    # Если второе число 0, то рейзим ошибку
    if not (NZER_N_B(C2)):
        raise Exception("The divisor must be different from zero")

    # если первое числа меньше второго, то целое = 0
    if COM_NN_D(C1, C2) == 1:
        return C1
    # если числа равны, то целое = 1
    elif COM_NN_D(C1, C2) == 0:
        return Natural('0')
    else:
        # пока C1 не меньше С2 ищем первые цифры деления как в функции DIV_NN_Dk, постоянное уменьшая делимое
        # в результате C1 и будет остатком
        while COM_NN_D(C1, C2) == 2:
            res = DIV_NN_Dk(C1, C2)
            res = MUL_NN_N(res, C2)
            C1 = SUB_NN_N(C1, res)

        return C1


# N-13 Горевская
# НОД натуральных чисел
def GCF_NN_N(a, b):
    # копируем данные
    C1 = Natural(str(a))
    C2 = Natural(str(b))

    if COM_NN_D(C1, Natural('0')) == 0 and COM_NN_D(C2, Natural('0')) == 0:
        raise Exception("two numbers are zero")

    # пока хотя бы одно из чисел не ноль, отнимаем от большего меньшее
    while NZER_N_B(C1) and NZER_N_B(C2):
        if COM_NN_D(C1, C2) == 2:
            C1 = MOD_NN_N(C1, C2)
        else:
            C2 = MOD_NN_N(C2, C1)

        # в результате сумма этих двух чисел и будет НОДом
    return ADD_NN_N(C1, C2)


# N-14 Моисеев
# НОК натуральных чисел
def LCM_NN_N(a, b):
    # копируем данные
    C1 = Natural(str(a))
    C2 = Natural(str(b))

    # НОК = C1*C2/НОД(C1,C2)
    GCF = GCF_NN_N(C1, C2)
    C1 = MUL_NN_N(C1, C2)

    return DIV_NN_N(C1, GCF)
