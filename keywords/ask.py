def execute(memory, line):

    content = line[4:].strip()

    if ":" not in content:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Invalid ask syntax.")
        print("")
        print("Correct Syntax:")
        print("ask variable: Your Question")
        print("===================================")
        return

    name, question = content.split(":", 1)

    name = name.strip()
    question = question.strip()

    if name == "":

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Variable name cannot be empty.")
        print("")
        print("Example:")
        print("ask name: What is your name?")
        print("===================================")
        return

    if question == "":

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print("Question cannot be empty.")
        print("")
        print("Example:")
        print("ask name: What is your name?")
        print("===================================")
        return

    answer = input(question + " ")

    memory[name] = answer