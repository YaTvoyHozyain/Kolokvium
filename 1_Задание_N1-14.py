# N-1
# Сравнение натуральных чисел: 2 - если первое больше второго,
# 0 - если равно, иначе 1
def COM_NN_D(A, B):
    # находим первый ненулевой элемент в первом числе
    i = 0
    while A[i] == 0 and i != len(A):
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
    while B[i] == 0 and i != len(B):
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
            
# N-2
# Проверка на ноль. Если ноль есть - выдаем "No", если есть - выдаем "Yes"
def NZER_N_B(i):
    if i[0] != 0:
        print("Yes")
    else:
        print("No")
        
# N- 3
# k - количество разрядов, a - массив цифр числа
def ADD_1N_N(k, a):
    a.reversed(a)
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
    a = int(''.join(map(str, a)))
    return k, a

# N-4
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

# N- 5
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

# N-6 Умножение натурального числа на цифру:
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

# N-7 Умножение натурального числа на 10^k
def MUL_Nk_N(A, k):
    for i in range(k):
        # Цикл по степени десятки, добавляет k нулей в конец массива
        A.append(0)
    return A

# N-8
# Умножение натуральных чисел
def MUL_NN_N(A, B):
    result = []
    B.reverse()
    B.append(0)
    for i in range(len(B)):
        # Умножаем исходное число на текущий разряд
        temp = MUL_ND_N(list(A), B[i])
        # Умноженаем результат на 10^i, чтобы "сдвинуть" его
        temp = MUL_Nk_N(list(temp), i)
        # добавляем к результату
        result = ADD_NN_N(list(result), temp)
    if result[0] == 0:
        del result[0]
    return result

# N-10
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
    return count, k

# N-11
def DIV_NN_N(a, k, b, n):
    # k - количество разрядов, a - массив цифр числа
    # n - количество разрядов, b - массив цифр числа
    m = DIV_NN_Dk(a, b)
    div = [0] * m[1]
    num = 0
    # Пусть a >= b
    # Тогда, если на вход задаются числа, не удовлетворяющие этому словию,
    # значения меняются местами
    if (k < n) or (k == n and a[k-1] < b[n-1]):
        a, b = b, a
        k, n = n, k
    # Частное от деления a на b
    while (COM_NN_D(a, k, b, n) == 2) or (COM_NN_D(a, k, b, n) == 0):
        c = DIV_NN_Dk(a, k, b, n)
        mul = MUL_NN_N(b, n, c[0], c[1])
        a = SUB_NDN_N(a, k, mul[0], mul[1])
        a = a[0]
        div = ADD_NN_N(div, c[0])
        num += 1
    return num, div[0]

# N-12
def MOD_NN_N(a,k,b,n):
    # k - количество разрядов, a - массив цифр числа
    # n - количество разрядов, b - массив цифр числа
    # Пусть a >= b
    # Тогда, если на вход задаются числа, не удовлетворяющие этому словию,
    # значения меняются местами
    if (k < n) or (k == n and a[k - 1] < b[n - 1]):
        a, b = b, a
        k, n = n, k
    c = DIV_NN_N(a, k, b, n)
    mul = MUL_NN_N(n, b, c[1], c[0])
    mod = SUB_NDN_N(a, k, mul[0], mul[1])
    return mod

# N-13
def GCF_NN_N(A, B):
    #Вычисление НОД натуральных чисел
    #Проверка на ноль
    if(A > 0):
        if(B > 0):
            #Сравнение чисел
            temp = COM_NN_D(A, B)
            #Если первое число меньше второго -
            #меняем их местами
            if(temp == 1):
                t = A 
                A = B
                B = t 
                temp = 2
            #Если первое число больше второго -
            #вычисляем НОД с помощью алгоритма
            #Евклида
            if(temp == 2):
                while(rem != 0):
                    rem = MOD_NN_N(A, B)
                    A = B 
                    B = rem
                print(A)
            #Если числа равны - любое из них
            #и есть их НОД
            if(temp == 0):
                print(B)
    #Если какое-то из чисел равно нулю, тогда 
    #НОД у них нет
    else:
        print("No common dividers")
