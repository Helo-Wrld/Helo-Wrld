import sys

Board = {'tl': ' ', 'tm': ' ', 'tr': ' ',
         'ml': ' ', 'mm': ' ', 'mr': ' ',
         'bl': ' ', 'bm': ' ', 'br': ' '}


def pboard(board):
    print("t" + "   " + board['tl'] + "  |      " + board['tm'] + "    |    " + board['tr'])
    print("       |           |       ")
    print("____________________________")
    print("m" + "   " + board['ml'] + "  |      " + board['mm'] + "    |    " + board['mr'])
    print("       |           |       ")
    print("____________________________")
    print("b" + "   " + board['bl'] + "  |      " + board['bm'] + "    |  " + board['br'])
    print("       |           |       ")
    print("   l         m         r   ")


pboard(Board)

turn = 'X'
for i in range(9):
    print("Enter location in the format 'bm'(or 'exit' to finish)?")
    v = input()
    if v == 'exit':
        print(turn + " has lost, because they were the one to quit")
        sys.exit()
    else:
        if turn == 'X':
            Board[v] = 'X'
            turn = 'O'
        elif turn == 'O':
            Board[v] = 'O'
            turn = 'X'
    pboard(Board)

if Board['tm'] == Board['tr'] == Board['tl']:
    print(str(Board['tl']) + " has won this game")
if Board['mm'] == Board['mr'] == Board['ml']:
    print(str(Board['ml']) + " has won this game")
if Board['bm'] == Board['br'] == Board['bl']:
    print(str(Board['bl']) + " has won this game")
if Board['tr'] == Board['mr'] == Board['br']:
    print(str(Board['tr']) + " has won this game")
if Board['tm'] == Board['mm'] == Board['bm']:
    print(str(Board['mm']) + " has won this game")
if Board['tl'] == Board['ml'] == Board['bl']:
    print(str(Board['tl']) + " has won this game")
if Board['mm'] == Board['tr'] == Board['bl']:
    print(str(Board['tr']) + " has won this game")
if Board['mm'] == Board['tl'] == Board['br']:
    print(str(Board['tl']) + " has won this game")



