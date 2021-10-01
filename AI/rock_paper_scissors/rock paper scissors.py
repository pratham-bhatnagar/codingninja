import random
import time

total_games_played = 0
winner = 0                                    # variables for score counter feature
counter_user = 0
counter_pc = 0

def game(user,comp):                          # Basic algorithm for rock paper and scissors
    
    if user==comp:                                   
        print('\t\tDRAW!\n\t\tYOU:',val,'COMP:',comp)
        winner=2
        return winner
    else:
        if user=='rock':
            if comp=='paper':
                print ('\t\tYOU LOSE \nYOU:',val,'and COMP:',comp)
                winner=0
                return winner
                
            else:
                print ('\t\tYOU W0N \n\t\tYOU:',val, 'and COMP:',comp)
                winner=1
                return winner
                 

        elif user=='paper':
            if comp=='rock':
                print ('\t\tYOU WON \n\t\tYOU:',val,' and COMP:',comp)
                winner=1
                return winner
                 
            else:
                print ('\t\tYOU LOSE \n\t\tYOU:',val,' and COMP:',comp)
                winner=0
                return winner
                
               
        elif user=='scissors':
            if comp=='rock':
                print ('\t\tYOU LOSE  \n\t\tYOU:',val,' and COMP:',comp)
                winner=0
                return winner
                
                
            else:
                print ('\t\tYOU WON  \n\t\tYOU:',val,' and COMP:',comp)
                winner=1
                return winner
                
                
        elif user==4:
            print("HAVE A NICE A AHEAD.")
            quit()
        else:
            print(val)


    
while True:                                     # main loop for the game

    for i in "ROCK PAPER SCISSORS \n":
        print(i, end="")
        time.sleep(0.05)                        # making it look like typing

    n=random.randint(1,3)                       # randomlly choosing rock, paper or sissor
    if n==1:
        comp="rock"
    elif n==2:
        comp="paper"
    else:
        comp="scissors"

    print("1~rock")
    print("2~paper")
    print("3~scissors")
    print("4~quit")

    try:
        val=int(input("Enter your Value: "))    # asking user for his choice
        print("\n")
        if val==1:
            user="rock"
        elif val==2:
            user="paper"
        elif val==3:
            user="scissors"
        else:
            user="INVALID OPTION"
    except ValueError:                         # In case user enters any non interger value.                  
        print("\n\nPlease enter a valid option.\n\n")
        quit()
    
    winner = game(user,comp)                   # game function reterns '0' for a lose and '1' for a win

    if winner==1:

        counter_user+=1                        # adds 1 in user total score
        total_games_played+=1                  # adds 1 in total games played
        print("#######################################################")
        print("SCORE:  YOU:",counter_user,"\t COMPUTER:",counter_pc)
        print("\t\tTotal Games played:",total_games_played,"\t\t")
        print("#######################################################")
        print("\n \n") 
        time.sleep(0.5)

    elif winner==0:

        total_games_played+=1
        counter_pc+=1                          # adds 1 in computer total score
        print("#######################################################")
        print("SCORE:  YOU:",counter_user,"\t COMPUTER:",counter_pc)
        print("\t\tTotal Games played:",total_games_played,"\t\t")
        print("#######################################################")
        print("\n \n") 
        time.sleep(0.5)

    else:

        total_games_played+=1
        print("#######################################################")
        print("\t\t ITS A DRAW!\t\t")
        print("SCORE:  YOU:",counter_user,"\t COMPUTER:",counter_pc)
        print("\t\tTotal Games played:",total_games_played,"\t\t")
        print("#######################################################")
        print("\n \n") 
        time.sleep(0.5)
    
    
    
    




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
    
    
