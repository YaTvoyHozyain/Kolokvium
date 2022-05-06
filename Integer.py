class Integer:
    """
        Целое число

        ввод числа:
        xy = Integer(input())
    """

    def __init__(self, number='0'):
        number = str(number)
        if number[0] in '-123456789' or (number[0] == '0' and len(number) == 1):
            if number[0] == "-":
                number = number[1:]
                self.pos = False
            elif number[0] in "0123456789":
                self.pos = True
            number = number[::-1]
            self.numbers = []
            for i in number:
                if i in "0123456789":
                    self.numbers.append(int(i))
                else:
                    raise Exception("Invalid initial data entered")
        else:
            raise Exception("Invalid initial data entered")

    def __str__(self):
        """Возврщает целое число строкой"""
        if self.pos:
            return ''.join([str(i) for i in reversed(self.numbers)])
        else:
            return '-' + ''.join([str(i) for i in reversed(self.numbers)])
        

# Z-1 Селиверстов
# Абсолютная величина числа
# A - целое число
def ABS_Z_N(A):
    C1 = Integer(str(A))

    if C1.pos:
        C1 = Natural(C1)
    else:
        C1.pos = True
        C1 = Natural(C1)

    return C1


# Z-2 Михайлова
# Определение положительности числа
# A - целое число
def POZ_Z_D(A):
    C1 = Integer(str(A))

    # если число ноль возвращаем 0
    if len(C1.numbers) == 1 and C1.numbers[0] == 0:
        return 0
    # если число положительное возвращаем 2
    elif C1.pos:
        return 2
    # если число отрицательное возвращаем 1
    else:
        return 1


# Z-3 Махаев
# Умножение целого на -1
# A - целое число
def MUL_ZM_Z(A):
    C1 = Integer(str(A))

    if len(C1.numbers) == 1 and C1.numbers[0] == 0:
        return Integer('0')
    if C1.pos:
        C1.pos = False
    elif not C1.pos:
        C1.pos = True
    return C1


# Z-4 Счастливая
# Преобразование натурального в целое
# A - натуральное число
def TRANS_N_Z(A):
    # превращаем натуральное в целое, конкруктор всё сделает сам
    return Integer(str(A))


# Z-5 Грицкевич
# Преобразование целого неотрицательного числа в натуральное
# A - целое число
def TRANS_Z_N(A):
    if A.pos:
        return Natural(str(A))
    else:
        raise Exception("The number must be non-negative")


# Z-6 Булацкий
# Сложение целых чисел
# A, B - целые числа
# result - итоговое целое число
def ADD_ZZ_Z(A, B):
    C1 = Integer(str(A))
    C2 = Integer(str(B))
    # Если оба числа равны нулю (POZ_Z_D - проверка на положительность), то их сумма тоже будет равна 0
    if POZ_Z_D(C1) == 0 and POZ_Z_D(C2) == 0:
        result = Integer('0')
    else:
        # если числа одного знака
        if POZ_Z_D(C1) == POZ_Z_D(C2):
            # Используем функцию сложения натуральных чисел (для этого берем модули чисел)
            result = ADD_NN_N(ABS_Z_N(C1), ABS_Z_N(C2))
            # превращаем натуральное в целое
            result = TRANS_N_Z(result)
            # Если оба числа отрицательные (POZ_Z_D - проверка на положительность)
            if POZ_Z_D(C1) == 1:
                # Домножаем результат на -1
                result = MUL_ZM_Z(result)
        # Если у чисел разные знаки
        else:
            # Сравниваем два числа по модулю
            raz = COM_NN_D(ABS_Z_N(C1), ABS_Z_N(C2))
            # Если а > b то
            if raz == 2:
                # Вычитаем из первого большего натурального числа второе меньшее
                result = SUB_NN_N(ABS_Z_N(C1), ABS_Z_N(C2))
                # превращаем натуральное в целое
                result = TRANS_N_Z(result)
                # Если первое число отрицательное
                if POZ_Z_D(C1) == 1:
                    # Домножаем результат на -1
                    result = MUL_ZM_Z(result)
            # Если а < b то
            else:
                # Вычитаем из второго большего натурального числа первое меньшее
                result = SUB_NN_N(ABS_Z_N(C2), ABS_Z_N(C1))
                # превращаем натуральное в целое
                result = TRANS_N_Z(result)
                # Если второе число отрицательное
                if POZ_Z_D(C2) == 1:
                    # Домножаем результат на -1
                    result = MUL_ZM_Z(result)
    return result


# Z-7 Горевская
# Вычитание целых чисел
# A, B - целые числа
def SUB_ZZ_Z(A, B):
    C1 = Integer(str(A))
    C2 = Integer(str(B))
    # Сравним модули чисел друг с другом функцией COM_NN_D (2 - a > b, 1 - b > a, 0 - a == b)
    com = COM_NN_D(ABS_Z_N(C1), ABS_Z_N(C2))
    # Функцией POZ_Z_D определяем положительность числа (2 - полож., 1 - отриц., 0 - ноль)
    # Рассмотрим разные случаи:
    # 1) Результат сравнения: оба числа положит.
    if (POZ_Z_D(C1) == POZ_Z_D(C2) == 2) or (POZ_Z_D(C1) == POZ_Z_D(C2) == 1):
        if com == 0:
            # Если числа равны -> результат вычитания 0
            res = Integer('0')
        # Если одно из чисел больше
        elif com == 2 or com == 1:
            # Используем функцию вычитания в зависимости от того, какое число больше, используем модули чисел
            if com == 2:
                res = SUB_NN_N(ABS_Z_N(C1), ABS_Z_N(C2))
            else:
                res = SUB_NN_N(ABS_Z_N(C2), ABS_Z_N(C1))
            # превращаем результат натуральное в целое
            res = TRANS_N_Z(res)
            # если первое число больше и они отрицательны или
            # второе больше и они положительны - меняем знак
            if (com == 2 and POZ_Z_D(C1) == 1) or (com == 1 and POZ_Z_D(C1) == 2):
                # Домножаем результат на -1
                res = MUL_ZM_Z(res)
    # 2) Результат сравнения: числа разных знаков
    elif (POZ_Z_D(C1) == 2 and POZ_Z_D(C2) == 1) or (POZ_Z_D(C1) == 1 and POZ_Z_D(C2) == 2):
        # вычитание замещается сложением модулей чисел:
        res = ADD_NN_N(ABS_Z_N(C1), ABS_Z_N(C2))
        # превращаем результат натуральное в целое
        res = TRANS_N_Z(res)
        # Если 2 число > 0, а 1 < 0, то меняем ещё и знак:
        if POZ_Z_D(C1) == 1 and POZ_Z_D(C2) == 2:
            # Домножаем результат на -1
            res = MUL_ZM_Z(res)
    # 3) Результат сравнения: a = 0   b != 0
    elif POZ_Z_D(C1) == 0 and POZ_Z_D(C2) != 0:
        # Домножаем второе число на -1
        res = MUL_ZM_Z(C2)
    # 4) Результат сравнения: a != 0   b = 0
    elif POZ_Z_D(C1) != 0 and POZ_Z_D(C2) == 0:
        # результат - первое число
        res = C1
    # 5) Результат сравнения: a = 0   b = 0
    else:
        res = Integer('0')
    return res


# Z-8 Прейгель
# умножение целых чисел
# A, B - целые числа
def MUL_ZZ_Z(A, B):
    C1 = Integer(str(A))
    C2 = Integer(str(B))
    # используем функцию проверки на положительность
    # если одно из чисел - 0, то новое число тоже 0, иначе перемножаем модули чисел
    if POZ_Z_D(C1) == 0 or POZ_Z_D(C2) == 0:
        result = Integer('0')
        # превращаем натуральное в целое
        result = TRANS_N_Z(result)
    else:
        # воспользуемся функцией умножения натуральных чисел (для этого возьмем их модули)
        result = MUL_NN_N(ABS_Z_N(C1), ABS_Z_N(C2))
        # превращаем натуральное в целое
        result = TRANS_N_Z(result)
    # если одно число положительное, а другое отрицательное, то знак "минус"
    if (POZ_Z_D(C1) == 2 and POZ_Z_D(C2) == 1) or (POZ_Z_D(C1) == 1 and POZ_Z_D(C2) == 2):
        # используем функцию домнажения на -1
        result = MUL_ZM_Z(result)
    return result


# Z-9 Моисеев
# частное от деления целого на целое
# A, B - целые числа
def DIV_ZZ_Z(A, B):
    C1 = Integer(str(A))
    C2 = Integer(str(B))

    # проверяем равен ли нулю делитель
    if POZ_Z_D(C2) != 0:
        # если числитель ноль
        if POZ_Z_D(C1) == 0:
            return Integer('0')
        # находим частное от деления большего натурального числа на меньшее или
        # равное натуральное с остатком (делитель отличен от нуля), берем числа по модулю
        result = DIV_NN_N(ABS_Z_N(C1), ABS_Z_N(C2))
        # если делимое - отрицательное и НОД - не второе число, добавляем единицу к результату
        if POZ_Z_D(C1) == 1 and (COM_NN_D(GCF_NN_N(ABS_Z_N(C1), ABS_Z_N(C2)), ABS_Z_N(C2)) != 0):
            result = ADD_1N_N(result)
        # преобразование натурального в целое
        result = TRANS_N_Z(result)
        # если числа разных знаков
        if (POZ_Z_D(C1) == 1 and POZ_Z_D(C2) == 2) or (POZ_Z_D(C1) == 2 and POZ_Z_D(C2) == 1):
            # используем функцию домнажения на -1
            result = MUL_ZM_Z(result)
        return result
    else:
        raise Exception("divisor is zero")


# Z-10 Горевская
# остаток от деления целого на целое
# A, B - целые числа
def MOD_ZZ_Z(A, B):
    # копирование данных
    C1 = Integer(str(A))
    C2 = Integer(str(B))
    # остаток = делимое - неполное частное * делитель
    if POZ_Z_D(C2) != 0:
        return SUB_ZZ_Z(C1, MUL_ZZ_Z(C2, DIV_ZZ_Z(C1, C2)))
    # если делитель = нолю, выдать ошибку
    else:
        raise Exception("divisor is zero")
