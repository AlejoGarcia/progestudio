#! /usr/bin/python
import csv
import random

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
                print("Saving new file(", name, ") ...")
                break
        file.close()

            
def use_file():
    name = input("Input file name: ") + ".csv"
    correct_list = []
    failed_list = []
    try:
        with open(name, newline='') as file:
            print("Opening file '" + name + "'...")
            for line in csv.reader(file):
                failed_list.append(tuple(line))
    except Exception:
        print("Failed to open file. File may not exist.")
        #return
    if read_input_val("Which mode of study you want to use? [n-options: nopt, quickcard: qcard]: ", "Wrong input.", ["nopt", "qcard"], []) \
            == "nopt":
        number_opt = int(input("How many options?: "))
        while number_opt < 2:
            print("Number of options must be bigger than 1.")
            number_opt = int(input("How many options?: "))
    else:
        number_opt = 1
    number = int(input("Continious mode or 'x' questions? [continious: 0, xquest: n]: ")) 
    while number < 0:
        print("Wrong input. Must be positive or zero.")
        number = int(input("Continious mode or 'x' questions? [continious: 0, xquest: n]: ")) 
    if number == 0:
        while failed_list != []:
            quest = do_question(number_opt, failed_list, correct_list)
            read_input_val("To se solution pulse enter: ", "Wrong input.", [""], [])
            print("SOLUTION:")
            solution = failed_list[quest]
            print(solution[1])
            res = read_input_val("Was right?: [y/n]", "Wrong input.", ["y", "n"], [])
            if res == "yes":
                print("Congratulations!!!")
                correct_list.append(failed_list.pop(quest))
            else:
                print("You'll get it next time")
            if read_input_val("Want to do another?: [y/n]", "Wrong input.", ["y", "n"], []) == "n":
                break
    else:
        n = number
        correct_answers = 0
        while failed_list != [] and n > 0:
            quest = do_question(number_opt, failed_list, correct_list)
            read_input_val("To se solution pulse enter: ", "Wrong input.", [""], [])
            print("SOLUTION:")
            print(failed_list[quest][2])
            res = read_input_val("Was right?: [y/n]", "Wrong input.", ["y", "n"], [])
            if res == "yes":
                print("Congratulations!!!")
                correct_list.append(failed_list.pop(quest))
            else:
                print("You'll get it next time")
        print("You got", correct_answers, "answers correct of", number + ".")

def do_question(options, list_questions, list2):
    number = random.randint(0, len(list_questions))
    print("QUESTION:")
    question = list_questions[number]
    print(question[0])
    if options > 1:
        long_list = list_questions + list2
        option_list = []
        option_list.append(list_questions[number])
        for i in range(1, options):
            option_list.append(long_list.pop(random.randint(0,len(long_list))))
        random.shuffle(option_list)
        print("OPTIONS:")
        for i in option_list:
            print(" -> " + i[1])
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
