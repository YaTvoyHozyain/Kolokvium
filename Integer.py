# Z-1 Селиверстов
# Абсолютная величина числа
# A - массив чисел, b - знак (0 - плюс, 1 - минус)
def ABS_Z_N(A, b):
    # возвращаем число без знака
    return A


# Z-2 Михайлова
# Определение положительности числа
# A - массив чисел, b - знак (0 - плюс, 1 - минус)
def POZ_Z_D(A, b):
    # если число ноль возвращаем 0
    if A == [0] * len(A):
        return 0
    # если число положительное возвращаем 2
    elif b == 0:
        return 2
    # если число отрицательное возвращаем 1
    else:
        return 1


# Z-3 Махаев
# Умножение целого на -1
# A - массив чисел, b - знак (0 - плюс, 1 - минус)
def MUL_ZM_Z(A, b):
    # меняем знак на противоположный
    if b == 0:
        b = 1
    elif b == 1:
        b = 0
    else:
        print('error Z-3')
    return A, b


# Z-4 Счастливая
# Преобразование натурального в целое
# A - массив чисел, b - знак (0 - плюс, 1 - минус)
def TRANS_N_Z(A):
    # добавляем натуральному числу знак, превращая в целое
    b = 0
    return A, b


# Z-5 Грицкевич
# Преобразование целого неотрицательного числа в натуральное
# A - массив чисел, b - знак (0 - плюс, 1 - минус)
def TRANS_Z_N(A, b):
    # возвращаем число без знака
    return A


# Z-6 Булацкий
# Сложение целых чисел
# A, B - массивы чисел, ka, kb - знаки (0 - плюс, 1 - минус)
# result - результирующий массив, res_k - знак получившегося числа
def ADD_ZZ_Z(A, ka, B, kb):
    # Если оба числа равны нулю (POZ_Z_D - проверка на положительность), то их сумма тоже будет равна 0
    if POZ_Z_D(A, ka) == POZ_Z_D(B, kb) & POZ_Z_D(A, ka) == 0:
        result = [0]
        res_k = 0
    else:
        # если числа одного знака
        if POZ_Z_D(A, ka) == POZ_Z_D(B, kb):
            # Используем функцию сложения натуральных чисел (для этого берем модули чисел)
            result = ADD_NN_N(ABS_Z_N(A, ka), ABS_Z_N(B, kb))
            # превращаем натуральное в целое
            result, res_k = TRANS_N_Z(result)
            # Если оба числа отрицательные (POZ_Z_D - проверка на положительность)
            if POZ_Z_D(A, ka) == 1:
                # Домножаем результат на -1
                result, res_k = MUL_ZM_Z(result, res_k)
        # Если у чисел разные знаки
        else:
            # Сравниваем два числа по модулю
            raz = COM_NN_D(ABS_Z_N(A, ka), ABS_Z_N(B, kb))
            # Если а > b то
            if raz == 2:
                # Вычитаем из первого большего натурального числа второе меньшее
                result = SUB_NN_N(ABS_Z_N(A, ka), ABS_Z_N(B, kb))
                # превращаем натуральное в целое
                result, res_k = TRANS_N_Z(result)
                # Если первое число отрицательное
                if POZ_Z_D(A, ka) == 1:
                    # Домножаем результат на -1
                    result, res_k = MUL_ZM_Z(result, res_k)
            # Если а < b то
            else:
                # Вычитаем из второго большего натурального числа первое меньшее
                result = SUB_NN_N(ABS_Z_N(A, ka), ABS_Z_N(B, kb))
                # превращаем натуральное в целое
                result, res_k = TRANS_N_Z(result)
                # Если второе число отрицательное
                if POZ_Z_D(B, kb) == 1:
                    # Домножаем результат на -1
                    result, res_k = MUL_ZM_Z(result, res_k)
    return result, res_k


# Z-7 Горевская
# Вычитание целых чисел
# A, B - массивы чисел, b1, b2 - знаки (0 - плюс, 1 - минус)
def SUB_ZZ_Z(A, b1, B, b2):
    # Сравним модули чисел друг с другом функцией COM_NN_D (2 - a > b, 1 - b > a, 0 - a == b)
    com = COM_NN_D(ABS_Z_N(A, b1), ABS_Z_N(B, b2))
    # Функцией POZ_Z_D определяем положительность числа (2 - полож., 1 - отриц., 0 - ноль)
    # Рассмотрим разные случаи:
    # 1) Результат сравнения: оба числа положит.
    if (POZ_Z_D(A, b1) == POZ_Z_D(B, b2) == 2) or (POZ_Z_D(A, b1) == POZ_Z_D(B, b2) == 1):
        if com == 0:
        # Если числа равны -> результат вычитания 0
            res, b = [0], 0
        # Если одно из чисел больше
        elif com == 2 or com == 1:
            # Используем функцию вычитания (она расставит числа в нужном порядке), используем модули чисел
            res = SUB_NN_N(ABS_Z_N(A, b1), ABS_Z_N(B, b2))
            # превращаем результат натуральное в целое
            res, b = TRANS_N_Z(res)
            # если первое число больше и они отрицательны или
            # второе больше и они положительны - меняем знак
            if com == 2 and POZ_Z_D(A, b1) == 1 or com == 1 and POZ_Z_D(A, b1) == 2:
                # Домножаем результат на -1
                res, b = MUL_ZM_Z(res, b)
    # 2) Результат сравнения: числа разных знаков
    elif (POZ_Z_D(A, b1) == 2 and POZ_Z_D(B, b2) == 1) or (POZ_Z_D(A, b1) == 1 and POZ_Z_D(B, b2) == 2):
        # вычитание замещается сложением модулей чисел:
        res = ADD_NN_N(ABS_Z_N(A, b1), ABS_Z_N(B, b2))
        # превращаем результат натуральное в целое
        res, b = TRANS_N_Z(res)
        # Если 2 число > 0, а 1 < 0, то меняем ещё и знак:
        if(POZ_Z_D(A, b1) == 1 and POZ_Z_D(B, b2) == 2):
            # Домножаем результат на -1
            res, b = MUL_ZM_Z(res, b)
    # 3) Результат сравнения: a = 0   b != 0
    elif POZ_Z_D(A, b1) == 0 and POZ_Z_D(B, b2) != 0:
        # Домножаем второе число на -1
        res, b = MUL_ZM_Z(B, b2)
    # 4) Результат сравнения: a != 0   b = 0
    elif (POZ_Z_D(A, b1) != 0) and POZ_Z_D(B, b2) == 0:
        # результат - первое число
        res, b = A, b1
    # 5) Результат сравнения: a = 0   b = 0
    else:
        res, b = [0], 0
    return res, b

# Z-8 Прейгель
# умножение целых чисел
# A, B - массивы чисел, b1, b2 - знаки чисел  (0 - плюс, 1 - минус)
def MUL_ZZ_Z(A, b1, B, b2):
    # используем функцию проверки на положительность
    # если одно из чисел - 0, то новое число тоже 0, иначе перемножаем модули чисел
    if POZ_Z_D(A, b1) == 0 or POZ_Z_D(B, b2) == 0:
        result = [0]
        # превращаем натуральное в целое
        result, res_b = TRANS_N_Z(result)
    else:
        # воспользуемся функцией умножения натуральных чисел (для этого возьмем их модули)
        result = MUL_NN_N(ABS_Z_N(A, b1), ABS_Z_N(B, b2))
        # превращаем натуральное в целое
        result, res_b = TRANS_N_Z(result)
    # если одно число положительное, а другое отрицательное, то знак "минус"
    if (POZ_Z_D(A, b1) == 2 and POZ_Z_D(B, b2) == 1) or (POZ_Z_D(A, b1) == 1 and POZ_Z_D(B, b2) == 2):
        # используем функцию домнажения на -1
        result, res_b = MUL_ZM_Z(result, res_b)
    return result, res_b


# Z-9 Моисеев
# частное от деления целого на целое
# A, B - массивы чисел, b1, b2 - знаки  (0 - плюс, 1 - минус)
def DIV_ZZ_Z(A, b1, B, b2):
    # если числитель ноль
    if POZ_Z_D(A, b1) == 0:
        return [0], 0
    # проверяем равен ли нулю делитель
    if POZ_Z_D(B, b2) != 0:
        # находим частное от деления большего натурального числа на меньшее или
        # равное натуральное с остатком (делитель отличен от нуля), берем числа по модулю
        result = DIV_NN_N(ABS_Z_N(A, b1), ABS_Z_N(B, b2))
        # если делитель - отрицательное и НОД - не второе число, добавляем единицу к результату
        if POZ_Z_D(B, b2) == 1 and GCF_NN_N(ABS_Z_N(A, b1), ABS_Z_N(B, b2)) != ABS_Z_N(B, b2):
            result = ADD_1N_N(result)
        # преобразование натурального в целое
        result, res_b = TRANS_N_Z(result)
        # если числа разных знаков
        if (POZ_Z_D(A, b1) == 1 and POZ_Z_D(B, b2) == 2) or (POZ_Z_D(A, b1) == 2 and POZ_Z_D(B, b2) == 1):
            # используем функцию домнажения на -1
            result, res_b = MUL_ZM_Z(result, res_b)
        return result, res_b
    else:
        return "Делитель равен нулю"


# Z-10 Горевская
# остаток от деления целого на целое
# A, B - массивы чисел, b1, b2 - знаки  (0 - плюс, 1 - минус)
def MOD_ZZ_Z(A, b1, B, b2):
    # если числитель ноль
    if POZ_Z_D(A, b1) == 0:
        return [0], 0
    if POZ_Z_D(B, b2) != 0:
        # используем функцию нахождения остатка от деления нат. чисел
        # (для этого используем модули целых чисел) res - нат. число
        res = MOD_NN_N(ABS_Z_N(A, b1), ABS_Z_N(B, b2))
        # если знаки чисел равны, то нат. число превращаем в целое
        if b1 == b2:
            return TRANS_N_Z(res)
        # если знаки разные, и числитель - отрицательное
        elif b1 == 1:
            # к результату добавляем единицу и превращаем в целое
            res = TRANS_N_Z(ADD_1N_N(res))
            return res
        # если знаки разные, и знаменатель - отрицательное
        else:
            return TRANS_N_Z(res)
    else:
        return "Делитель равен нулю"
