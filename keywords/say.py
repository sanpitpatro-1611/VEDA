import re

def execute(memory, line):

    message = line[4:].strip()

    # Whole variable
    if message in memory:
        print(memory[message])
        return

    # Find all placeholders like {name}
    placeholders = re.findall(r"\{(.*?)\}", message)

    for variable in placeholders:

        if variable not in memory:

            print("===================================")
            print("VEDA ERROR")
            print("-----------------------------------")
            print(f'Variable "{variable}" does not exist.')
            print("")
            print("Create it first using:")
            print(f"remember {variable}: value")
            print("===================================")
            return

    # Replace placeholders
    for key in memory:

        placeholder = "{" + key + "}"

        if placeholder in message:

            message = message.replace(
                placeholder,
                str(memory[key])
            )

    print(message)