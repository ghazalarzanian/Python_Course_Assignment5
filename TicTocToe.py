import random
from termcolor import colored
import time
##########################################
def Show_Game_Board():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end=' ')
        print() 
############################################
def Winnner_Checking():
    for i in range(3):
        if game[i][0]==colored('X','red') and game[i][1]==colored('X','red') and game[i][2]==colored('X','red'):
            print("player 1 is winner")
            return True
        elif game[i][0]==colored('O','blue') and game[i][1]==colored('O','blue') and game[i][2]==colored('O','blue'):
            print("Player 2 is winner")
            return True
    for j in range(3):
        if game[0][j]==colored('X','red') and game[1][j]==colored('X','red') and game[2][j]==colored('X','red'):
            print("player 1 is winner")
            return True
        elif game[0][j]==colored('O','blue') and game[1][j]==colored('O','blue') and game[2][j]==colored('O','blue'):
            print("Player 2 is winner")
            return True
    win =int(0)
    win1 =int(0)    
    for i in range(3):
        if game [i][i]==colored('X','red'):
            win+=1
        if game[i][i]==colored('O','blue'):
            win1+=1
    if win ==3 :
        print ("Player 1 is winner")  
        return True
    elif win1==3:
        print("Player 2 is winner ")
        return True
    win =0
    win1=0
    for i in range(2,-1,-1):
        if game [i][i]==colored('X','red'):
            win+=1
        if game[i][i]==colored('O','blue'):
            win1+=1
    if win ==3 :
        print ("Player 1 is winner")
        return True  
    elif win1==3 :
        print("Player 2 is winner")
        return True
###########################################
def Menu():
    print("For playing with Computer Press 1")
    print("For playing with Partner Press 2")
############################################
def With_Partner():
    Cel=int(0)
    while True:
        begin = time.time()
        Done = 1
        while Done ==1 and Cel !=9 :
            Show_Game_Board()
            print("Player 1:")
            row = int(input("Enter row[0:2]:"))
            col = int(input("Enter col[0:2]:"))
            if 0<= row <=2 and 0<= col <=2:
                if game[row][col] == '_':
                    game[row][col] = colored('X','red')
                    Cel +=1
                    Done =0
                else:
                    print('Enter Another one:')
            else :
                print("Row and col out of range,Enter again:")
        if Winnner_Checking() == True:
            Show_Game_Board()
            time.sleep(1)
            end = time.time()
            print(f"Total runtime of the program is {end - begin}")
            break
        Done = 1
        while Done ==1 and Cel !=9:
            Show_Game_Board()
            print("Player 2:")
            row = int(input("Enter row[0:2]:"))
            col = int(input("Enter col[0:2]:"))
            if 0<= row <=2 and 0<= col <=2:
                if game[row][col] == '_':
                    game[row][col] = colored('O','blue')
                    Cel +=1
                    Done =0
                else:
                    print('Enter Another one')
            else :
                print("Row and col out of range,Enter again:")
        if Winnner_Checking() == True:
            Show_Game_Board()
            time.sleep(1)
            end = time.time()
            print(f"Total runtime of the program is {end - begin}")
            break
        if Cel==9:
            Show_Game_Board()
            print("Draw")
            break
###############################################
def With_Computer():#O Human, X Computer 
    Cel=int(0)
    while True:
        begin = time.time()
        Done = 1
        if Done ==1 and Cel !=9 :
            Show_Game_Board()
            print("Player 1:")
            while Done ==1:
                row = random.randint(0,2)
                col = random.randint(0,2)
                if game[row][col] == '_':
                    game[row][col] = colored('X','red')
                    Cel +=1
                    Done =0
        if Winnner_Checking() == True:
            Show_Game_Board()
            time.sleep(1)
            end = time.time()
            print(f"Total runtime of the program is {end - begin}")
            break
##########################Human
        Done = 1
        while Done ==1 and Cel !=9:
            Show_Game_Board()
            print("Player 2:")
            row = int(input("Enter row[0:2]:"))
            col = int(input("Enter col[0:2]:"))
            if 0<= row <=2 and 0<= col <=2:
                if game[row][col] == '_':
                    game[row][col] = colored('O','blue')
                    Cel +=1
                    Done =0
                else:
                    print('Enter Another one')
            else :
                print("Row and col out of range,Enter again:")
        if Winnner_Checking() == True:
            Show_Game_Board()
            time.sleep(1)
            end = time.time()
            print(f"Total runtime of the program is {end - begin}")
            break
        if Cel==9:
            Show_Game_Board()
            print("Draw")
            break
#################################################################Main
game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]

# Cel =int(0)
Menu()
Choice=int(input(":"))
if Choice == 2:
    With_Partner()
elif Choice==1:
    With_Computer()
else:
    print("Try Agin")
    exit()
