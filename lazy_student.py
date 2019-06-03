import sys
import os

HOMEWORK_FILE = 1
SOLUTION_FILE = 2
VALID_FILENAME = "homework.txt"
SOLUTION_FILENAME = "solution.txt"
VALID_OPERATIONS = ["+", "-", "*", "/"]


def check_for_errors(path):
    with open(path, "r") as file:
        wrong_equation_indexes = {}
        line_index = 0
        for line in file:
            args_in_line = line.split(' ')
            if len(args_in_line) != 3:
                wrong_equation_indexes[line_index] = "too many arguments\n"
            args_in_line[2] = args_in_line[2][:-1]
            if not (args_in_line[0].isdigit() and args_in_line[2].isdigit()):
                wrong_equation_indexes[line_index] = "not digits in the equation\n"
            if args_in_line[1] not in VALID_OPERATIONS:
                wrong_equation_indexes[line_index] = "not a valid operation\n"
            if args_in_line[1] == '/' and args_in_line[2] == '0':
                wrong_equation_indexes[line_index] = "cannot divide by zero\n"
            line_index += 1
        return wrong_equation_indexes


def count_number_of_lines(path):
    with open(path, "r") as file:
        number_of_lines = 0
        for line in file:
            number_of_lines += 1
        return number_of_lines


def load_homework(homework_path):
    """
    will load the file if the file exists and valid, and will check the input
    :param homework_path
    :return: Array with indexes of wrong equations
    """
    check_filename_exists_and_valid(homework_path)
    lines_with_errors = check_for_errors(homework_path)
    copy_file(VALID_FILENAME, SOLUTION_FILENAME)
    list_of_lines = []
    with open(SOLUTION_FILENAME, 'r') as solution_file:
        line_index = 0
        for line in solution_file:
            line = line[:-1]
            if line_index in lines_with_errors:
                line = line + " ERROR: " + lines_with_errors[line_index]
            else:
                solution = calculate_solution(line.split(' '))
                line = line + " = " + str(solution) + "\n"
            list_of_lines.append(line)
            line_index += 1
    with open(SOLUTION_FILENAME, 'w') as solution_file:
        solution_file.writelines(list_of_lines)


def calculate_solution(equation_in_list):
    """
    gets a valid equation and calculates it by required operation
    :param equation_in_list:
    :return: solution
    """
    arg1 = float(equation_in_list[0])
    arg2 = float(equation_in_list[2])
    operation = equation_in_list[1]
    if operation == '+':
        return arg1 + arg2
    elif operation == '-':
        return arg1 - arg2
    elif operation == '*':
        return arg1 * arg2
    elif operation == '/':
        return arg1 / arg2
    else:
        exit("Unknown Error in calculate_solution function")


def copy_file(source_path, destination_path):
    with open(source_path, "r") as source_file:
        with open(destination_path, "w") as dest_file:
            for line in source_file:
                dest_file.write(line)


def check_filename_exists_and_valid(path_name):
    """
    check for valid filename
    :param path_name: "homework.txt"
    :return: True if correct, False elsewhere
    """
    if path_name != VALID_FILENAME:
        exit("Error in filename")
    if not os.path.exists(path_name):
        exit("Such file doesn't exist!")


def main():
    load_homework(VALID_FILENAME)


if __name__ == "__main__":
    main()
