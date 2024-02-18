"""Rock Paper Scissor Game"""

from random import randint


def welcome():
    print("-------------------Welcome------------------")
    print("Let's!! fresh your mood")
    print("It's ROCK PAPER SCISSOR GAME")
    print("Rock beats scissors, scissors beat paper, and paper beats rock.")

def game():
    comp_option={1:'rock',2:'paper',3:'scissor'}
    comp_choice=comp_option[randint(1,3)]

    print("Select your move ('Rock','Paper','Scissor')")
    valid_option=('rock','paper','scissor')
    while True:
        try:
            user_choice=(input("Enter your choice:"))
            if not user_choice.lower() in valid_option:
                raise ValueError("Provide valid choice!!")
            print(f'computer:{comp_choice}     VS     user:{user_choice}')
            if user_choice == comp_choice:
                print("It's a Draw")
                score = 0
                return score
            win_cond=[
                 user_choice == 'rock' and comp_choice == 'scissor',
                 user_choice == 'scissor' and comp_choice == 'paper',
                 user_choice == 'paper' and comp_choice == 'rock'
            ]
            if True in win_cond:
                print("Congrats!! You won")
                score =1
                return score
            
            if False in win_cond:
                print("Oops!! You loose")
                score =-1
                return score

        except ValueError as error:
            print(f"Error : {error}")

def rock_paper_scissor():
    total_score=0
    while True :
        print("1.Play Game\n2.Exit")
        try:
            userinput=int(input("Enter your choice:"))

            if userinput == 1:
                total_score+=game()
                print(f'Score = {total_score}')
                print()
            elif userinput== 2:
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Please choose 1 or 2")

welcome()
rock_paper_scissor()

        


