name = input("Type your name: ")

print(f"Welcome {name.capitalize()} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right)? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim accross (swim/walk)? ").lower()
    if answer == "swim":
        print("You swim accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You Lose.")
        
elif answer == "right":
    answer = input("You come to a brige, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a strange. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talked to the stranger they got impressed by you and gave Gold. You Win!")
        elif answer == "no":
            print("You don't talk and got killed by stranger.")
        else:
            print("Not a valid option. You Lose.")
            
    elif answer == "back":
        print("You go back and struck by lightning.")
    else:
        print("Not a valid option. You Lose.")
else:
    print("Not a valid option. You Lose.")