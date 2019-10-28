import main
import time
import random
import file_manipulations

def Scripture_practice():
    print("-------------------")
    print("\nPress 0 to quit!\n")
    print("Answer in a format like: '1Jn 3:8'")
    while True:
        temp = file_manipulations.get_table_from_file("quiz_file.csv")
        random_scripture = random.randint(0,14)
        question1 = temp[random_scripture]
        print(question1[0])
        user_answer = input("Which scripture is it?\n:")
        time.sleep(5)
        correct_answer = question1[1]
        print()
        print("The correct answer is: " + correct_answer)
        if user_answer == correct_answer:
            print("Congratulations!\n\n")
        if user_answer == "0":
            break
    main.return_to_main_menu()


#def Words_practice(): (((Under construction)))
