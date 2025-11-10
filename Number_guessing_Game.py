import random
import time

start = int(input("Enter the first number : "))
end = int(input("Enter the second number : "))
main_number = random.randint(start, end)

user_guess = int(input("Enter the your guess number : "))

guess_count = 1 
start_time = time.time()

while main_number != your_guess :
    guess_count += 1
    try :
        if your_guess > main_number : 
            print("Your guess is too high ")
            your_guess = int(input("Enter the your guess number, again : "))

        elif your_guess < main_number :
            print("Your guess is too low ")
            your_guess = int(input("Enter the your guess number, again : "))

    except ValueError :
        print("Pleas enter number only ")    

end_time = time.time()
time_guess = end_time - start_time

print(f"Time guess : {time_guess:.2f} seconds")
print("Every guess is a step closer to success, finish game ")
print(f"Guess count :  {guess_count}")