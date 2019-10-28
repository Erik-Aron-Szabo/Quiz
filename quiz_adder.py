import main
import csv



def quiz_adder(file_name):
    while True:
        quote = input("Write the Scripture quote:\n")
        address = input("Write the Scripture address:\n")
        with open(file_name, "a") as f:
            f.writelines(quote + "!" + address + "\n")
        if quote == "0":
            break
    main.return_to_main_menu()