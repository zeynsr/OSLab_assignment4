n = int(input())

def fib(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
       return fib(num-1) + fib(num-2)

r = fib(n)
print(r)
