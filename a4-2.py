w=int(input())
h=int(input())

def func(w,h):
    for i in range(w):
        if i % 2 == 0:
            for j in range(h):
                if j % 2 == 0 or j == 0:
                    print('# ', end=' ')
                elif j % 2 == 1:
                    print('* ', end=' ')
            print()
        elif i % 2 == 1:
            for j in range(h):
                if j % 2 == 0 or j == 0:
                    print('* ', end=' ')
                elif j % 2 == 1:
                    print('# ', end=' ')
            print()

func(w,h)