from random import choice
from os import system
from time import sleep

def compare(a,b):
    if celebrities[a][1]>celebrities[b][1]:
        return a
    else:
        return b
celebrities={
    "Rihanna":["Singer",1500000],
    "Eminem":["Rapper",1750000],
    "Şehinşah":["Rapper",150000],
    "Celal Şengör":["Jeologist",100000],
    "İlber Ortaylı":["Professor",95000],
    "Shawn Mendes":["Musician",200000],
    "Emma Watson":["Actress",195000],
    "Gigi Hadid":["Model",250000],
    "LeBron James":["Basketball Player",1000000],
    "Drake":["Rapper",2000000]
    
}
gameOn=True
isSame=False
point=0
optionA=choice(list(celebrities.keys()))
while gameOn:
    print('''
    
  _  _      _      __ _   _                      
 | || |    (_)    / _` | | |_      ___      _ _  
 | __ |    | |    \__, | | ' \    / -_)    | '_| 
 |_||_|   _|_|_   |___/  |_||_|   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
   _                                             
  | |      ___   __ __ __  ___      _ _          
  | |__   / _ \  \ V  V / / -_)    | '_|         
  |____|  \___/   \_/\_/  \___|   _|_|_          
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|         
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'         
''')
    
    optionB=choice(list(celebrities.keys()))
    if optionA==optionB:
        isSame=True
        while isSame:
            optionB=choice(list(celebrities.keys()))
            if not optionA ==optionB:
                isSame=False
    print(f"Option A is:{optionA}, {celebrities[optionA][0]}")
    print('''
    
 __   __   ___   
 \ \ / /  / __|  
  \ V /   \__ \  
  _\_/_   |___/  
_| """"|_|"""""| 
"`-0-0-'"`-0-0-' 
''')
    print(f"Option B is:{optionB}, {celebrities[optionB][0]}")
    userGuess=input("Which one is higher a or b: ")
    
    if compare(optionA,optionB)==optionA:
        winner="a"
        
    else:
        winner="b"
        optionA=optionB
    print("You areeee....")
    sleep(1)
    system("cls")
    if userGuess==winner:
        point+=1
        print(f"Right! Current score: {point}")
        
    else:
        print('''
    
  _  _      _      __ _   _                      
 | || |    (_)    / _` | | |_      ___      _ _  
 | __ |    | |    \__, | | ' \    / -_)    | '_| 
 |_||_|   _|_|_   |___/  |_||_|   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
   _                                             
  | |      ___   __ __ __  ___      _ _          
  | |__   / _ \  \ V  V / / -_)    | '_|         
  |____|  \___/   \_/\_/  \___|   _|_|_          
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|         
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'         
''')
        gameOn=False
        print(f"Wrong! Final score: {point}")
