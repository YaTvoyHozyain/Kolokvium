# Z-1 Селивесртов
# Абсолютная величина числа
# Первый элемент массива заменяем на 0
def ABS_Z_N(A):
    A[0] = 0
    return A

# Z-2 Михайлова
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

# Z-3 Махаев
# Умножение целого на -1.
def MUL_ZM_Z(A,k):
    if ((k==1)|(k==0)):
        if k == 0:
            # Если число положительное, то есть знак числа k равно нулю,
            # то заменяем на противоположный знак
            k = 1
        else:
            # Иначе также заменяем k на противоположный знак.
            k = 0
    else: print('error Z-3')
    return k,A

# Z-4 Счастливая
# Преобразование натурального в целое
def TRANS_N_Z(A):
    A = [0] + A
    return A

# Z-5 Грицкевич
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

# Z-6 Булацкий 
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


# Z-7 Горевская
# вычитание целых чисел
def SUB_ZZ_Z (A, b1, n1, B, b2, n2):
    # Рассмотрим разные случаи:
    # 1) a > 0   b > 0
    if(POZ_Z_D(b1, n1, A) == 2 and POZ_Z_D(b2, n2, B) == 2):
        if COM_NN_D(A, B) == 0:
            return 0
        if (COM_NN_D(A, B) == 2) or (COM_NN_D(A, B) == 1):
            SUB_NN_N(A, B)
            if COM_NN_D(A, B) == 1:
                MUL_ZM_Z(A,b1)
            return A
    # 2) a < 0   b < 0
    if(POZ_Z_D(b1, n1, A) == 1 and POZ_Z_D(b2, n2, B) == 1):
        if COM_NN_D(A, B) == 0:
            return 0
        if (COM_NN_D(A, B) == 2) or (COM_NN_D(A, B) == 1):
            SUB_NN_N(A, B)
            if COM_NN_D(A, B) == 1:
                MUL_ZM_Z(A,b1)
            return A
    # 3) a > 0   b < 0
    if(POZ_Z_D(b1, n1, A) == 2 and POZ_Z_D(b2, n2, B) == 1):
        ADD_NN_N(A, B)
        return B
    # 4) a < 0   b > 0
    if(POZ_Z_D(b1, n1, A) == 1 and POZ_Z_D(b2, n2, B) == 2):
        ADD_NN_N(A, B)
        MUL_ZM_Z(B,b2)
        return B
    # 5) a = 0   b > 0
    if(POZ_Z_D(b1, n1, A) == 0 and POZ_Z_D(b2, n2, B) == 2):
        MUL_ZM_Z(B,b2)
        return B
    # 6) a = 0   b < 0
    if(POZ_Z_D(b1, n1, A) == 0 and POZ_Z_D(b2, n2, B) == 1):
        MUL_ZM_Z(B,b2)
        return B
    # 7) a > 0   b = 0
    if(POZ_Z_D(b1, n1, A) == 2 and POZ_Z_D(b2, n2, B) == 0):
        return A
    # 8) a < 0   b = 0
    if(POZ_Z_D(b1, n1, A) == 1 and POZ_Z_D(b2, n2, B) == 0):
        return A
    # 9) a = 0   b = 0
    else:
        return 0
    
# Z-8 Прейгель
# умножение целых чисел
def MUL_ZZ_Z(b1, n1, A1, b2, n2, A2):
    # если одно из чисел - 0, то новое число тоже 0, иначе перемножаем модули чисел
    if(A1[0] == 0 or A2[0] == 0):
        A3 = [0]
    else:
        A3 = MUL_NN_N(A1, A2)
    # n3 - количество чисел в новом числе
    n3 = len(A3)
    # далее учитываются знаки чисел, поданных на вход, из этой информации получаем знак нового числа - b3
    if (POZ_Z_D(b1, n1, A1) == 2 and POZ_Z_D(b2, n2, A2) == 2) or (POZ_Z_D(b1, n1, A1) == 1 and POZ_Z_D(b2, n2, A2) == 1) or POZ_Z_D(b1, n1, A1) == 0 or POZ_Z_D(b2, n2, A2) == 0:
        b3 = 0
    elif (POZ_Z_D(b1, n1, A1) == 2 and POZ_Z_D(b2, n2, A2) == 1) or (POZ_Z_D(b1, n1, A1) == 1 and POZ_Z_D(b2, n2, A2) == 2):
        b3 = 1
    # возвращаем новый массив цифр числа, его знак и номер старшей позиции
    return(b3, n3, A3)


# Z-9 Моисеев
# частное от деления целого на целое
def DIV_ZZ_Z(b, A, c, B):
    # модули числел A и B, результат - натуральное число
    z = ABS_Z_N(A)
    x = ABS_Z_N(B)
    if(POZ_Z_D(x)!=0):
        # частное от деления большего натурального числа на
        # меньшее или равное натуральное с остатком(делитель отличен от нуля)
        t = DIV_NN_N(z, x)
        # преобразование натурального в целое
        t = TRANS_N_Z(t)
        # сравнение знаков
        if b == c:
            return 0, len(t), t
        else:
            return 1, len(t), t
    else:
        print("Делитель равен нулю")
    
    
#Z-10 Горевская
# остаток от деления целого на целое
def MOD_ZZ_Z(a,n1, A, b,n2, B):
    # a,b - знаки чисел, A,B- массивы
    res = MOD_NN_N(A,n1, B,n2)
    if a==b:
        return TRANS_N_Z(res)
    elif a==1:
        res = TRANS_N_Z(ADD_1N_N(res))
        return res
    else:
        return res
