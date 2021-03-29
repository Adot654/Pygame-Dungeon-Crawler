import random
                                                                                                                                                                                                                                                                       
def multiplication():
    for i in range(0,10):
        # randomise numbers for multiplcation
        num_1 = random.randint(2,10)
        num_2 = random.randint(2,10)
        answer = num_1 * num_2

        guess = 0
        print("What is", num_1, "x", num_2, "?")

        while guess != answer:
            
            guess = input("Answer: \n")
            while not guess.isnumeric():
                print("ENTER A NUMBER!")
                guess = input("Try Again: \n")
                if guess == answer:
                    print("Correct!")

def division():
    for i in range(0,10):
        # randomise numbers for division
        num_1 = random.randint(10,100)
        num_2 = random.randint(2,10)
        answer = round(num_1 / num_2)

        guess = 0
        print("What is", num_1, "÷", num_2, "?")

        guess = input("Answer: \n")
        while not guess.isnumeric():
            print("ENTER A NUMBER!")
            guess = input("Try Again: \n")

def addition():
    for i in range(0,10):
        # randomise numbers for addition
        num_1 = random.randint(1,20)
        num_2 = random.randint(1,20)
        answer = num_1 + num_2

        guess = 0
        print("What is", num_1, "+", num_2, "?")

        guess = input("Answer: \n")
        while not guess.isnumeric():
            print("ENTER A NUMBER!")
            guess = input("Try Again: \n")
        
def subtraction():
    for i in range(0,10):
        # randomise numbers for subtraction
        num_1 = random.randint(1,100)
        num_2 = random.randint(1,100)
        answer = num_1 - num_2

        guess = 0
        print("What is", num_1, "-", num_2, "?")

        guess = input("Answer: \n")
        while not guess.isnumeric():
            print("ENTER A NUMBER!")
            guess = input("Try Again: \n")

def algebra():
    for i in range(0,10):
        #randomise numbers
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        num_3 = random.randint(1,10)
        num_4 = random.randint(1,10)
        answer = num_1 * num_2 - num_3 + num_4
        
        guess = 0
        print("What is", num_1, "x", num_2, "-", num_3, "+", num_4, "?")

        guess = input("Answer: \n")
        while not guess.isnumeric():
            print("ENTER A NUMBER!")
            guess = input("Try Again: \n")
            

# main loop
multiplication()

print('congratulations you completed the game')

