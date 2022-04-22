# Преобразование числа в массив чисел
def INT_TO_ARR(A):
    B = [0] * len(A)
    for i in range(len(A)):
        B[i] = int(A[i])
    return B

A = input("Enter the number: ")

print(INT_TO_ARR(A))
