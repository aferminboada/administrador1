board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

def show_board (new_board):
    for b in new_board:
        for c in b:
            if c == 0:
                print("_  ", end="")
            else:
                print(c, " ", end="")
        print()

def read_position ():
    x = input("Introduce un movimiento para la posicion x: ")
    y = input("Introduce un movimiento para la posicion y: ")
    x_int = int(x)
    y_int = int(y)
    return x_int, y_int
#read_position()

def play(is_player1):
    if is_player1:
        print("Jugador 1 realiza una jugada")
    else:
        print("Jugador 2 realiza una jugada")
    return read_position()

#play(True)

def vieja():
    player_playing = True
    do_we_play = True
    someone_won = 0
    while do_we_play and someone_won == 0:
        x, y = play(player_playing)
        if player_playing == True:
            board[x][y] = "X"
            player_playing = False
        else:
            board[x][y] = "O"
            player_playing = True


        show_board(board)
        do_we_play = there_is_play(board)
        someone_won = player_won(board)
    print("felicidades, player gano", who_won())

def there_is_play (new_board):
    for i in new_board:
        for d in i:
            if d == 0:
                return True
    return False

def player_won(new_board):

    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != 0:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board [1][0] != 0:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != 0:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != 0:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != 0:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != 0:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    else:
        return 0

def who_won():
    which_player_won = player_won(board)
    if which_player_won == "X":
        return "Ha ganado el jugador 1"
    elif which_player_won == "O":
        return "Ha ganado el jugador 2"
    else:
        return "Ha ganado la vieja"

vieja()




