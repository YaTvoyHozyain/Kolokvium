# P-1: сложение многочленов
# вход: многочлен1, многочлен2::: степень многочлена, массив рац. коэффициентов
# выход: кортеж (степень, (рац.коэф-ты))
# здесь подразумевается, что массив рац. коэф-в имеет вид q1[i]=[((b1,n1,[A1]),(n2,[A2])), ((b21,n21,[A21]),(n22,[A22])), ... ]
def ADD_PP_P(L,q1,O,q2):
    # находим степень многочлена
    m = DEG_P_N(L)
    m1 = DEG_P_N(q1)
    n = DEG_P_N(O)
    n1 = DEG_P_N(q2)
    err = 0
    # проверка назанаменатель!=0
    for i in range(L):
        if m == 0:
            print("Error P-1")
            err = 1
    for i in range(O):
        if n == 0:
            print("Error P-1")
            err = 1
    if err != 0:
        # решение
        if m > n:
            raz = m - n
            for i in range((raz)):
                q2.insert(0, ((0, 1, [0]), (0, 1, [0])) )
        elif m < n:
            raz = n - m
            for i in range((raz)):
                q1.insert(0, ((0, 1, [0]), (0, 1, [0])) )
        for i in range(max(m1, m2)):
            q[i] = ADD_QQ_Q(q1[i], q2[i])
            q.insert(0, q[i])
        q = (len(q), q)
        return q

# P-2: вычитание многочленов
# дано: многочлены - старш. ст. m1, m2 и массивы рац. коэф-в C1, C2
# использовать:
# Q-6 SUB_QQ_Q вычитание дробей
def SUB_PP_P(m1,C1,m2,C2):
    # степень 1го многочл. больше ст. 2го
    if(m1>m2):
        # слева направо переносим коэф-ты 1го многочл., тк из них вычитаются нулевые коэф-ты 2го
        for i in range(m1-1,m2-1,-1):
            Cres.append(C1[i])
        # затем из оставшихся коэф-в 1го многочл. вычитаем коэф-ты 2го
        for i in range(m2-1, -1, -1):
            Cres.append( SUB_QQ_Q( C1[i], C2[i]) )
    # степень 1го многочл. меньше ст. 2го
    elif(m1<m2):
        # слева направо переносим коэф-ты 2го многочл. с минусом, тк они вычитаются из нулевых коэф-в 1го
        for i in range(m2-1,m1-1,-1):
            # делаем список,кот. можно изменять
            С2list[i] = list(С2[i])
            # берем числ-ль дробного коэф-та, если дробь это (num, denom) и
            # меняем знак у числителя, если num = (b,n,A)
            if С2list[i][0][0] == 0:
                С2list[i][0][0] == 1
            else:
                С2list[i][0][0] == 0
            С2[i] = (С2list[i])
        # затем из коэф-в 1го многочл. вычитаем оставшиеся коэф-ты 2го
        for i in range(m1 - 1, -1, -1):
            Cres.append( SUB_QQ_Q( C1[i][0],C1[i][1], C2[i][0], C2[i][0]))
    mres = len(Cres)
    return mres, Cres
    
# P-3: умножение многочлена на рациональное число
# дано: многочлен - старш. ст. m1 и массив рац. коэф-в C1; рац. число q
# использовать:
# Q-7 MUL_QQ_Q умножение дробей
def MUL_PQ_P(m1, C1, q):
    for i in range(m1):
        # MUL_QQ_ умножает числь-ль и знам-ль каждой дроби
        # результат в Cres заносится справа налево
        Cres[i] = MUL_QQ_Q(C1[i][0], C1[i][1], q[0], q[1])
        Cres.insert(0, Cres[i])
    return m1, Cres

# P-4 - Умножение многочлена на x^k
# m – степень многочлена, массив C коэффициентов, k - степень переменной, на которую умножается
def MUL_Pxk_P(m, C, k):
    C.extend([0] * k)
    return ADD_NN_N(m, k), C

# P - 5 - старший коэффициент многочлена
def LED_P_Q(m, C):
    # возврат первого коэффициента из массива коэффициентов - он и является старшим
    return C[0]

# P-6 - Степень многочлена
# массив C коэффициентов
def DEG_P_N(C):
    return len(C) - 1  # количество коэффициентов, за исключением свободного члена, по сути и является степенью полинома

# P-7 Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей 
# Чтобы найти НОД чисел, сначала нужно поэтапно находить НОД 2 чисел от первого 
# коэффициента к последнему
# Чтобы найти НОК чисел, делаем тоже самое
def FAC_P_Q(arr):
    # Смотрим степень многочлена
    m = DEG_P_N(arr)
    nok = []
    nod = []
    i = 0
    # Переделываем в положительное натуральное
    for i in range(0, m + 1):
        if POZ_Z_D(arr[i].A) == 1:
            arr[i].A = ABS_Z_N(arr[i].A)
        else:
            arr[i].A = TRANS_Z_N(arr[i].A)
    # Если степень = 0
    if m == 0:
        nod = arr[i].A
        nok = arr[i].B
    else:
        # Ищем НОК и НОД первых 2 чисел
        for i in range(0, m + 1):
            if i == 0:
                nod = GCF_NN_N(arr[i].A, arr[i + 1].A)
                nok = LCM_NN_N(arr[i].B, arr[i + 1].B)
            else:
                # Ищем НОК и НОД последующих
                if i < m:
                    nod = GCF_NN_N(nod, arr[i + 1].A)
                    nok = LCM_NN_N(nok, arr[i + 1].B)
    return TRANS_N_Z(nod), TRANS_N_Z(nok)
   
# P-8 - Умножение многочленов(пока с сылками такими)
# C1 - коэффициенты первого многочлена, m1 - старшая степень первого многочлена,
# C2 - коэффициенты второго многочлена, m2 - старшая степень второго многочлена
# надо использовать: MUL_PQ_P - умножение многочлена на рациональное число, MUL_Pxk_P - умножение многочлена на x ^ k
def MUL_PP_P(m1, C1, m2, C2):
    if COM_NN_D(m1, m2) == 2:  # первый многочлен для удобства должен быть меньше степенью, чем второй
        m1, m2 = m2, m1
        C1, C2 = C2, C1

    m = MUL_Pxk_P(m2, C2, m1)[0]  # степень рез-рующего полинома - рез-т умножения 1-го полинома на x ^ 2-го полинома
    C = [0] * ADD_1N_N(m)  # количество коэффициентов будет соответствовать степени полученного многочлена + 1

    for i in range(len(С1)):  # чтобы второй полином перемножился на все коэффициенты первого полинома
        C0, m0 = MUL_PQ_P(C1[i], C2, m2)  # умножаем второй полином на i-тый коэффициент первого полинома
        k = 0
        for j in range(i, i + len(C0)):  # цикл, который обновляет коэффициенты для рез-рующего полинома
            C[j] = ADD_NN_N(C[j], C0[k])  # к уже полученному коэффициенту степени + новый коэффициент после умножения
            k = ADD_1N_N(k)  # счетчик индексов в массиве новых коэффов

    return m, C  # возвращается массив полученных коэффициентов и старшая степень полученного сногочлена

# P-9 - Частное от деления многочлена на многочлен при делении с остатком
# C1 - коэффициенты первого многочлена (делимое),
# C2 - коэффициенты второго многочлена (делитель)
# Надо использовать:
# DIV_QQ_Q - Деление дробей
# DEG_P_N - Степень многочлена
# MUL_Pxk_P - Умножение многочлена на x^k
# SUB_PP_P - Вычитание многочленов
# ADD_PP_P - Сложение многочленов
def DIV_PP_P(C1, C2):
    C3 = copy.deepcopy(C2) # *Копирование, чтобы потом вернуть C2 изначальные значение, так как функция MUL_Pxk_P
    # изменяет массив-параметр, а не возвращает новый массив
    deg1, deg2 = DEG_P_N(C1), DEG_P_N(C2) # Степени многочленов
    # Если степень делимого меньше степени делителя, то целое от такого деление = 0
    if deg1 < deg2:
        return [0]
    else:
        div = [0 for i in range(deg1 - deg2 + 1)] # Создаем массив коэффициентов целого необходимой длины
    # Пока степень делимого больше или равна степени делителя будет выполнятся:
    while deg1 >= deg2:
        # Домножаем делитель до степени делителя и сохраняем это промежуточное значение
        res = MUL_Pxk_P(deg2, C2, deg1-deg2)
        # Возвращаем C2 изначальные значения
        C2 = C3
        # Число, на которое необходимо домножить делитель, чтобы убрать старшую степень
        num = DIV_QQ_Q(LED_P_Q(deg1, C1), LED_P_Q(deg2, C2))
        # Домножаем промежуточное значение на частное от деления старших членов текущего делимого и делителя
        res = MUL_PQ_P(DEG_P_N(res), res, num)
        # Вычитаем из делимого результат, степень делимого уменьшится
        C1 = SUB_PP_P(C1, res)
        # Удаление незначащих нулей (необходимость зависит от реализации функции SUB_PP_P)
        while C1[0] == 0 and len(C1) != 1:
            C1.pop(0)
        # Добавляем коэффициент в результирующий массив
        div[deg1-deg2] = num
        deg1, deg2 = DEG_P_N(C1), DEG_P_N(C2)
    # Возвращает массив коэффициентов целого (первый коэффициент - старший)
    return div[::-1]

# P-10 - Остаток от деления многочлена на многочлен при делении с остатком
# C1 - коэффициенты первого многочлена (делимое),
# C2 - коэффициенты второго многочлена (делитель)
# Надо использовать:
# DIV_PP_P - Частное от деления многочлена на многочлен при делении с остатком
# MUL_PP_P - Умножение многочленов
# SUB_PP_P - Вычитание многочленов
def MOD_PP_P(C1, C2):
    div = DIV_PP_P(C1, C2)  # Находим частное от деления двух многочленов
    res = SUB_PP_P(C1, MUL_PP_P(DEG_P_N(div), div, DEG_P_N(C2), C2))  # Вычитаем из первого исходного многочлена
    # произведение частного на второй
    # В каком порядке будут возвращены коэффициенты зависит от функции SUB_PP_P
    return res

# P-11 - НОД многочленов
# C1 - коэффициенты первого многочлена, m1 - старшая степень первого многочлена,
# C2 - коэффициенты второго многочлена, m2 - старшая степень второго многочлена
# надо использовать DEG_P_N - степень многочлена,
# MOD_PP_P - Остаток от деления многочлена на многочлен при делении с остатком

def GCF_PP_P(m1, C1, m2, C2):
    deg1, deg2 = m1, m2  # чтобы не портить изначальные данные
    coef1, coef2 = C1, C2

    if COM_NN_D(m1, m2) == 1:  # первый многочлен-делимое должен быть больше степенью, чем второй многочлен-делитель
        deg1, deg2 = deg2, deg1
        coef1, coef2 = coef2, coef1

    while MOD_PP_P(deg1, coef1, deg2, coef2) != 0:  # пока остаток от деления многочленов не станет равен нулю
        coef = MOD_PP_P(deg1, coef1, deg2, coef2)  # коэффы остатка
        deg = DEG_P_N(coef)  # степень получившегося остатка (в MOD_PP_P не передает?)
        deg1, coef1, deg2, coef2 = deg2, coef2, deg, coef  # 1 полином - делимое, 2 полином - остаток, теперь делитель

    # довели до момента, когда делитель остался нужный для получения НОД (это deg2 и coef2)

    coef = coef1[:len(coef2)]  # часть от делимого, равная по длине делителю, т.к. работаем элементами столбика
    for i in range(len(coef1)):
        r = MOD_PP_P(DEG_P_N(coef), coef, deg2, coef2)  # остаток от той части делимого при делении на делитель
        if r != 0:  # если этот остаток не равен 0. Чтобы сохранился НОД, идущий перед нулевым остатком
            coef = r
            if len(coef2) + i < len(coef1):  # перестраховка, чтобы не было ошибок с индексацией
                coef.append(coef1[len(coef2) + i])  # добавляем следующий коэффициент из нашего изначального делимого
        else:
            break
    return coef

# P - 12 - производная многочлена
def DER_P_P(m, C):
    # приведение коэффициентов к виду (b,n,A[])
    for x in range(m):
        C_new = []
        if str(C[x])[0] == "-":
            b1 = 1
        else: b1 = 0
        d = 0
        for i in str(C[x]):
            if i == "." and b1 != 1:
                n = d
            elif i == "." and b1 == 1:
                n = d - 1
            elif i != "-":
                C_new.append(int(i))
            d += 1
        n1 = len(C_new)
        M = []
        X = []
        for i in str(m):
            M.append(int(i))
        for i in str(x):
            X.append(int(i))
        A = SUB_NN_N(M, X)
        b2 = 0
        n2 = len(A)
        b3,n3,C[x] = MUL_ZZ_Z(b1, n1, C_new, b2, n2, A)# умножение коэффициентов на соответствующую им степень
        if n and n > 0:
            C[x] = C[x][:n+(n3-n1)] + ["."] + C[x][n+(n3-n1):]
        if b1 == 1:
            C[x] = ["-"] + C[x]
        if C[x][len(C[x])-1] == 0 and C[x][len(C[x])-2] == ".":
            C[x].pop(len(C[x])-2)
            C[x].pop(len(C[x])-1)
        str1 = ""
        for i in range(len(C[x])):
            str1 += str(C[x][i])
        for i in C[x]:
            if i == ".":
                n = -2
        if n == -2:
            C[x] = float(str1)
        else:
            C[x] = int(str1)
        n = - 1
    m = m - 1 # понижение степени многочлена
    C.pop(len(C) - 1) # выброс последнего коэффициента - свободного члена
    return(m, C)


# P-13 - Преобразование многочлена — кратные корни в простые
# C1 - Многочлен, которые необходимо сократить
# Надо использовать:
# DIV_PP_P - Частное от деления многочлена на многочлен при делении с остатком
# DER_P_P - Производная многочлена
# GCF_PP_P - НОД многочленов
def NMR_P_P(C1):
    # Простые корни многочлена не являются корнями его производной
    # А кратный корень многочлена является корнем его производной на единицу меньшей кратности
    # Значит НОД многочлена и его производной равен произведению кратных корней многочлена на единицу меньшей кратности
    # Находим производную многочлена
    deriv = DER_P_P(C1)
    # Находим НОД многочлена и производной
    GCD = GCF_PP_P(C1, deriv)
    # Делим многочлен на НОД
    res = DIV_PP_P(C1, GCD)
    # Возвращает массив коэффициентов (первый коэффициент - старший)
    return res
