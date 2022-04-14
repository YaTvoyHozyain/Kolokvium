# Q-1: cокращение дроби
# вход: дробь::: знак,ст.поз-я,мас-в цифр целого числ-ля,  ст.поз-я,мас-в цифр нат. знам-ля
# выход: дробь::: кортеж ((цел.числ-ль),(нат.знам-ль))
def RED_Q_Q(b1, n1, A1, n2, A2):
    # ЕСЛИ знам-ль 0, вывод 'Can't devide by zero.'
    # ИНАЧЕ ЕСЛИ числ-ль 0, вывод 0
    if A2 == [0]:
        print("Can't divide by zero.")
    else:
        if A1==[0]:
            Q = (0, 1, [0])
        else:
            # ИНАЧЕ числ-ль сделать натуральным (Z-1) и найти НОД нат. чисел GCD (N-13)
            Q1 = ABS_Z_N(b1, n1, A1)
            GCD = GCF_NN_N(Q1[0], Q1[1])
            # цел. числ-ль разделить на НОД(натуральное, явл-ся целым) (Z-9)
            Q1 = DIV_ZZ_Z(b1, n1, A1,GCD[0],GCD[1])
            # нат. знам-ль разделить на НОД(натуральное, явл-ся целым) (N-11)
            Q2 = DIV_NN_N(n2,A2,GCD[0],GCD[1])
            # соединить цел.числ-ль, нат.знам-ль в 2х уровневый кортеж...godddamn
            Q = ( (Q1, Q2) )
        return Q

# Q-3    
# Преобразование целого в дробное
def TRANS_Z_Q(a):
    # возвращает массив [a,b], где
    # a - числитель, b - знаменатель
    t = [a, 1]
    return t

# Q-4 Преобразование дробного в целое (если знаменатель равен 1),
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

# Q - 6 - вычитание дробей
def SUB_QQ_Q(q1, k1, q2, k2):
    # приведение к общему знаменателю обоих чисел
    q1 = q1 * k2 # (здесь и в двух последующих выражениях вместо * должна быть функция умножения натуральных чисел MUL_NN_N)
    q2 = q2 * k1 
    k3 = k1 * k2
    # вычитание второго числителя из первого
    q3 = q1 - q2 #здесь должна быть функция вычитания целых чисел SUB_ZZ_Z
    # сокращение получившейся дроби
    g = math.gcd(k3, q3)#(это и три следующих выражения надо заменить на одно с функцией сокращения дроби RED_Q_Q)
    k3 = k3 // g
    q3 = q3 // g
    return (q3, k3)

# Q-7: умножение дробей
# вход: дробь1, дробь2::: знак,ст.поз-я,мас-в цифр целого числ-ля,  ст.поз-я,мас-в цифр нат. знам-ля
# выход: дробь::: кортеж ((цел.числ-ль),(нат.знам-ль))
def MUL_QQ_Q(b1, n1, A1, n2, A2, b3, n3, A3, n4, A4):
    if A2 != [0] and A4 != [0]:
        if A1 != [0] and A3 != [0]:
            # ИНАЧЕ умножение цел. числителей (исп.Z-8)
            Q1 = MUL_ZZ_Z(b1, n1, A1, b3, n3, A3,)
            # умножение натур. знаменателей (исп.N-8)
            Q2 = MUL_NN_N(n2,A2,n4,A4)
            # сокращение рац. дроби (исп.Q-1)
            Q = RED_Q_Q(Q1[0], Q1[1], Q1[2], Q2[0], Q2[1])
        else:
            Q = (0, 1, [0])
        return Q
    # ЕСЛИ хотя бы один знам-ль 0, вывод 'Can't divide by zero.'
    # ИНАЧЕ ЕСЛИ хотя бы один числ-ль 0, вывод 0
    else:
        print("Can't divide by zero.")
