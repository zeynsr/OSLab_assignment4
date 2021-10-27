game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]

def show_game_board():
    for i in range(3):
        print(*game[i])

def check_game():
    s=True
    for i in range(3):
        if game[i][0]==game[i][1]==game[i][2]=='❌' and game[i][0]!='-':
            print('player1 wins')
            s=False
            exit()
    if game[1][1]=='❌':
        if game[0][0]==game[2][2]=='❌':
            print('player1 wins')
            s = False
            exit()
        elif game[0][2]==game[2][0]=='❌':
            print('player1 wins')
            s = False
            exit()

    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == '⭕' and game[i][0] != '-':
            print('player2 wins')
            s = False
            exit()
    if game[1][1] == '⭕':
        if game[0][0] == game[2][2] == '⭕':
            print('player2 wins')
            s = False
            exit()
        elif game[0][2] == game[2][0] == '⭕':
            print('player2 wins')
            s = False
            exit()

    for i in game[2][2]:
        if '-' not in i:
            if  s == True:
                print('The game was a draw')
                exit()

print('''(1)  2 players
(2)  1player and computer''')
choose=int(input('Choose an option :'))

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
                    game[row][col] = '⚪'
                    break
                else:
                    print("this cell is not empty")

            else:
                print("invalid inputs,row and col must be between 0 and 2")

        show_game_board()
        check_game()

elif choose==2 :
    check_game()