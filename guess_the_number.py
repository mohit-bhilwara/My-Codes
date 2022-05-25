import random

num1 = random.randint(1,100)
# print(num1)

turn = 5
Guesses = 0

while turn > 0 :
    try: 
        print(f'you have {turn} turn')
        num2 = int(input('Guess the number: '))  
    
        if num1 == num2:
            print(f'you win in {Guesses+1} guesses')
            turn = 0   
    
        elif num1 < num2:
            if turn!=1:
               print('lower number please') 
               print('')
    
        elif num1 > num2:
            if turn!=1:
                print('higher number please')    
                print('')
    
    except:
         print('please enter integers only')
         if turn!=1:
          print('')
    turn= turn-1
    Guesses+=1
       
print('')
print('Game Over')