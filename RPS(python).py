print('Welcome to Rock Paper Scissors \nChoose between Rock, Paper and Scissors\nAccordingly enter\n1 for Rock\n2 for Paper\n3 for scissors')
print('Enter the no. of rounds you desire to play')

round=int(input())

import random

pcc=0
uc=0

#pcc=pc_count
#uc=user_count

for i in range(0,round):
    
    print('\nRound',i+1)
    print('Enter 1 or 2 or 3')
    
    userv= int(input())
    
    pc= random.randrange(1,4)
    
    if(pc==1):
        y='rock'
    elif(pc==2):
        y='paper'
    elif(pc==3):
        y='scissor'
        
    if(userv==1):
        x='rock'
    elif(userv==2):
        x='paper'
    elif(userv==3):
        x='scissor'
    
    print('Your pick',x)
    print('PC pick',y)
    
# when the user opts for rock    
    if(userv==1):
        if(pc==3):
            print('you win\n')
            uc=uc+1
        
        elif(pc==2):
            print('you lose\n')
            pcc=pcc+1
        
        elif(pc==1):
            print("we are of one mind:-):It's a Tie\n")
    
# when the user opts for paper  
    if(userv==2):
        if(pc==1):
            print('you win\n')
            uc=uc+1
        
        elif(pc==3):
            print('you lose\n')
            pcc=pcc+1
        
        elif(pc==2):
            print("we are of one mind:-):It's a Tie\n")

# when the user opts for scissors  
    if(userv==3):
        if(pc==2):
            print('you win\n')
            uc=uc+1
        
        elif(pc==1):
            print('you lose\n')
            pcc=pcc+1
        
        elif(pc==3):
            print("we are of one mind:-):It's a Tie\n")




if(pcc>uc):
  print('\nYou LOSE')
elif(uc>pcc):
  print('Hurrah!!!! You WIN')
elif(uc==pcc):
  print('A close match but a TIE')
  
for i in range(1):
    g=input()