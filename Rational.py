# Q-1 Черникова
# Сокращение дроби
# использовать:
# {Z-1, ABS_Z_N} Aбсолютная величина числа, результат - нат.число
# {N-13, GCF_NN_N} НОД нат.чисел
# {Z-9, DIV_ZZ_} Частное от деления целого на целое (делитель не ноль)
# вход: num, numb, denom - массив цифр числителя, знак дроби, массив цифр знаменателя
# выход: массив цифр числителя, знак дроби, массив цифр знаменателя
def RED_Q_Q(num, numb, denom):
    # проверяем чилитель на 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(num, numb) != 0:
        # делаем числитель натуральным {Z-1, ABS_Z_N}
        num_nat = ABS_Z_N(num, numb)
        # находим НОД натуральных числителя и знаменателя {N-13, GCF_NN_N}
        gcf = GCF_NN_N(num_nat, denom)
        # делим натуральный знаменатель на натуральный НОД {N-11, DIV_NN_N}
        denom = DIV_NN_N(denom, gcf)
        # преобразуем натуральный НОД в целое число {Z-4, TRANS_N_Z}
        gcf = TRANS_N_Z(gcf)
        # делим целый числитель на целый НОД {Z-9, DIV_ZZ_Z}
        num = DIV_ZZ_Z(num, numb, gcf[0], gcf[1])
        return num, numb, denom
    else:
        # если числитель 0, вернуть нулевую дробь [0], 0, [1] (1,тк знаменатель не мб 0) {Q-3,  TRANS_Z_Q}
        qzero = TRANS_Z_Q(num, numb)
        return qzero[0], qzero[1], qzero[2]


# Q-2 Селиверстов
# Проверка на целое, если рациональное число является целым, то 1, иначе 0
# вход: num, numb, denom - массив цифр числителя, знак дроби, массив цифр знаменателя
# выход: 0 или 1
def INT_Q_B(num, numb, denom):
    # проверяем целый числитель на 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(num, numb) != 0:
        # сокращаем дробь {Q-1, RED_Q_Q}
        q = RED_Q_Q(num, numb, denom)
        # если знаменатель равен 1 - дробь целая {N-1, COM_NN_D}
        if COM_NN_D(q[2], [1]) == 1:
            return 1
        else:
            return 0
    # если числитель 0 - дробь 0, т.е. целое
    else:
        return 1
    

# Q-3 Моисеев
# Преобразование целого в дробное
# вход: A, b - массив цифр целого числа, его знак
# выход: массив цифр числителя, знак дроби, массив цифр знаменателя
def TRANS_Z_Q(A, b):
    # если целое число не 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(A, b) != 0:
        # в числитель - массив цифр, в знак дроби - знак целого, в знаменатель - 1
        num, numb, denom = A, b, [1]
        return num, numb, denom
    # если числитель 0 - дробь 0:
    else:
        # иначе вернуть 0 в виде дроби (1 в знаменателе, тк он не мб 0)
        return [0], 0, [1]

# Q-4 Махаев
# Преобразование дробного в целое (если знаменатель равен 1)
# вход: num, numb, denom - массив цифр числителя, знак дроби, массив цифр знаменателя
# выход: массив цифр целого числа, его знак
def TRANS_Q_Z(num, numb, denom):
    # проверим дробь на целое, результат сохраним {Q-2, INT_Q_B}
    # INT_Q_B вернет 1, если дробь 0 или её знаменатель 1, иначе 2
    result1 = INT_Q_B(num, numb, denom)
    # если результат равен 1 - дробь целая {N-1, COM_NN_D}
    if COM_NN_D([result1], [1]) == 1:
        # если дробь(числитель) не 0, вернуть числитель и знак {Z-2, POZ_Z_D}
        if POZ_Z_D(num, numb) != 0:
            return num, numb
        else:
            # иначе сделать числитель целым числом 0 со знаком 0 {Z-4, TRANS_N_Z}
            qzero = TRANS_N_Z(num)
            return qzero[0], qzero[1]
    else:
        print("This fraction is NOT integer.")

    
# Q-5 Булацкий 
# Сложение дробей
# использовать:
# {N-14, LCM_NN_N} НОК натуральных чисел
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# {Z-6, ADD_ZZ_Z} Сложение целых чисел
# вход: num1, num1b, denom1 - массив цифр числителя 1, знак дроби 1, массив цифр знаменателя 1
# num2, num2b, denom2 - массив цифр числителя 2, знак дроби 2, массив цифр знаменателя 2
# выход: массив цифр числителя, знак дроби, массив цифр знаменателя
def ADD_QQ_Q(num1, numb1, denom1, num2, numb2, denom2):
    # находим НОК знаменателей {N-14, LCM_NN_N}
    lcm = LCM_NN_N(denom1, denom2)
    # находим коэффициенты для домножения на числители: делим НОК на каждый знаменатель {N-11, DIV_NN_N}
    koef1 = DIV_NN_N(lcm, denom1)
    koef2 = DIV_NN_N(lcm, denom2)
    # делаем коэффициенты целыми числами {Z-4, TRANS_N_Z}
    koef1 = TRANS_N_Z(koef1)
    koef2 = TRANS_N_Z(koef2)
    # умножаем их на числители: num1 на k2, num2 на k1 {Z-8, MUL_ZZ_Z}
    num1 = MUL_ZZ_Z(num1, numb1, koef2[0], koef2[1])
    num2 = MUL_ZZ_Z(num2, numb2, koef1[0], koef1[1])
    # складываем числители {Z-6, ADD_ZZ_Z}
    numres = ADD_ZZ_Z(num1[0], num1[1], num2[0], num2[1])
    # если полученный числитель не 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(numres[0], numres[1]) != 0:
        # сократим полученную дробь {Q-1, RED_Q_Q}
        qres = RED_Q_Q(numres[0], numres[1], lcf)
        return qres[0], qres[1], qres[2]
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,тк знаменатель не мб 0) {Q-3, TRANS_Z_Q}
        qzero = TRANS_Z_Q(num, numb)
        return qzero[0], qzero[1], qzero[2]


# Q-6 Прейгель
# Вычитание дробей
# использовать:
# {N-14, LCM_NN_N} НОК натуральных чисел
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# {Z-7, SUB_ZZ_Z} Вычитание целых чисел
# вход: num1, num1b, denom1 - массив цифр числителя 1, знак дроби 1, массив цифр знаменателя 1
# num2, num2b, denom2 - массив цифр числителя 2, знак дроби 2, массив цифр знаменателя 2
# выход: массив цифр числителя, знак дроби, массив цифр знаменателя
def SUB_QQ_Q(num1, numb1, denom1, num2, numb2, denom2):
    # находим НОК знаменателей
    lcm = LCM_NN_N(denom1, denom2)
    # находим коэффициенты для домножения на числители: делим НОК на каждый знаменатель {N-11, DIV_NN_N}
    koef1 = DIV_NN_N(lcm, denom1)
    koef2 = DIV_NN_N(lcm, denom2)
    # делаем коэффициенты целыми числами {Z-4, TRANS_N_Z}
    koef1 = TRANS_N_Z(koef1)
    koef2 = TRANS_N_Z(koef2)
    # умножаем их на числители: num1 на k2, num2 на k1 {Z-8, MUL_ZZ_Z}
    num1 = MUL_ZZ_Z(num1, numb1, koef2[0], koef2[1])
    num2 = MUL_ZZ_Z(num2, numb2, koef1[0], koef1[1])
    # вычитаем числители {Z-7, SUB_ZZ_Z}
    numres = SUB_ZZ_Z(num1[0], num1[1], num2[0], num2[1])
    # если полученный числитель не 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(numres[0], numres[1]) != 0:
        # сократим полученную дробь {Q-1, RED_Q_Q}
        qres = RED_Q_Q(numres[0], numres[1], lcf)
        return qres[0], qres[1], qres[2]
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,тк знаменатель не мб 0) {Q-3,  TRANS_Z_Q}
        qzero = TRANS_Z_Q(num, numb)
        return qzero[0], qzero[1], qzero[2]


# Q-7 Черникова
# Умножение дробей
# использовать:
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# вход: num1, num1b, denom1 - массив цифр числителя 1, знак дроби 1, массив цифр знаменателя 1
# num2, num2b, denom2 - массив цифр числителя 2, знак дроби 2, массив цифр знаменателя 2
# выход: массив цифр числителя, знак дроби, массив цифр знаменателя
def MUL_QQ_Q(num1, num1b, denom1, num2, num2b, denom2):
    # если числители не равны 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(num1, num1b) != 0 and POZ_Z_D(num2, num2b) != 0:
        # умножим целые числители {Z-8, MUL_ZZ_Z}
        qnum = MUL_ZZ_Z(num1, num1b, num2, num2b)
        # умноженим натуральные знаменатели {N-8, MUL_NN_N}
        qdenom = MUL_NN_N(denom1, denom2)
        # сократим полученную дробь {Q-1, RED_Q_Q}
        qres = RED_Q_Q(qnum[0], qnum[1], qdenom)
        return qres[0], qres[1], qres[2]
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,т.к. знаменатель не мб 0) {Q-3,  TRANS_Z_Q}
        qzero = TRANS_Z_Q(num, numb)
        return qzero[0], qzero[1], qzero[2]
        
    
# Q-8 Счастливая
# Деление дробей (делитель отличен от нуля)
# использовать:
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# вход: num1, num1b, denom1 - массив цифр числителя 1, знак дроби 1, массив цифр знаменателя 1
# num2, num2b, denom2 - массив цифр числителя 2, знак дроби 2, массив цифр знаменателя 2
# выход: массив цифр числителя, знак дроби, массив цифр знаменателя
def DIV_QQ_Q(num1, num1b, denom1, num2, num2b, denom2):
    # если числители не равны 0
    if POZ_Z_D(num1, num1b) != 0 and POZ_Z_D(num2, num2b) != 0:
        # переворачиваем вторую дробь
        num2, denom2 = denom2, num2
        # умножим целые числители {Z-8, MUL_ZZ_Z}
        qnum = MUL_ZZ_Z(num1, num1b, num2, num2b)
        # умноженим натуральные знаменатели {N-8, MUL_NN_N}
        qdenom = MUL_NN_N(denom1, denom2)
        # сократим полученную дробь {Q-1, RED_Q_Q}
        qres = RED_Q_Q(qnum[0], qnum[1], qdenom)
        return qres[0], qres[1], qres[2]
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,т.к. знаменатель не мб 0) {Q-3,  TRANS_Z_Q}
        qzero = TRANS_Z_Q(num, numb)
        return qzero[0], qzero[1], qzero[2]
