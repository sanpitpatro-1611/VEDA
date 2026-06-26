def execute(memory, result_name, left_var, operator, right_var):

    if left_var not in memory:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print(f'Variable "{left_var}" does not exist.')
        print("")
        print("Create it first using:")
        print(f"remember {left_var}: value")
        print("===================================")
        return

    if right_var not in memory:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print(f'Variable "{right_var}" does not exist.')
        print("")
        print("Create it first using:")
        print(f"remember {right_var}: value")
        print("===================================")
        return

    try:
        left = float(memory[left_var])
        right = float(memory[right_var])

    except:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Calculation requires numeric values.")
        print("===================================")
        return

    if operator == "+":
        result = left + right

    elif operator == "-":
        result = left - right

    elif operator == "*":
        result = left * right

    elif operator == "/":

        if right == 0:

            print("===================================")
            print("VEDA ERROR")
            print("-----------------------------------")
            print("Cannot divide by zero.")
            print("===================================")
            return

        result = left / right

    else:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print(f'Unknown operator "{operator}".')
        print("Supported operators: +  -  *  /")
        print("===================================")
        return

    memory[result_name] = str(result)