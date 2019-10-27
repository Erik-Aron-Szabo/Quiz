import time
import quiz
import practice
import quiz_adder


def main():
    user_input = introduction()

    if user_input == 1:
        quiz.simple_quiz()
    elif user_input == 2:
        practice.Scripture_practice()
    elif user_input == 3:
        print() # under construction
    elif user_input == 4:
        quiz_adder.quiz_adder("quiz_file.csv")
    elif user_input == 5:
        exit()
    return_to_main_menu()
    

def introduction():
    print("Welcome to the MAIN MENU!")
    print("What would you like to do?")
    print("Please choose an option!")
    print("----------------------------")
    print("(1) Bible Quiz")
    print("(2) Practice Scriptures")
    print("(3) Practice Words")
    print("(4) Add New Scriptures")
    print("(5) Quit")

    user_input = int(input("Your choice: "))

    return user_input

def return_to_main_menu():
    time.sleep(3)
    print("Return?")
    user_input = int(input("Press 0 to return to main menu."))
    if user_input == 0:
        main()

    return user_input

if __name__ == '__main__':
    main()
