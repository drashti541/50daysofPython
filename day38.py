#Task 1: Guess a Number
import random
print("\n*******************Task 1: Guess a Number*******************")
def guess_a_number():
    rnum = random.randint(0, 10)
    guess = 1
    
    while guess < 4:
        num = int(input("Guess a number:"))
        
        if guess == 3:
            print("You lose and you run out of guesses")
            break
        elif num > rnum:
            print("Guess is high")
        elif num < rnum:
            print("Guess is low")
        else:
            return "Winner"
        
        guess += 1
    return ""
               
result_guess = guess_a_number()
print(result_guess)


#Task 2:  Find Missing Numbers
print("\n*******************Task 2:  Find Missing Numbers*******************")
def missing_numbers(l1):
    l2 = [i for i in range(l1[0], l1[-1]+1) if i not in l1 ]
    return l2
  
  
l1 =  [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]         
result_index = missing_numbers(l1)
print(result_index)