import random

dict = {
        'rock':1,
        'paper':2,
        'scissors':3
}


turn = 1 
while turn == 1:
     try:
       print('enter 1,2,and 3 for rock, paper, and scissors respectively.')
       computer = random.randint(1,3)
    
       key =  list(dict.keys())
       val = list(dict.values())
       position_c= val.index(computer)
       # print(key[position])
        
    #    print(dict.get(key[position_c]))
       

       you = int(input('enter the value: '))
       positon_k = val.index(you)

       if you == computer:
           print('tie')
           print('you chioce -->',key[positon_k])
           print('computer chioce -->',key[position_c])

       elif you ==1 and computer ==3:
           print('you win')
           print('computer chioce -->',key[position_c])
           print('you chioce -->',key[positon_k])

       elif you ==2 and computer ==1:
           print('you win')
           print('computer chioce -->',key[position_c])
           print('you chioce -->',key[positon_k])
           
           
       
       elif you ==3 and computer ==2:
           print('you win')
           print('computer chioce -->',key[position_c])
           print('you chioce -->',key[positon_k])

       else :
           print('you loss')
           print('computer chioce -->',key[position_c])
           print('you chioce -->',key[positon_k])
           
       turn = int(input('if you want to play again enter 1, otherwise enter 0 :'))

     except:
          print('an exception occurred')
    
