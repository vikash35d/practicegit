

HISTORY_FILE = "history.txt"

def show_history():
    file= open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history available.")
    else:
        for line in lines:
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.write("")
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Use: <number> <operator> <number>")
        return

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Division by zero is not allowed.")
            return 
        result = num1 / num2    
    else:
        print("Invalid operator. Use: +, -, *, /")   
    return


    result = calculate(user_input)    
    if int(result) == result:
        result = int(result)
    print(f"The result of {user_input} is: {result}")
    save_to_history(user_input, result)
    return


def main():
    while True:
        user_input = input("Enter your equation (or 'history' to view history, 'clear' to clear history, 'exit' to quit): ")
        if user_input == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == "history":
            show_history()
            continue            
        elif user_input == "clear":
            clear_history()
            continue
        else:
            calculate(user_input)



main()
# calculator.py
# This script implements a simple calculator that can perform basic arithmetic operations
# and maintain a history of calculations in a text file.
