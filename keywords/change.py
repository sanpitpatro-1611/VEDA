def execute(memory, variable_name, value):

    if variable_name not in memory:

        print("===================================")
        print("VEDA ERROR")
        print("-----------------------------------")
        print(f'Variable "{variable_name}" does not exist.')
        print("")
        print("Create it first using:")
        print(f"remember {variable_name}: value")
        print("===================================")
        return

    memory[variable_name] = value