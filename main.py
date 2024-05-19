""" 
Rock paper scissor game in python 

"""
import random

computer_tries = ["Scissor","rock","Paper"]
exit_message = "Enter 4 to exit"
score_message= "& 5 to for score"
screen_width = 80
text_width = len("Scissor")
box_width = text_width + 10
left_margin = (screen_width - box_width) // 2
print("Your Try")

score = [0,0]
def game(user_input):
    if int(user_input) < 4:
        computer_tries = ["Scissor","rock","Paper"]
        user_choice = computer_tries[user_input - 1]
        random_integer = random.randint(0,2)
        computer_choice = computer_tries[random_integer]
        print("Your choice is : ",user_choice)
        if (user_input-1) == random_integer:
            print("Uh oh Both our choices are same")
        if user_choice == computer_tries[0]:
            if random_integer == 2:
                print("my choice was :",computer_choice)
                print("You win")
                score[0] = score[0] +1
            if random_integer == 1:
                print("my choice was :",computer_choice)
                print("Whoo whoo I win")  
                score[1] = score[1] +1 
        if user_choice == computer_tries[1]:
            if random_integer == 0:
                print("my choice was :",computer_choice)
                print("You win")
                score[0] = score[0] +1
            if random_integer == 2:
                print("my choice was :",computer_choice)
                print("Whoo whoo I win") 
                score[1] = score[1] +1 
        if user_choice == computer_tries[2]:
            if random_integer == 1:
                print("my choice was :",computer_choice)
                print("You win")
                score[0] = score[0] +1
            if random_integer == 0:
                print("my choice was :",computer_choice)
                print("Whoo whoo I win") 
                score[1] = score[1] +1 
    if user_input == 4:
        exit()
    
    if user_input == 5:
        print("computer score :",score[1])
        print("Your score :",score[0])
    if user_input >5 or user_input == 0 :
        print("Enter numbers form the given choices only")
def input_function():
    print()
    print(' ' * left_margin + '+' + '-' * (box_width) + '+')
    print(' ' * left_margin + '| ' + ' ' * (box_width-2) + ' |')
    for i in range(0,3):
        string_to_print = computer_tries[i] + " = " + str(i+1)
        print(' ' * left_margin + '| ' + string_to_print + ' '*(15-len(string_to_print))  + ' |')
    print(' ' * left_margin + '| ' + exit_message + ' '*(9-len(string_to_print))  + ' |')
    print(' ' * left_margin + '| ' + score_message  + '|')
    print(' ' * left_margin + '| ' + ' ' * (box_width-2) + ' |')
    print(' ' * left_margin + '+' + '-' * (box_width) + '+')
    print()
    print()
    user_input = int(input("Enter the number infront of the choices to choose : "))
    return user_input


r = input_function()
while r != 4 :
    game(r)
    input("Press Enter")
    r = input_function()
    