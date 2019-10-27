import time
import file_manipulations
import random


def simple_quiz():
    round_count = int(input("How many rounds do you want to play?\n(Type a number!):"))

    for i in range(round_count):   
        temp = file_manipulations.get_table_from_file("quiz_file.csv")
        random_scripture = random.randint(0,24)
        question1 = temp[random_scripture]

        string_from_list = ''.join(question1)

        print("-"*len(string_from_list))
        print(question1[0])
        print("-"*len(string_from_list))
        print("Please write down the correct KJV Scripture!\nOr write down from which Scripture the quote is from!\n")
        
        user_answer = input("Which Bible Scripture is it?\n")


        if user_answer == question1[1]:
            print("Congratulation!")
        time.sleep(5)
        print(f"The correct answer is: {question1[1]}!\n\n")
