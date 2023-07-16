width = int(input())
height = int(input())

def func(width, height):
    for i in range(width):
        if i % 2 == 0:
            for j in range(height):
                if j % 2 == 0 or j == 0:
                    print('# ', end=' ')
                elif j % 2 == 1:
                    print('* ', end=' ')
            print()
        elif i % 2 == 1:
            for j in range(height):
                if j % 2 == 0 or j == 0:
                    print('* ', end=' ')
                elif j % 2 == 1:
                    print('# ', end=' ')
            print()

func(width,h)
