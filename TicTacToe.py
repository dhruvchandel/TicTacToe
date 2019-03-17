#   X | X | X 
#  ---+---+---
#   X | X | X 
#  ---+---+---
#   X | X | X
 
# what above shown is sample tic tac toe board representation

p1=p2=p3=p4=p5=p6=p7=p8=p9=' '
flag = int(1)

def display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9) :
    print(" {} | {} | {} ".format(p1,p2,p3))
    print("---+---+---")
    print(" {} | {} | {} ".format(p4,p5,p6))
    print("---+---+---")
    print(" {} | {} | {} ".format(p7,p8,p9))
    
display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9) 
    
player1_sign = input("What sign Do you Choose Player 1 ? 'X' or 'O' =>"  )

if player1_sign == 'X' :
    player2_sign = 'O'
else :
    player2_sign = 'X'

def move_coordinator_player1(move):
    global flag 
    if(move==1) :
        global p1
        if(p1!=' ') : 
            print("Invalid Move !!!")
            flag = 1 
        else : 
            p1 = player1_sign
    if(move==2) :
        global p2 
        if(p2!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p2 = player1_sign
    if(move==3) :
        global p3 
        if(p3!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p3 = player1_sign
    if(move==4) :
        global p4 
        if(p4!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p4 = player1_sign
    if(move==5) :
        global p5
        if(p5!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p5 = player1_sign
    if(move==6) :
        global p6
        if(p6!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p6 = player1_sign
    if(move==7) :
        global p7 
        if(p7!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p7 = player1_sign
    if(move==8) :
        global p8 
        if(p8!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p8 = player1_sign
    if(move==9) :
        global p9 
        if(p9!=' ') : 
            print("Invalid Move !!!")
            flag = 1
        else : 
            p9 = player1_sign

def move_coordinator_player2(move):
    global flag
    if(move==1) :
        global p1
        if(p1!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p1 = player2_sign
    if(move==2) :
        global p2 
        if(p2!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p2 = player2_sign
    if(move==3) :
        global p3 
        if(p3!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p3 = player2_sign
    if(move==4) :
        global p4 
        if(p4!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p4 = player2_sign
    if(move==5) :
        global p5
        if(p5!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p5 = player2_sign
    if(move==6) :
        global p6
        if(p6!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p6 = player2_sign
    if(move==7) :
        global p7 
        if(p7!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p7 = player2_sign
    if(move==8) :
        global p8 
        if(p8!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p8 = player2_sign
    if(move==9) :
        global p9 
        if(p9!=' ') : 
            print("Invalid Move !!!")
            flag = 2
        else : 
            p9 = player2_sign


 
def move_enterer() :
    global flag
    if(flag==1) :
        move = int(input("Player 1 : Please Enter Your Move :"))
        flag = 2
        move_coordinator_player1(move)
    else :
        move = int(input("Player 2 : Please Enter Your Move :"))
        flag = 1
        move_coordinator_player2(move)

winner_name = ""

def win_detector(p1,p2,p3,p4,p5,p6,p7,p8,p9) :
    global winner_name
    if p1!=' ' and p1!=' ' and p2!=' ' and p3!=' ' and p4!=' ' and p5!=' ' and p6!=' ' and p7!=' ' and p8!=' ' and p9!=' ' :  
        winner_name = "None"
        return False
    if p1==p2 and p2==p3 and p1 not in ' ' and p2 not in ' ' and p3 not in ' ' :
        if(p1 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    elif p4==p5 and p5==p6 and p4 not in ' ' and p5 not in ' ' and p6 not in ' ' :
        if(p4 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    elif p7==p8 and p8==p9 and p7 not in ' ' and p8 not in ' ' and p9 not in ' ' :
        if(p7 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    elif p1==p4 and p4==p7 and p1 not in ' ' and p4 not in ' ' and p7 not in ' ' :
        if(p1 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    elif p2==p5 and p5==p8 and p2 not in ' ' and p5 not in ' ' and p8 not in ' ' :
        if(p2 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    elif p3==p6 and p6==p9 and p3 not in ' ' and p6 not in ' ' and p9 not in ' ' :
        if(p3 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    elif p3==p5 and p5==p7 and p3 not in ' ' and p5 not in ' ' and p7 not in ' ' :
        if(p3 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    elif p1==p5 and p5==p9 and p1 not in ' ' and p5 not in ' ' and p9 not in ' ' :
        if(p1 == player1_sign) :
            winner_name = 'Player 1'
        else :
            winner_name = 'Player 2'
        return False
    else :
        return True

while(win_detector(p1,p2,p3,p4,p5,p6,p7,p8,p9)) :
    move_enterer()
    display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9) 
    
    
if winner_name != 'None' :
    print("\n\n\n\t\tHurarh ! So , the Winner is " + winner_name + "\n\t\tWinner Winner Samosa Dinner")
else :
    print("\n\n\n\t\tEat half-half Samosa as its a TIE ;)")
