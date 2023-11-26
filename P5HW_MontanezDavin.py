#This program runs simple math quizzes
#20 Nov 2023
#CTI-110 P5HW-Math Quiz
#Davin Montanez
#

import random

print('Welcome to my Math Quiz\n')
print('Main Menu')
print('-' * 20)

def display_menu():
    print('1. Add two numbers')
    print('2. Subtract two numbers')
    print('3. Exit\n')

def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1, '\n+', num2)
    counter = 0
    while True:
        answer = int(input('What do they add to? \n'))
        counter += 1
        if answer == num1 + num2:
            print(f'Congratulations! That\'s correct. You guessed it in {counter} attempts.\n')
            break
        elif answer > num1 + num2:
            print("Sorry, that's incorrect. Your guess is too high. Try again.")
        else:
            print("Sorry, that's incorrect. Your guess is too low. Try again.")

def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1, '\n-', num2)
    counter = 0
    while True:
        answer = int(input('What is the final answer? \n'))
        counter += 1
        if answer == num1 - num2:
            print(f'Congratulations! That\'s correct. You guessed it in {counter} attempts.')
            break
        elif answer > num1 - num2:
            print("Sorry, that's incorrect. Your guess is too high. Try again.")
        else:
            print("Sorry, that's incorrect. Your guess is too low. Try again.")

def main():
    while True:
        display_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            add_numbers()
        elif choice == '2':
            subtract_numbers()
        elif choice == '3':
            print('Come back soon...')
            break
        else:
            print('Invalid choice. Please enter 1, 2, or 3.')

if __name__ == '__main__':
    main()
