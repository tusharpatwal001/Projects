import random

OPERATORS = ["+", "-", "*", "/"]
MIN_OPERAND = 2
MAX_OPERAND = 12


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


while True:
    user_play = input("Do you want to play (y)? ")
    if user_play != "y":
        break

    expr, answer = generate_problem()
    print(f"Here is a question for you\n{expr}")
    while True:
        user_answer = eval(input("Enter your answer: "))
        if answer == user_answer:
            print(f"Your answer was correct {expr} = {user_answer}")
            break
        else:
            print("Try Again")
