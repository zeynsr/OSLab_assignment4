import random
import time
from colorama import init
init()

start = time.time()

game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]

def show_game_board():
    for i in range(3):
        print(*game[i])

def check_game():

    for i in range(3):
        if game[i][0]==game[i][1]==game[i][2]=='❌' and game[i][0]!='-':
            print('player1 wins')
            print("Run Time: " + str(time.time() - start))
            exit()
        elif game[1][1]=='❌':
            if game[0][0]==game[2][2]=='❌':
                print('player1 wins')
                print("Run Time: " + str(time.time() - start))
                exit()
            elif game[0][2]==game[2][0]=='❌':
                print('player1 wins')
                print("Run Time: " + str(time.time() - start))
                exit()
        elif game[i][0] == game[i][1] == game[i][2] == '⭕' and game[i][0] != '-':
                print('player2 wins')
                print("Run Time: " + str(time.time() - start))
                exit()
        elif game[1][1] == '⭕':
            if game[0][0] == game[2][2] == '⭕':
                print('player2 wins')
                print("Run Time: " + str(time.time() - start))
                exit()
            elif game[0][2] == game[2][0] == '⭕':
                print('player2 wins')
                print("Run Time: " + str(time.time() - start))
                exit()
        elif cnt == 9:
            print('The game was a draw')
            print('Run Time: ' + str(time.time() - start))
            exit()

print('''(1)  2 players
(2)  1player and computer''')
choose=int(input('Choose an option :'))
cnt=0
if choose==1:
    show_game_board()

    while True:

        # player1
        while True:
            print("Player1")

            row = int(input('row:'))
            col = int(input('col: '))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '-':
                    game[row][col] = '❌'
                    cnt+=1
                    break
                else:
                    print("this cell is not empty")

            else:
                print("invalid inputs,row and col must be between 0 and 2")

        show_game_board()
        check_game()

        # player2
        while True:
            print("Player 2")
            row = int(input('row:'))
            col = int(input('col: '))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '-':
                    game[row][col] = '⭕'
                    cnt += 1
                    break
                else:
                    print("this cell is not empty")

            else:
                print("invalid inputs,row and col must be between 0 and 2")

        show_game_board()
        check_game()

elif choose==2 :
   while True :
       while True:
           print("Player ")
           row = int(input('row:'))
           col = int(input('col: '))

           if 0 <= row <= 2 and 0 <= col <= 2:
               if game[row][col] == '-':
                   game[row][col] = '❌'
                   cnt += 1
                   break
               else:
                   print("this cell is not empty")

           else:
               print("invalid inputs,row and col must be between 0 and 2")

       show_game_board()
       check_game()
       while True:
           print("computer ")
           row = random.randint(0, 2)
           col = random.randint(0, 2)
           print('row : ',row)
           print('col : ',col)
           if 0 <= row <= 2 and 0 <= col <= 2:
               if game[row][col] == '-':
                   game[row][col] = '⭕'
                   cnt += 1
                   break
               else:
                   print("this cell is not empty")

           else:
               print("invalid inputs,row and col must be between 0 and 2")

       show_game_board()
       check_game()
