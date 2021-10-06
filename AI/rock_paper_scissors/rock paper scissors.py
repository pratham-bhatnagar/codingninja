import random
import time

class bcolors:                          #added this class to color some of the next!
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

total_games_played = 0
winner = 0                                    # variables for score counter feature
counter_user = 0
counter_pc = 0


def game(user,comp):                          # Basic algorithm for rock paper and scissors
    
    if user==comp:                                   
        print('\t\tDRAW!\n\t\tYOU:',user,'COMP:',comp)
        winner=2
        return winner
    else:
        if user=='rock':
            if comp=='paper':
                print ('\t\tYOU LOSE \nYOU:',user,'and COMP:',comp)
                winner=0
                return winner
                
            else:
                print ('\t\tYOU W0N \n\t\tYOU:',user, 'and COMP:',comp)
                winner=1
                return winner
                 

        elif user=='paper':
            if comp=='rock':
                print ('\t\tYOU WON \n\t\tYOU:',user,' and COMP:',comp)
                winner=1
                return winner
                 
            else:
                print ('\t\tYOU LOSE \n\t\tYOU:',user,' and COMP:',comp)
                winner=0
                return winner
                
               
        elif user=='scissors':
            if comp=='rock':
                print ('\t\tYOU LOSE  \n\t\tYOU:',user,' and COMP:',comp)
                winner=0
                return winner
                
                
            else:
                print ('\t\tYOU WON  \n\t\tYOU:',user,' and COMP:',comp)
                winner=1
                return winner
                
                
        elif user=="quit":
            print("HAVE A NICE A AHEAD.\n\n")
            quit()
            
        else:
            print(user)


    
while True:                                     # main loop for the game

    for i in f"{bcolors.WARNING}ROCK  PAPER  SCISSORS  \n{bcolors.ENDC}":
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
        elif val==4:
            user="quit"
        else:
            user="INVALID OPTION\n\n"
    except ValueError:                         # In case user enters any non interger value.                  
        print("\n\nPlease enter a valid option.\n\n")
        time.sleep(0.5)
        continue
    
    winner = game(user,comp)                   # game function reterns '0' for a lose and '1' for a win

    if winner==1:

        counter_user+=1                        # adds 1 in user total score
        total_games_played+=1                  # adds 1 in total games played
        print(f"{bcolors.OKCYAN}#######################################################{bcolors.ENDC}")
        print("SCORE:  YOU:",counter_user,"\t COMPUTER:",counter_pc)
        print("\t\tTotal Games played:",total_games_played,"\t\t")
        print(f"{bcolors.OKCYAN}#######################################################{bcolors.ENDC}")
        print("\n \n") 
        time.sleep(0.2)

    elif winner==0:

        total_games_played+=1
        counter_pc+=1                          # adds 1 in computer total score
        print(f"{bcolors.OKCYAN}#######################################################{bcolors.ENDC}")
        print("SCORE:  YOU:",counter_user,"\t COMPUTER:",counter_pc)
        print("\t\tTotal Games played:",total_games_played,"\t\t")
        print(f"{bcolors.OKCYAN}#######################################################{bcolors.ENDC}")
        print("\n \n") 
        time.sleep(0.2)

    elif winner==2:

        total_games_played+=1
        print(f"{bcolors.OKCYAN}#######################################################{bcolors.ENDC}")
        print("\t\t ITS A DRAW!\t\t")
        print("SCORE:  YOU:",counter_user,"\t COMPUTER:",counter_pc)
        print("\t\tTotal Games played:",total_games_played,"\t\t")
        print(f"{bcolors.OKCYAN}#######################################################{bcolors.ENDC}")
        print("\n \n") 
        time.sleep(0.2)
    
    
    
    




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
    
    
