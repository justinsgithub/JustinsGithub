import os




def guess_the_number():
    print("i love guessing numbers")

    print("choose a number for me to guess, and see how fast i guess it")
    print("tell me if its too high or too low")
    print("choose a starting number")
    start_num = int(input())
    print("choose an ending number")
    end_numb = int(input())
    
    guess = int((start_num + end_numb) / 2)
    print("is it " + format(guess) + "?")


guess_the_number()


