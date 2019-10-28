import random
import csv


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split("!") for element in lines]
    return table


def csv_reader(file_name):
    reader = csv.reader(open(file_name, 'r'))
    data = sum([i for i in reader], [])
    return random.choice(data)
