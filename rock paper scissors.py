import random
def get_choices():
    p_choice= input("enter a choice(ROCK , PAPER , SCISSORS)  ")
    options =["rock" , "paper" , "scissors" ]
    c_choice = random.choice(options)
    choices = { "p": p_choice, "c":c_choice} 
    return (choices)

def check_win(p,c):
    print (f"your choice  {p} , computer choice {c} ")
    if p==c :
        return ("it's a tie ")
    elif p == "rock":
        if c == "scissors" :
            return(f" {p} smash {c} , you win ")
        else :
            return (f" {c} covers {p}, you lose")
    elif p== "paper":
        if c=="rock":
            return (f"{p} covers {c} , you win")
        else :
            return (f"{c} cuts {p} , you lose ")
    else:
        if c== "paper" :
            return(f"{p} cuts {c},  you win")
        else:
            return (f"{c} smash {p}, you lose ")


choices= get_choices()
result= check_win(choices["p"],choices["c"])
print(result)