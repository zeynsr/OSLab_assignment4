a = int(input())
b = int(input())

def f1(num1, num2):
    for i in range(num1):
        for j in range(num2):
            print((i + 1) * (j + 1), end='  ')
        print()

f1(a, b)
