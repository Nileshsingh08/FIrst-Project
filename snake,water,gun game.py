import random
l1=['w' ,'s' ,'g']
chance=5
computer_point=0
human_point=0
no_of_chance=0
print("select any of these?\ng for gun\nw for water\ns for snake")
while no_of_chance < chance:
    ns=input('snake,water,gun:')
    ps=random.choice(l1)
    if ns==ps:
        print("tie both got 0 point")
    #when human choose s
    elif ns == "s" and ps == "g" :
        print("computer won\n")
        computer_point= computer_point+1
        print(f"your guess {ns} and computer guess is {ps} \n")
        print(f"computer_point{computer_point} and your point{human_point}\n")
    elif ns == "s" and ps == "w":
        print("you won\n")
        human_point=human_point + 1
        print(f"your guess {ns} and computer guess is {ps} \n")
        print(f"computer_point{computer_point} and your point{human_point}\n")
    #when human choose w
    elif ns=="w" and ps == "g":
        print("you win\n")
        human_point = human_point + 1
        print(f"your guess {ns} and computer guess is {ps} \n")
        print(f"computer_point{computer_point} and your point{human_point}\n")
    elif ns =="w" and ps =="s":
        print("computer won\n")
        computer_point = computer_point + 1
        print(f"your guess {ns} and computer guess is {ps} \n")
        print(f"computer_point{computer_point} and your point{human_point}\n")
    # when user choose g
    elif ns == "g" and ps == "w":
        print("computer won\n")
        computer_point = computer_point + 1
        print(f"your guess {ns} and computer guess is {ps} \n")
        print(f"computer_point{computer_point} and your point{human_point}\n")
    elif ns == "g" and ps == "s":
        print("you win\n")
        human_point = human_point + 1
        print(f"your guess {ns} and computer guess is {ps} \n")
        print(f"computer_point{computer_point} and your point{human_point}\n")
    else:
        print("you have input wrong \n")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
print("game over")
if computer_point == human_point:
    print("tie")
elif computer_point>human_point:
    print("computer won")
elif computer_point<human_point:
    print("user won")
print(f"your point is {human_point} and computer point is {computer_point}")


