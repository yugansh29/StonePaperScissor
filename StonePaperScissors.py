import random
while True:
    choices={"Stone":"🪨","Paper":"📄","Scissor":"✂️"}
    computer=random.choice(list(choices))
    _= None
    while (_ not in choices):
        _ = input("Enter your choice Stone,Paper,Scissor ").capitalize()
    print ("You choose "+ _ )
    print("Computer Choose "+computer )   
    if (_== computer):
        print("It's a Tie !!!")
    elif(_=="Scissor" and computer=="Paper" ):
        print ("You Won!!!")
    elif(_=="Paper" and computer=="Scissor" ):
        print ("You lost!!!")
    elif(_=="Stone" and computer=="Scissor" ):
        print ("You Won!!!")
    elif(_=="Scissor" and computer=="Stone" ):
        print ("You Lost!!!")
    elif(_=="Stone" and computer=="Paper" ):
        print ("You Lost!!!")
    elif(_=="Paper" and computer=="Stone" ):
        print ("You Won!!!")
    
    playAgain=input("Would you like to try again(yes/no)").lower()
    if playAgain =="no":
        break
print ("bye")
