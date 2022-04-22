# Преобразование числа в массив чисел
def INT_TO_ARR(A):
    B = [0] * len(A)
    for i in range(len(A)):
        B[i] = int(A[i])
    return B

A = input("Enter the number: ")

print(INT_TO_ARR(A))


# Преобразование массива чисел в число
def ARR_TO_INT(A):
    A = map(str, A)
    B = "".join(A)
    B = int(B)

    return B

A = list(map(int, input("Введите массив чисел: ").split()))
print(ARR_TO_INT(A))
