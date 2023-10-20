import random
#
choices={"Stone":"🪨","Paper":"📄","Scissor":"✂️"}
computer=random.choice(list(choices))
_ = input("Enter your choice Stone,Paper,Scissor ")
print ("You choose "+ _ )
print("Computer Choose "+computer)

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

    
