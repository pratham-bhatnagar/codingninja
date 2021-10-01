import random
import time
#from tkinter import *
#display = Tk()
#display.title("BHANU")
#Label (display, text="STONE PAPER SISSOR", bg="black", fg="green" , font="none 15 bold") .grid(row=1, column=0, sticky=W)

counter_user = 0
counter_pc = 0

def game(val,user,comp,counter_user,counter_pc):#algorithm for deciding a win or a loose
    
    if user==n:  #algorithm for deciding a win or a loose
        return 'DRAW!\n YOU:',val,'COMP:',comp
    else:
        if user==1:
            if comp==2:
                counter_pc+=1
                return ('YOU LOSE \n YOU:',val,'and COMP:',comp)
            else:
                counter_user+=1
                return ('YOU W0N \n YOU:',val, 'and COMP:',comp)
        elif user==2:
            if comp==1:
                counter_user+=1
                return ('YOU WON \n YOU:',val,' and COMP:',comp)
            else:
                counter_pc+=1
                return ('YOU LOSE \n YOU:',val,' and COMP:',comp)
        elif user==3:
            if comp==1:
                counter_pc+=1
                return ('YOU LOSE  \n YOU:',val,' and COMP:',comp)
            else:
                counter_user+=1
                return ('YOU WON  \n YOU:',val,' and COMP:',comp)
        elif user==4:
            quit()
        else:
            return val


while True:   #main loop for the game

    for i in "ROCK PAPER SCISSORS \n":
        print(i, end="")
        time.sleep(0.1) #making it look like typing

    n=random.randint(1,3) #randomlly choosing rock, paper or sissor
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
    user=int(input("Enter your Value: "))  #asking user for his choice
    if user==1:
        val="rock"
    elif user==2:
        val="paper"
    elif user==3:
        val="scissors"
    else:
        val="INVALID OPTION"
    
    print(game(val,user,comp))
    print("#######################################################")
    print("SCORE:  YOU:",counter_user,"\t COMPUTER:",counter_pc)
    print("#######################################################")
    print("\n \n") 
    time.sleep(0.5)





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
    
    
