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
# Проверка на ноль. Если ноль есть - выдаем "No", если нет - выдаем "Yes"
def NZER_N_B(i):
    if i[0] != 0:
        return "Yes"
    else:
        return "No"


# N- 3 Михайлова
# k - количество разрядов, a - массив цифр числа
def ADD_1N_N(k, a):
    a.reverse()
    if a[0] < 9:
        # Если последняя цифра числа < 9, то добавляем единицу
        a[0] += 1
    else:
        i = 0
        while (a[i] == 9):
            # Если последняя цифра числа равна 9, то, пока разряды не перестанут
            # быть равными 9, заменяем на 0
            a[i] = 0
            i += 1
            # Если преобразования были осуществлены со всеми разрядами,
            # то добавляем новый разряд
            if i == len(a):
                a.append(0)
                k += 1
            # К первому разряду, не равному 9, добавляем единицу
        a[i] += 1
    a.reverse()
    a = ''.join(map(str, a))
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = int(a[i])

    return (k, c)


# N-4 Селиверстов
# Сложение  натуральных чисел
def ADD_NN_N(A, B):
    # Если первое число больше второго, то меняем их местами
    if COM_NN_D(A, B) == 2:
        C = B
        B = A
        A = C
    k = len(B) - len(A)
    A.reverse()
    # Дополняем нулями разряды меньшего числа до разрядов большего
    for i in range(0, k + 1, 1):
        A.append(0)
    A.reverse()
    B.reverse()
    B.append(0)
    B.reverse()
    # Процесс сложения чисел
    for i in range(len(B) - 1, 0, -1):
        # Если суума цифр больше десяти,
        # то переносим единицу в старший разряд
        if B[i] + A[i] >= 10:
            B[i] = (B[i] + A[i]) % 10
            B[i - 1] += 1
        else:
            B[i] = B[i] + A[i]
    if B[0] == 0:
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
    if len(A) != len(B):
        B.reverse()
        for i in range(len(A) - len(B)):
            B.append(0)
        B.reverse()
    # вычитание
    for i in range(len(B) - 1, -1, -1):
        if A[i] >= B[i]:
            A[i] -= B[i]
        else:
            A[i] = A[i] + 10 - B[i]
            k = i - 1
            while A[k] == 0:
                A[k] = 9
                k -= 1
            A[k] -= 1
    # убираем лишние нули в начале
    i = 0
    while A[i] == 0 and i != len(A) - 1:
        i += 1
    if i == len(A):
        A = [0]
    else:
        A = A[i:]

    return A


# N-6 Махаев
# Умножение натурального числа на цифру:
def MUL_ND_N(A, n):
    A.reverse()
    A.append(0)
    A.reverse()
    # Добавляем доп. разряд в начало
    k = 0
    for i in range(len(A) - 1, 0, -1):
        tmp = A[i]
        A[i] = A[i] * n % 10
        A[i] += k
        k = int(tmp * n / 10)
        # k - перенос на другой разряд
        if A[i] >= 10:
            # Если после домнажения,в разряде числа больше 9, то
            # разряд числа равен остатку от деления на 10, и
            # в переменную, отвечающую за доп разряд прибавляем 1
            A[i] = A[i] % 10
            k += 1
    A[0] = k
    if A[0] == 0:
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
def MUL_NN_N(A, B):
    k = 0
    result = []
    B.reverse()
    B.append(0)
    for i in range(len(B)):
        # Умножаем исходное число на текущий разряд
        temp = MUL_ND_N(list(A), B[i])
        # Умноженаем результат на 10^i, чтобы "сдвинуть" его
        temp = MUL_Nk_N(list(temp), i)
        # добавляем к результату
        if len(result) != 0:
            result = ADD_NN_N(list(result), temp)
        else:
            result = list(temp)
    if result[0] == 0:
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
        k += 1
        n3 = MUL_Nk_N(tm, k)
        tm = small.copy()
    k -= 1
    tm = small.copy()
    n3 = MUL_Nk_N(tm, k)
    small = n3
    tm = small.copy()
    while COM_NN_D(big, n3) == 2:
        count += 1
        n3 = MUL_ND_N(tm, count)
        tm = small.copy()
    if COM_NN_D(big, n3) != 0:
        count -= 1
    if count == 10:
        count = 1
        k += 1
    bb = [count]
    df = MUL_Nk_N(bb, k)

    return df


# N-11 Михайлова
# Частное от деления большего натурального числа на
# меньшее или равное натуральное с остатком(делитель отличен от нуля)
def DIV_NN_N(a, b):
    if(COM_NN_D(a, b) == 0):
        return a
    elif a==[1]:
        return b
    elif b==[1]:
        return a
    elif a!=b:
        # k - количество разрядов, a - массив цифр числа
        # n - количество разрядов, b - массив цифр числа
        m = DIV_NN_Dk(a, b)
        div = [0] * len(m)
        # Пусть a >= b
        # Тогда, если на вход задаются числа, не удовлетворяющие этому словию,
        # значения меняются местами
        if (len(a) < len(b)) or (len(a) == len(b) and a[0] < b[0]):
            a, b = b, a
        # Частное от деления a на b
        while (COM_NN_D(a, b) == 2) or (COM_NN_D(a, b) == 0):
            c = DIV_NN_Dk(a, b)
            mul = MUL_NN_N(b, c)
            c = DIV_NN_Dk(a, b)
            a = SUB_NN_N(a, mul)
            div = ADD_NN_N(div, c)
        return div
    else:
        return [1]
    
    
# N-12 Михайлова
#Остаток от деления большего натурального числа на меньшее
#или равное натуральное с остатком(делитель отличен от нуля)
def MOD_NN_N(a, b):
    if a==[1] or b==[1] or a==b:
        return [0]
    elif a != b:
        k=[0]
        n=[0]
        # k - количество разрядов, a - массив цифр числа
        # n - количество разрядов, b - массив цифр числа
        # Пусть a >= b
        # Тогда, если на вход задаются числа, не удовлетворяющие этому словию,
        # значения меняются местами
        if (len(a) < len(b)) or (len(a) == len(b) and a[0] < b[0]):
            a, b = b, a
        k = [0]*len(a)
        n = [0]*len(b)
        for i in range (len(a)):
            k[i]=a[i]
        for i in range(len(b)):
            n[i]=b[i]
        c = DIV_NN_N(k, n)
        mul = MUL_NN_N(b, c)
        mod = SUB_NN_N(a, mul)
        return mod
    else:
        return [0]
    
    
# N-13 Горевская
# НОД натуральных чисел
def GCF_NN_N(A, B):
    # Вычисление НОД натуральных чисел
    # Проверка на ноль
    if (NZER_N_B(A) == "Yes" and NZER_N_B(B) == "Yes"):
        # Сравнение чисел
        temp = COM_NN_D(A, B)
        # Если первое число меньше второго -
        # меняем их местами
        if (temp == 1):
            A, B = B, A
            temp = 2
        # Если первое число больше второго -
        # вычисляем НОД с помощью алгоритма
        # Евклида
        rem=[0]
        if (temp == 2):
            while (B[0] != 0):
                rem=MOD_NN_N(A, B)
                print('rem:')
                print(rem)
                A = B
                B = rem
            return A
        # Если числа равны - любое из них
        # и есть их НОД
        if (temp == 0):
            return B
    # Если какое-то из чисел равно нулю, тогда
    # НОД у них нет
    else:
        return ("No common dividers")

        
# N-14 Моисеев
#НОК натуральных чисел
def LCM_NN_N(A, B):
    k = [0] * len(A)
    n = [0] * len(B)
    for i in range(len(A)):
        k[i] = A[i]
    for i in range(len(B)):
        n[i] = B[i]
    #НОК(a, b)=a·b:НОД(a, b).
    t = DIV_NN_N(MUL_NN_N(k, n), GCF_NN_N(A, B))
    return t
