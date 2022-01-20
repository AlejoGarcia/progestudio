#! /usr/bin/python
import csv
import random
import os

print("QuickCard STUDING PROGRAM")

def read_input_val(initial_msg, fail_msg, pos_values, bad_values):
    buffer = input(initial_msg)
    if pos_values == []:
        while buffer in bad_values:
            print(fail_msg)
            buffer = input(initial_msg)
    else:
        while buffer not in pos_values:
            print(fail_msg)
            buffer = input(initial_msg)
    return buffer

def create_file():
    name = input("Input file name: ") + ".csv"
    print("Creating file...")
    with open(name, "w", newline='') as file:
        fieldnames = ['question', 'answer']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        while True:
            another = read_input_val("You want to write another row?[y/n]: ", "Wrong input", ["y", "n"], [])
            if another == "y":
                question = read_input_val("Introduce the question: ", "Question cannot be 'exit'.", [], ["exit"])
                answer =  read_input_val("Introduce the answer: ", "Answer cannot be 'exit'.", [], ["exit"])
                writer.writerow({'question': question, 'answer': answer})
            else:
                print("Saving new file(" + name + ") ...")
                break

            
def use_file():
    name = input("Input file name: ") + ".csv"
    correct_list = []
    failed_list = []

    try:
        with open(name, newline='') as file:
            print("Opening file '" + name + "'...")
            for line in csv.reader(file):
                failed_list.append(tuple(line))
            failed_list.pop(0)
    except Exception:
        print("Failed to open file. File may not exist.")
        return

    if read_input_val("Which mode of study you want to use? [n-options: nopt, quickcard: qcard]: ", "Wrong input.", ["nopt", "qcard"], []) \
            == "nopt":
        number_opt = int(input("How many options?: "))
        while number_opt < 2:
            print("Number of options must be bigger than 1.")
            number_opt = int(input("How many options?: "))
    else:
        number_opt = 1

    while (number := int(input("Continious mode or 'x' questions? [continious: 0, xquest: n]: "))) < 0:
        print("Wrong input. Must be positive or zero.")
    n = 1
    correct_answers = 0     
    res = "" 
    print("el numero de preguntas es", number)

    while failed_list != [] and res != "exit":
        os.system('cls' if os.name == 'nt' else 'clear')
        quest = do_question(n, number_opt, failed_list, correct_list)
        read_input_val("To see solution pulse enter : ", "Wrong input.", [""], [])
        print("SOLUTION:")
        print(failed_list[quest][1])
        res = read_input_val("Was right? (to exit write 'exit') [y/n/exit]: ", "Wrong input.", ["y", "n", "exit"], [])
        if res == "y":
            print("Congratulations!!!")
            correct_answers += 1
            correct_list.append(failed_list.pop(quest))
        else:
            print("You'll get it next time")
        n += 1
        if number > 0 and n > number:
            break
    print("You got", correct_answers, "answers correct of", number)

def do_question(number, options, list_questions, list2):
    print("QUESTION " + str(number) + ":")
    number = random.randrange(0, len(list_questions))
    print(list_questions[number][0])
    if options > 1:
        if options > len(list_questions):
            options = len(list_questions)
        option_list =[]
        option_list.append(list_questions[number][1])
        long_list = []
        for i in list_questions + list2:
            long_list.append(i[1])
        for i in range(1, options):
            option = option_list[0]
            while option in option_list: 
                option = long_list.pop(random.randrange(0, len(long_list)))
            option_list.append(option)
        random.shuffle(option_list)
        print("OPTIONS:")
        for i in option_list:
            print(" -> " + i)
    return number

# Ask for action to take
while True: 
    mode = input("You want to create or use a file?[c/u/q]: ")
    if mode == "c":
        create_file()
    elif mode == "u":
        use_file()
    elif mode == "q":
        print("Exiting program...")
        break
    else:
        print("Wrong input.")
