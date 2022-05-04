# N-1 Счастливая
# Сравнение натуральных чисел: 2 - если первое больше второго,
# 0 - если равно, иначе 1
def COM_NN_D(A, B):
    # находим первый ненулевой элемент в первом числе
    i = 0
    while A[i] == 0 and i + 1 != len(A):
        i += 1
    # если количество пройденных элементов равно длине массива,
    # то число - ноль
    if i == len(A):
        A1 = [0]
        len1 = 1
    else:
        # начиная с этого элемента заносим все оставшиеся цифры в новый массив А1,
        # где len1 - длина нового массива
        len1 = len(A) - i
        A1 = A[i:]
    # аналогично работаем со вторым числом
    i = 0
    while B[i] == 0 and i + 1 != len(B):
        i += 1
    if i == len(B):
        B1 = [0]
        len2 = 1
    else:
        len2 = len(B) - i
        B1 = B[i:]
    # сравниваем длину чисел, которое длиннее - больше
    if len1 > len2:
        return 2
    elif len2 > len1:
        return 1
    # если длины равны
    else:
        i = 0
        # находим номер несовпадающего элемента массивов
        while i != len1 and A1[i] == B1[i]:
            i += 1
        # если такого числа не нашлось, и количество пройденных
        # элементов равно длине массива, то они совпадают
        if i == len1:
            return 0
        else:
            # если несовпадающий элемент первого массива больше,
            # значит первое число больше, иначе - второе
            if A1[i] > B1[i]:
                return 2
            else:
                return 1


# N-2 Булацкий 
# Проверка на ноль. Если ноль - выдаем 1, если нет - выдаем 0
def NZER_N_B(i):
    if i[0] != 0:
        return 0
    else:
        return 1


# N- 3 Михайлова
# k - количество разрядов, a - массив цифр числа
def ADD_1N_N(A):
    A.reverse()
    if COM_NN_D([A[0]], [9]) == 1:
        # Если последняя цифра числа < 9, то добавляем единицу
        A[0] += 1
    else:
        i = 0
        while COM_NN_D(INT_TO_ARR(A[0]), [9]) == 0:
            # Если последняя цифра числа равна 9, то, пока разряды не перестанут
            # быть равными 9, заменяем на 0
            A[i] = 0
            i += 1
            # Если преобразования были осуществлены со всеми разрядами,
            # то добавляем новый разряд
            if i == len(A):
                A.append(0)
            # К первому разряду, не равному 9, добавляем единицу
        A[i] += 1
    A.reverse()
    A = ''.join(map(str, A))
    c = [0] * len(A)
    for i in range(len(A)):
        c[i] = int(A[i])
    return c


# N-4 Селиверстов
# Сложение натуральных чисел
def ADD_NN_N(A, B):
    # Если первое число больше второго, то меняем их местами
    if COM_NN_D(A, B) == 2:
        A, B = B, A
    k = len(B) - len(A)
    A.reverse()
    # Дополняем нулями разряды меньшего числа до разрядов большего
    for i in range(0, ARR_TO_INT(ADD_1N_N(INT_TO_ARR(k)))):
        A.append(0)
    A.reverse()
    B.reverse()
    B.append(0)
    B.reverse()
    print(A, B)
    # Процесс сложения чисел
    for i in range(len(B) - 1, 0, -1):
        # Если сумма цифр больше десяти,
        # то переносим единицу в старший разряд
        if type(B[i]) == list:
            B[i] = ARR_TO_INT(B[i])
        if type(A[i]) == list:
            A[i] = ARR_TO_INT(A[i])
        if COM_NN_D(INT_TO_ARR(B[i] + A[i]), INT_TO_ARR(10)) != 1:
            B[i] = (B[i] + A[i]) % 10
            B[i - 1] = ADD_1N_N(INT_TO_ARR(B[i - 1]))
        else:
            B[i] = B[i] + A[i]
    if type(B[0]) != int:
        B[0] = ARR_TO_INT(B[0])
    if COM_NN_D(INT_TO_ARR(B[0]), INT_TO_ARR(0)) == 0:
        B.remove(0)
    return B


# N- 5 Счастливая
# Вычитание из первого большего натурального числа
# второго меньшего или равного
def SUB_NN_N(A, B):
    # если второе число больше, меняем A и B местами
    if COM_NN_D(A, B) == 1:
        temp = A
        A = B
        B = temp
    # если длины чисел не равны, то добавляем нули в начало второго числа
    if COM_NN_D(INT_TO_ARR(len(A)), INT_TO_ARR(len(B))) != 0:  # Если длины А и В не равны
        B.reverse()
        for i in range(len(A) - len(B)):
            B.append(0)
        B.reverse()
    # вычитание
    for i in range(len(B) - 1, -1, -1):
        if COM_NN_D([A[i]], [B[i]]) != 1:  # Если A[i] >= B[i]
            A[i] -= B[i]
        else:
            A[i] = ARR_TO_INT(ADD_NN_N([A[i]], [1, 0])) - B[i]
            k = i - 1
            while NZER_N_B([A[k]]) == 1:
                A[k] = 9
                k -= 1
            A[k] -= 1
    # убираем лишние нули в начале
    i = 0
    while NZER_N_B([A[i]]) == 1 and COM_NN_D(INT_TO_ARR(i), INT_TO_ARR(len(A) - 1)) != 0:  # Пока A[i] нуль и индекс i не последний
        i = ARR_TO_INT(ADD_1N_N(INT_TO_ARR(i)))  # индекс увеличивается на 1
    if COM_NN_D(INT_TO_ARR(i), INT_TO_ARR(len(A))) == 0:  # Если индекс равен длине
        A = [0]
    else:
        A = A[i:]
    return A


# N-6 Махаев
def MUL_ND_N(A, n):
    A.reverse()
    A.append(0)
    A.reverse()
    # Добавляем доп. разряд в начало
    k = 0
    for i in range(len(A) - 1, 0, -1):
        tmp = A[i]
        A[i] = A[i] * n % 10
        A[i] = ARR_TO_INT(ADD_NN_N(INT_TO_ARR(A[i]), INT_TO_ARR(k)))
        k = int(tmp * n / 10)
        # k - перенос на другой разряд
        if COM_NN_D(INT_TO_ARR(A[i]), [1, 0]) != 1:
            # Если после домножения, в разряде числа больше 9, то
            # разряд числа равен остатку от деления на 10, и
            # в переменную, отвечающую за доп разряд прибавляем 1
            A[i] = A[i] % 10
            k = ARR_TO_INT(ADD_1N_N(INT_TO_ARR(k)))
    A[0] = k
    if NZER_N_B(INT_TO_ARR(A[0])) == 1:
        A.remove(0)
    return A


# N-7 Махаев
# Умножение натурального числа на 10^k
def MUL_Nk_N(A, k):
    for i in range(k):
        # Цикл по степени десятки, добавляет k нулей в конец массива
        A.append(0)
    return A


# N-8 Селиверстов
# Умножение натуральных чисел
def MUL_NN_N(a, b):
    A, B = copy.copy(a), copy.copy(b)
    result = []
    B.reverse()
    B.append(0)
    for i in range(len(B)):
        temp = []
        # Умножаем исходное число на текущий разряд
        if NZER_N_B(INT_TO_ARR(B[i])) == 0:
            temp = MUL_ND_N(A, B[i])
        # Умножаем результат на 10^i, чтобы "сдвинуть" его
        temp = MUL_Nk_N(temp, i)
        # добавляем к результату
        if NZER_N_B(INT_TO_ARR(len(result))) == 0:
            result = ADD_NN_N(result, temp)
        else:
            result = temp
    if NZER_N_B(INT_TO_ARR(result[0])) == 1:
        del result[0]
    return result


# N-9 Моисеев
# Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
def SUB_NDN_N(A, B, n):
    t = SUB_NN_N(A, MUL_ND_N(B, n))
    return t


# N-10 Булацкий
# Вычисление первой цифры деления, умноженное на 10^k, k - номер позиции цифры.
# Преобразование массивов в числа, перемещение большего числа на первое место,
# нахождение самого числа, ее позиции и результата.
def DIV_NN_Dk(i, y):
    count = 1
    if COM_NN_D(i, y) == 0:
        return 1, 0
    if COM_NN_D(i, y) == 1:
        big = y
        small = i
    else:
        big = i
        small = y
    k = 0
    n3 = small
    tm = small.copy()
    while COM_NN_D(big, n3) == 2:
        k = ARR_TO_INT(ADD_1N_N(INT_TO_ARR(k)))  # добавление 1 к k
        n3 = MUL_Nk_N(tm, k)
        tm = small.copy()
    k = ARR_TO_INT(SUB_NN_N(INT_TO_ARR(k), [1]))  # вычитаение 1 из k
    tm = small.copy()
    n3 = MUL_Nk_N(tm, k)
    small = n3
    tm = small.copy()
    while COM_NN_D(big, n3) == 2:
        count = ARR_TO_INT(ADD_1N_N(INT_TO_ARR(count)))  # добавление 1 к count
        n3 = MUL_ND_N(tm, count)
        tm = small.copy()
    if COM_NN_D(big, n3) != 0:
        count = ARR_TO_INT(SUB_NN_N(INT_TO_ARR(count), [1]))  # вычитаение 1 из count
    if COM_NN_D(INT_TO_ARR(count), [1, 0]) == 0:
        count = ARR_TO_INT(SUB_NN_N(INT_TO_ARR(count), [1]))  # вычитаение 1 из count
        k = ARR_TO_INT(ADD_1N_N(INT_TO_ARR(k)))  # добавление 1 к k
    bb = [count]
    df = MUL_Nk_N(bb, k)
    return df


# N-11 Михайлова
# Частное от деления большего натурального числа на
# меньшее или равное натуральное с остатком(делитель отличен от нуля)
def DIV_NN_N(A, B):
    if COM_NN_D(A, B) != 0:
        m = DIV_NN_Dk(A, B)
        print(m)
        div = [0]
        # Пусть a >= b
        # Тогда, если на вход задаются числа, не удовлетворяющие этому условию,
        # значения меняются местами
        if COM_NN_D(A, B) == 1:
            A, B = B, A
        # Частное от деления a на b
        while COM_NN_D(A, B) != 1:  # пока A >= B
            A = SUB_NN_N(A, B)
            if NZER_N_B(INT_TO_ARR(B[0])) == 1:
                del B[0]
            div = ADD_1N_N(div)
        return div
    else:
        return [1]
    
    
# N-12 Михайлова
# Остаток от деления большего натурального числа на меньшее
# или равное натуральное с остатком(делитель отличен от нуля)
def MOD_NN_N(a, b):
    A = copy.copy(a)
    B = copy.copy(b)
    if A != B:
        # Пусть a >= b
        # Тогда, если на вход задаются числа, не удовлетворяющие этому словию,
        # значения меняются местами
        if COM_NN_D(A, B) == 1:
            A, b = B, A
        k = [0]*len(A)
        n = [0]*len(B)
        for i in range(len(A)):
            k[i] = A[i]
        for i in range(len(B)):
            n[i] = B[i]
        c = DIV_NN_N(k, n)
        mul = MUL_NN_N(B, c)
        mod = SUB_NN_N(A, mul)
        return mod
    else:
        return [0]
    
    
# N-13 Горевская
# НОД натуральных чисел
def GCF_NN_N(a, b):
    A, B = copy.copy(a), copy.copy(b)
    # Вычисление НОД натуральных чисел
    # Проверка на ноль
    if NZER_N_B(A) == 0 and NZER_N_B(B) == 0:
        # Сравнение чисел
        temp = COM_NN_D(A, B)
        # Если первое число меньше второго -
        # меняем их местами
        if temp == 1:  # если temp равно 1
            A, B = B, A
            temp = 2
        # Если первое число больше второго -
        # вычисляем НОД с помощью алгоритма
        # Евклида
        if temp == 2:  # если temp равно 2
            while NZER_N_B(B) == 0:  # если B[0] не нуль
                rem = MOD_NN_N(A, B)
                if NZER_N_B(rem) == 1:
                    return B
                A = B
                B = rem
        # Если числа равны - любое из них
        # и есть их НОД
        if NZER_N_B(INT_TO_ARR(temp)) == 1:  # если равно нулю
            return B
    # Если какое-то из чисел равно нулю, тогда
    # НОД у них нет
    else:
        return ("No common dividers")

        
# N-14 Моисеев
# НОК натуральных чисел
def LCM_NN_N(A, B):
    if COM_NN_D(A, B) == 1:
        A, B = B, A
    i = copy.copy(A)
    while True:
        if NZER_N_B(MOD_NN_N(i, A)) == 1 and NZER_N_B(MOD_NN_N(i, B)) == 1:
            break
        i = ADD_1N_N(i)
    return i
