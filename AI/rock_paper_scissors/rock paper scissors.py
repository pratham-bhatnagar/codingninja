import random
#from tkinter import *
#display = Tk()
#display.title("BHANU")
#Label (display, text="STONE PAPER SISSOR", bg="black", fg="green" , font="none 15 bold") .grid(row=1, column=0, sticky=W)

def game(val,user,comp): #algorithm for deciding a win or a loose

    if user==n:  #algorithm for deciding a win or a loose
        return 'DRAW!\n YOU:',val,'COMP:',comp
    else:
        if user==1:
            if comp==2:
                return ('YOU LOSE \n YOU:',val, 'and COMP:',comp)
            else:
                return ('YOU W0N \n YOU:',val, 'and COMP:',comp)
        elif user==2:
            if comp==1:
                return 'YOU WON \n YOU:',val,' and COMP:',comp
            else:
                return 'YOU LOSE \n YOU:',val,' and COMP:',comp
        elif user==3:
            if comp==1:
                return 'YOU LOSE  \n YOU:',val,' and COMP:',comp
            else:
                return 'YOU WON  \n YOU:',val,' and COMP:',comp
        elif user==4:
            quit()
        else:
            return val


while True:   #main loop for the game

    print("ROCK\t PAPAR\t SISSOR") 
    n=random.randint(1,3) #randomlly choosing rock, paper or sissor
    if n==1:
        comp="rock"
    elif n==2:
        comp="paper"
    else:
        comp="sissor"

    print("1~rock")
    print("2~paper")
    print("3~sissor")
    print("4~quit")
    user=int(input("Enter your Value: "))  #asking user for his choice
    if user==1:
        val="rock"
    elif user==2:
        val="paper"
    elif user==3:
        val="sissor"
    else:
        val="INVALID OPTION"
    
    print(game(val,user,comp))
    
    print("#######################################################")
    print("\n \n") 





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
    
    
