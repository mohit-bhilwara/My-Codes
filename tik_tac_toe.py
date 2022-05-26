
a = 'a'
b = 'b'
c = 'c'
d = 'd' 
e = 'e'
f,g,h,i = 'f','g','h','i'


def Board():
    print('',a,"|"'',b,'|''',c )
    print('---|---|---')
    print('',d,"|"'',e,'|''',f )
    print('---|---|---')
    print('',g,"|"'',h,'|''',i )


total_turn = 10
def checkwin():
    wins = [[a,b,c],[d,e,f],[g,h,i],[a,d,g,],[b,e,h],[c,f,i],[a,e,i],[g,e,c]]

    for win in wins :
        if win[0]=="X" and win[1]=="X" and win[2] =="X":
             Board()
             print('X won the match')
             return 1
          
        elif win[0]=="O" and win[1]=="O" and win[2] =="O":
             Board()
             print('O won the match')
             return 0
    
    
print('welcom to tik tac teo game')
turn = 1
while total_turn > 0:
    Board()
    if total_turn >1:
        if turn == 1 :
            x= input("X's turn enter any alphabetical position: ")
            
            if x == "a":
                 a= "X"
            elif x == "b":
                 b= "X"
            elif x == "c":
                 c= "X"
            elif x == "d":
                 d= "X"
            elif x == "e":
                 e= "X"
            elif x == "f":
                 f= "X"
            elif x == "g":
                 g= "X"
            elif x == "h":
                 h= "X"
            elif x == "i":
                 i= "X"

        elif turn == 0:
            o = input("O's turn enter any alphabetical position: ") 
     
            if o == "a":
                 a= "O"
            elif o == "b":
                 b= "O"
            elif o == "c":
                 c= "O"
            elif o == "d":
                 d= "O"
            elif o == "e":
                 e= "O"
            elif o == "f":
                 f= "O"
            elif o == "g":
                 g= "O"
            elif o == "h":
                 h= "O"
            elif o == "i":
                 i= "O"


    if checkwin() == 1 or checkwin() == 0:
     
         break
#     if checkwin !=1 and checkwin()!=0:
#           print('match tie')

         

    total_turn = total_turn-1
    turn = 1 - turn
        
print('Gameover')  
