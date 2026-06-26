def execute(memory, result_name, left_var, operator, right_var):

    # ----------------------------
    # Resolve LEFT operand
    # ----------------------------
    if left_var in memory:
        left = memory[left_var]
    else:
        left = left_var

    # ----------------------------
    # Resolve RIGHT operand
    # ----------------------------
    if right_var in memory:
        right = memory[right_var]
    else:
        right = right_var

    # ----------------------------
    # Convert to numbers
    # ----------------------------
    try:
        left = float(left)
        right = float(right)

    except:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Calculation requires numeric values.")
        print("===================================")
        return

    # ----------------------------
    # Perform calculation
    # ----------------------------
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

    # ----------------------------
    # Save Result
    # ----------------------------
    memory[result_name] = str(result)