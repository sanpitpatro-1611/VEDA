def execute(memory, line):

    content = line[9:].strip()

    if ":" not in content:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Invalid remember syntax.")
        print("")
        print("Correct Syntax:")
        print("remember variable: value")
        print("===================================")
        return

    name, value = content.split(":", 1)

    name = name.strip()
    value = value.strip()

    if name == "":

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Variable name cannot be empty.")
        print("")
        print("Example:")
        print("remember age: 20")
        print("===================================")
        return

    if value == "":

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Variable value cannot be empty.")
        print("")
        print("Example:")
        print("remember age: 20")
        print("===================================")
        return

    memory[name] = value