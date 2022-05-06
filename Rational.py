class Rational:
    """
    Рациональное число
    """

    # это конструктор, он собирает объект, в этом случае рациональное число из строки
    def __init__(self, numbers='0'):
        numbers = str(numbers)
        if '/' in numbers:
            a = numbers.split('/')
            self.numer = Integer(a[0])
            if not NZER_N_B(Natural(a[1])):
                raise Exception("denominant is zero")
            self.denom = Natural(a[1])
            self.pos = self.numer.pos
        else:
            self.numer = Integer(numbers)
            self.denom = Natural(1)
            self.pos = self.numer.pos

    def __str__(self):
        if POZ_Z_D(self.numer) == 0:
            return '0'
        elif COM_NN_D(self.denom, Natural(1)) == 0:
            return '{}'.format(self.numer)
        else:
            return '{}/{}'.format(self.numer, self.denom)


# Q-1 Черникова
# Сокращение дроби
# использовать:
# {Z-1, ABS_Z_N} Aбсолютная величина числа, результат - нат.число
# {N-13, GCF_NN_N} НОД нат.чисел
# {Z-9, DIV_ZZ_} Частное от деления целого на целое (делитель не ноль)
# вход: A - рациональное число
# выход: рациональное число
def RED_Q_Q(A):
    C1 = Rational(str(A))
    # проверяем чилитель на 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(C1.numer) != 0:
        # делаем числитель натуральным {Z-1, ABS_Z_N}
        num_nat = ABS_Z_N(C1.numer)
        # находим НОД натуральных числителя и знаменателя {N-13, GCF_NN_N}
        gcf = GCF_NN_N(num_nat, C1.denom)
        # делим натуральный знаменатель на натуральный НОД {N-11, DIV_NN_N}
        denom = DIV_NN_N(C1.denom, gcf)
        # преобразуем натуральный НОД в целое число {Z-4, TRANS_N_Z}
        gcf = TRANS_N_Z(gcf)
        # делим целый числитель на целый НОД {Z-9, DIV_ZZ_Z}
        num = DIV_ZZ_Z(C1.numer, gcf)
        # конструктор класса принимает на вход только строку в определенной форме
        # именно таким образом можно преобразовать целое и натуральное число в одно рациональное
        s = '{}/{}'.format(num, denom)
        return Rational(s)
    else:
        # если числитель 0, вернуть нулевую дробь со знаменателем 1
        # конструктор сам всё сделает
        return Rational('0')


# Q-2 Селиверстов
# Проверка на целое, если рациональное число является целым, то 1, иначе 0
# вход: рациональное число
# выход: 0 или 1
def INT_Q_B(A):
    C1 = Rational(str(A))
    # проверяем целый числитель на 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(C1.numer) != 0:
        # сокращаем дробь {Q-1, RED_Q_Q}
        C1 = RED_Q_Q(C1)
        # если знаменатель равен 1 - дробь целая {N-1, COM_NN_D}
        if COM_NN_D(C1.denom, Natural(1)) == 0:
            return True
        else:
            return False
    # если числитель 0 - дробь 0, т.е. целое
    else:
        return True


# Q-3 Моисеев
# Преобразование целого в дробное
# вход: A - целое число
# выход: рациональное число
def TRANS_Z_Q(A):
    C1 = Integer(str(A))
    # если целое число не 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(C1) != 0:
        # в числитель - массив цифр, в знак дроби - знак целого, в знаменатель - 1
        res = Rational('0/1')
        res.numer = C1
        res.pos = C1.pos
        return res
    # если числитель 0 - дробь 0:
    else:
        # иначе вернуть 0 в виде дроби (1 в знаменателе, тк он не мб 0)
        return Rational('0')


# Q-4 Махаев
# Преобразование дробного в целое (если знаменатель равен 1)
# вход: A - рациональное число
# выход: целое число
def TRANS_Q_Z(A):
    C1 = Rational(str(A))
    # сократим дробь {Q-1, RED_Q_Q}
    C1 = RED_Q_Q(C1)
    # проверим дробь на целое, результат сохраним {Q-2, INT_Q_B}
    # INT_Q_B вернет True, если дробь 0 или её знаменатель 1, иначе False
    # если результат равен True - дробь целая {N-1, COM_NN_D}
    if INT_Q_B(C1):
        # если дробь(числитель) не 0, вернуть числитель и знак {Z-2, POZ_Z_D}
        if POZ_Z_D(C1.numer) != 0:
            return C1.numer
        else:
            # иначе вернуть целое число 0 с положительным знаком
            return Integer(0)
    else:
        raise Exception("This fraction is not integer.")


# Q-5 Булацкий
# Сложение дробей
# использовать:
# {N-14, LCM_NN_N} НОК натуральных чисел
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# {Z-6, ADD_ZZ_Z} Сложение целых чисел
# вход: A, B - рациональные числа
# выход: Рациональное число
def ADD_QQ_Q(A, B):
    C1 = Rational(str(A))
    C2 = Rational(str(B))
    # находим НОК знаменателей {N-14, LCM_NN_N}
    lcm = LCM_NN_N(C1.denom, C2.denom)
    # находим коэффициенты для домножения на числители: делим НОК на каждый знаменатель {N-11, DIV_NN_N}
    koef1 = DIV_NN_N(lcm, C1.denom)
    koef2 = DIV_NN_N(lcm, C2.denom)
    # делаем коэффициенты целыми числами {Z-4, TRANS_N_Z}
    koef1 = TRANS_N_Z(koef1)
    koef2 = TRANS_N_Z(koef2)
    # умножаем их на числители: num1 на k2, num2 на k1 {Z-8, MUL_ZZ_Z}
    num1 = MUL_ZZ_Z(C1.numer, koef1)
    num2 = MUL_ZZ_Z(C2.numer, koef2)
    # складываем числители {Z-6, ADD_ZZ_Z}
    numres = ADD_ZZ_Z(num1, num2)
    # если полученный числитель не 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(numres) != 0:
        # сократим полученную дробь {Q-1, RED_Q_Q}
        # опять же просто способ получения рационального числа как экземпляра класса
        # то есть особенности синтаксиса
        s = '{}/{}'.format(numres, lcm)
        qres = Rational(s)
        # сокращаем дробь
        qres = RED_Q_Q(qres)
        return qres
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,тк знаменатель не может быть  0) {Q-3, TRANS_Z_Q}
        return Rational('0')


# Q-6 Прейгель
# Вычитание дробей
# использовать:
# {N-14, LCM_NN_N} НОК натуральных чисел
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# {Z-7, SUB_ZZ_Z} Вычитание целых чисел
# вход: A, B - рациональные числа
# выход: рациональное число
def SUB_QQ_Q(A, B):
    C1 = Rational(str(A))
    C2 = Rational(str(B))
    # находим НОК знаменателей
    lcm = LCM_NN_N(C1.denom, C2.denom)
    # находим коэффициенты для домножения на числители: делим НОК на каждый знаменатель {N-11, DIV_NN_N}
    koef1 = DIV_NN_N(lcm, C1.denom)
    koef2 = DIV_NN_N(lcm, C2.denom)
    # делаем коэффициенты целыми числами {Z-4, TRANS_N_Z}
    koef1 = TRANS_N_Z(koef1)
    koef2 = TRANS_N_Z(koef2)
    # умножаем их на числители: num1 на k2, num2 на k1 {Z-8, MUL_ZZ_Z}
    num1 = MUL_ZZ_Z(C1.numer, koef1)
    num2 = MUL_ZZ_Z(C2.numer, koef2)
    # вычитаем числители {Z-7, SUB_ZZ_Z}
    numres = SUB_ZZ_Z(num1, num2)
    # если полученный числитель не 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(numres) != 0:
        # сократим полученную дробь {Q-1, RED_Q_Q}
        # опять же просто способ получения рационального числа как экземпляра класса
        # то есть особенности синтаксиса
        s = '{}/{}'.format(numres, lcm)
        qres = Rational(s)
        # сокращаем дробь
        qres = RED_Q_Q(qres)
        return qres
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,тк знаменатель не мб 0) {Q-3,  TRANS_Z_Q}
        return Rational('0')


# Q-7 Черникова
# Умножение дробей
# использовать:
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# вход: A, B - рациональные числа
# выход: рациональное число
def MUL_QQ_Q(A, B):
    C1 = Rational(str(A))
    C2 = Rational(str(B))
    # если числители не равны 0 {Z-2, POZ_Z_D}
    if POZ_Z_D(C1.numer) != 0 and POZ_Z_D(C2.numer) != 0:
        # умножим целые числители {Z-8, MUL_ZZ_Z}
        qnum = MUL_ZZ_Z(C1.numer, C2.numer)
        # умноженим натуральные знаменатели {N-8, MUL_NN_N}
        qdenom = MUL_NN_N(C1.denom, C2.denom)
        # сократим полученную дробь {Q-1, RED_Q_Q}
        # получаем нужную дробь
        s = '{}/{}'.format(qnum, qdenom)
        qres = Rational(s)
        # сокращаем её
        qres = RED_Q_Q(qres)
        return qres
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,т.к. знаменатель не мб 0)
        return Rational('0')


# Q-8 Счастливая
# Деление дробей (делитель отличен от нуля)
# использовать:
# {Z-8, MUL_ZZ_Z} Умножение целых чисел
# вход: A, B - рациональные числа
# выход: рациональное число
def DIV_QQ_Q(A, B):
    C1 = Rational(str(A))
    C2 = Rational(str(B))
    # если числители не равны 0
    if POZ_Z_D(C1.numer) != 0 and POZ_Z_D(C2.numer) != 0:
        # переворачиваем вторую дробь
        # так как числитель целое, а знаменатель натуральное, то нужно сохранить знак для, того чтобы потом его присвоить, когда дробь перевернется
        temp = C2.numer.pos
        C2.numer, C2.denom = TRANS_N_Z(C2.denom), ABS_Z_N(C2.numer)
        C2.numer.pos = temp
        # умножим целые числители {Z-8, MUL_ZZ_Z}
        qnum = MUL_ZZ_Z(C1.numer, C2.numer)
        # умноженим натуральные знаменатели {N-8, MUL_NN_N}
        qdenom = MUL_NN_N(C1.denom, C2.denom)
        # сократим полученную дробь {Q-1, RED_Q_Q}
        # Получаем нужную дробь
        s = '{}/{}'.format(qnum, qdenom)
        qres = Rational(s)
        # сокращаем дробь
        qres = RED_Q_Q(qres)
        return qres
    else:
        # иначе вернуть нулевую дробь [0], 0, [1] (1,т.к. знаменатель не мб 0)
        return Rational('0')
