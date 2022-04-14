# Z-1
# Абсолютная величина числа
# Первый элемент массива заменяем на 0
def ABS_Z_N(A):
    A[0] = 0
    return A

# Z-2
def POZ_Z_D(b, n, a):
    # b - знак числа, n - количество разрядов, a - массив цифр числа
    # b = 0 - положительное, 1 - отрицательное
    # Возвращает 0 если число равно нулю, если отрицательное возвращает 1
    # и если положительное - 2
    if a == [0] * n:
        return 0
    elif b == 0:
        return 2
    else:
        return 1

# Z-3 Умножение целого на -1.
def MUL_ZM_Z(A,k):
    if k == 0:
        # Если число положительное, то есть знак числа k равно нулю,
        # то заменяем на противоположный знак
        k = 1
    else:
        # Иначе также заменяем k на противоположный знак.
        k = 0
    return k,A

# Z-4
# Преобразование натурального в целое
def TRANS_N_Z(A):
    A = [0] + A
    return A

# Z-5
# Преобразование целого неотрицательного числа в натуральное
def TRANS_Z_N(a):
    #приравниваем весь массив
    Str=a[:]
    #если 1 элемент массива ноль, то оно целое число, значит удаляем этот элемент
    if Str[0] == 0:
        Str.remove(Str[0])
    #если не 0, то значит число натуральное и выводит ошибку в применении
    elif Str[0] != 0:
        print("Error: Z-5")
    return Str

# Z-6
# Сложение целых чисел. Определяем положительность, далее используем функцию сложение натуральных,
# добавляем ячейку для знака и домножаем на -1. Если они оба положительны, то делаем
# тоже самое, но не домножаем на -1 в конце. Если они оба равны - результат равен 0.
# Если они разных знаков то делаем натуральным, далее  сравниваем по величине. Производим вычитание.
def ADD_ZZ_Z(A, B):
    AZ = POZ_Z_D(A) 
    BZ = POZ_Z_D(B)
    if (AZ == BZ) & (AZ == 1):
        a = A[1:]
        b = B[1:]
        result = ADD_NN_N(a, b)
        result.insert(0, 0)
        result = MUL_ZM_Z(result)
    elif (AZ == BZ) & (AZ == 2):
        a = A[1:]
        b = B[1:]
        result = ADD_NN_N(a, b)
        result.insert(0, 0)
    elif (AZ == BZ) & (AZ == 0):
        result = 0
    else:
        a = ABS_Z_N(A)
        b = ABS_Z_N(B)
        raz = COM_NN_D(a, b)
        if raz == 2:
            result = SUB_NN_N(a, b)
            if AZ == 1:
                result.insert(0, 0)
                result = MUL_ZM_Z(result)
            else:
                result.insert(0, 0)
        else:
            result = SUB_NN_N(b, a)
            result.insert(0, 0)
            if BZ == 1:
                result = MUL_ZM_Z(result)
    return result

# Z - 8 - умножение целых чисел
def MUL_ZZ_Z(b1, n1, A1, b2, n2, A2):
    # из массива A1 и A2 делаем сначала строки, а потом числа
    str1 = ""
    str2 = ""
    for x in range(n1):
        str1 += str(A1[x])
    for x in range(n2):
        str2 += str(A2[x])
    a = int(str1)
    b = int(str2)
    c = a * b # умножение двух чисел в натуральном виде, знаки пока не учитываются (здесь вместо * должна быть функция умножения натуральных чисел MUL_NN_N)
    n3 = len(str(c))# n3 - номер старшего разряда получившегося числа, он же равен количесту цифр в числе
    # далее учитываются знаки чисел, поданных на вход, из этой информации получаем знак нового числа - b3
    if (POZ_Z_D(b1, n1, A1) == 2 and POZ_Z_D(b2, n2, A2) == 2) or (POZ_Z_D(b1, n1, A1) == 1 and POZ_Z_D(b2, n2, A2) == 1) or POZ_Z_D(b1, n1, A1) == 0 or POZ_Z_D(b2, n2, A2) == 0:
        b3 = 0
    elif (POZ_Z_D(b1, n1, A1) == 2 and POZ_Z_D(b2, n2, A2) == 1) or (POZ_Z_D(b1, n1, A1) == 1 and POZ_Z_D(b2, n2, A2) == 2):
        b3 = 1
    # из числа делаем массив его цифр
    A3 = []
    for x in range(n3):
        A3.append(int(str(c)[x]))
    return(b3, n3, A3)
# Z - 9
def DIV_ZZ_Z(b, A, c, B):
    # b - знак первого числа A - массив цифр первого числа
    # с - знак второго числа B - массив цифр второго числа
    n = POZ_Z_D(A)
    m = POZ_Z_D(B)
    A = ABS_Z_N(A)
    B = ABS_Z_N(B)
    t = DIV_NN_N(A, B)
    if n == m:
        return TRANS_N_Z(t)
    elif MOD_NN_N(A, B)[1] != [0]:
        t = TRANS_N_Z(ADD_1N_N(t))
        t[0] += 1
        return t
    else:
        t = TRANS_N_Z(t)
        t[0] += 1
        return t
