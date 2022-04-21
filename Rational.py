
# Q-1 Черникова
# cокращение дроби
# дано: рац. дробь - числ-ль num и знам-ль denom
# использовать:
# Z-1 ABS_Z_N абсолютная величина числа, результат - нат.число
# N-13 GCF_NN_N НОД нат.чисел
# Z-9 DIV_ZZ_Z частное от деления целого на целое (делитель не ноль)
def RED_Q_Q(num, denom):
    if num != 0:
        # делаем числ-ль натуральным
        num_nat = ABS_Z_N(num)
        # находим НОД натуральных числ-ля и знам-ля
        gcf = GCF_NN_N(num_nat, denom)
        # Z-4 TRANS_N_Z преобразование натурального в целое
        gcf = TRANS_N_Z(gcf)
        # делим цел.числ-ль на цел. НОД
        num = DIV_ZZ_Z(num[0], num[2], gcf[0], gcf[2])
        # делим нат.знам-ль на НОД
        # (N-11 DIV_NN_N частное от деления с остатком нат. числа на меньшее/равное, ненулевое)
        denom = DIV_NN_N(denom[0], denom[1], gcf[0], gcf[0])
        # собираем рац.дробь
        qres = (num, denom)
    else:
        # если числ-ль 0, дробь 0
        qres = 0, 1, 0
    return qres


# Q-2 Селиверстов
# Проверка на целое, если рациональное число является целым, то <да>, иначе <нет>
def INT_Q_B(A, B):
    if len(B) == 1 and B[0] == 1:
        return True
    elif len(A) == 1 and A[0] == 0:
        return True
    elif A == B:
        return True
    else:
        return False
    

# Q-3 Моисеев
# Преобразование целого в дробное
def TRANS_Z_Q(a):
    # возвращает массив [a,b], где
    # a - числитель, b - знаменатель
    t = [a, 1]
    return t


# Q-4 Махаев
# Преобразование дробного в целое (если знаменатель равен 1),
def TRANS_Q_Z(A,B):
    # По хорошему, здесь в начале должна быть функция Q-1,
    # чтобы сделать дробь несократимой, и потом уже преобразовывать в целое
    zero_element = 0
    count_element = 0
    for i in range(len(B)):
        if B[i] == 0:
            zero_element = zero_element + 1
        count_element = count_element + 1
        # Считаем количество элементов и нулевых элементов в знаменателе
    if (zero_element == count_element - 1) and (B[zero_element] == 1):
        # Если количество элементов больше чем количество нулевых элементов на единицу
        # и последний элемент знаменателя равен единице,то возвращаем только числитель
        return A
    
    
# Q-5 Булацкий 
# Сложение дробей
def ADD_QQ_Q(A, B, C, D):
    tempB = B.copy()
    tempD = D.copy()
    sum3 = MUL_NN_N(tempB, tempD)
    sum1 = MUL_ZZ_Z(A, TRANS_N_Z(D))
    sum2 = MUL_ZZ_Z(TRANS_N_Z(B), C)
    temp = ADD_ZZ_Z(sum1, sum2)
    return RED_Q_Q([temp, sum3])


# Q-6 Прейгель
# вычитание дробей
def SUB_QQ_Q(q1, k1, q2, k2):
    #определение знаков и приведение чисел к виду массива(числители и знаменатели)
    Q1 = []
    Q2 = []
    K1 = []
    K2 = []
    if(str(q1)[0] == "-"):
        bq1 = 1
        nq1 = len(str(q1))-1
        for x in range(1, len(str(q1))):
            Q1.append(int(str(q1)[x]))
    else:
        bq1 = 0
        nq1 = len(str(q1))
        for x in str(q1):
            Q1.append(int(x))
    if(str(q2)[0] == "-"):
        bq2 = 1
        nq2 = len(str(q2))-1
        for x in range(1, len(str(q2))):
            Q2.append(int(str(q2)[x]))
    else:
        bq2 = 0
        nq2 = len(str(q2))
        for x in str(q2):
            Q2.append(int(x))
    bk1 = 0
    bk2 = 0
    nk1 = len(str(k1))
    nk2 = len(str(k2))
    for k in str(k1):
        K1.append(int(k))
    for k in str(k2):
        K2.append(int(k))
    #умножение первого числителя на второй знаменатель
    bq1,nq1,Q1 = MUL_ZZ_Z(bq1,nq1,Q1,bk2,nk2,K2)
    #перемножение знаменателей
    K3 = MUL_NN_N(K1, K2)
    #умножение второгт числителя на первый знаменатель
    bq2,nq2,Q2 = MUL_ZZ_Z(bq2,nq2,Q2,bk1,nk1,K1)
    #вычитание второго числителя из первого
    Q3 = SUB_ZZ_Z(Q1, bq1, nq1, Q2, bq2, nq2)
    strk3 = ""
    strq3 = ""
    for x in K3:
        strk3 += str(x)
    for x in Q3:
        strq3 += str(x)
    K3 = int(strk3)
    Q3 = int(strq3)
    #сокращение получившейся дроби
    return RED_Q_Q(Q3, K3) 


# Q-7 Черникова
# умножение дробей
# дано: рац. дроби - числ-ли num1, num2 и знам-ли denom1, denom2
# использовать:
def MUL_QQ_Q(num1, denom1, num2, denom2):
    if num1[2] or num2[2] != [0]:
        # умножение целых числ-й
        qnum = MUL_ZZ_Z(num1[0], num1[1], num1[2], num2[0], num2[1], num2[2])
        # умножение нат. знам-й
        # N-8 MUL_NN_N умножение натуральных чисел
        qdenom = MUL_NN_N(denom1, denom2)
        # сокращаем рац. дробь
        # Q-1 RED_Q_Q cокращение дроби
        qres = RED_Q_Q(qnum, qdenom)
    else:
        # если хб один числ-ль 0, дробь 0
        qres = 0, 1, 0
    return qres
        
    
# Q-8 Счастливая
# Деление дробей (делитель отличен от нуля)
def DIV_QQ_Q(b1, Z1, n1, N1, b2, Z2, N2):
    # Z1, Z2 - числители (целое), N1, N2 - знаменатели (натуральное)
    # b1, b2 - знаки Z1 и Z2 соответственно
    # n1, n2 - номера старшей позиции Z1 и Z2 соответственно
    # Переворачиваем вторую дробь
    t = N2
    N2 = Z2
    Z2 = t
    # Перемножаем числители (целые числа)
    chis = MUL_ZZ_Z(b1, n1, Z1, b2, n2, Z2)
    # Перемножаем знаменатели (натуральные числа)
    znam = MUL_NN_N(N1, N2)
    return chis, znam
