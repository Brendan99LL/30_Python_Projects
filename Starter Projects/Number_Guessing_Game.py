# Import the dependency to use random numbers
from random import randint

# Define what the range for the numbers will be
lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}.')

# Make sure that the program will work only if the user inputs a number
# Print a statement that would prevent the user from inputing something besides a number
while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue
    
    # Print statements if the number inputed is lower, higher, and when it is the same as the random number
    if user_guess > random_number:
        print('The number is lower.')
    elif user_guess < random_number:
        print('The number is higher.')
    else:
        print('You guessed it!')
        # Finish the program
        break
    