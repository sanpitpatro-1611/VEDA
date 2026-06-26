from keywords.say import execute as say_execute
from keywords.remember import execute as remember_execute
from keywords.ask import execute as ask_execute
from keywords.repeat import execute as repeat_execute
from keywords.action import execute as action_execute
from keywords.do import execute as do_execute
from keywords.calculate import execute as calculate_execute
from keywords.change import execute as change_execute


memory = {}
actions = {}
last_if_result = False


def execute_say(message):
    if message in memory:
        print(memory[message])
    else:
        print(message)


with open("main.veda", "r") as file:
    lines = file.readlines()

i = 0

while i < len(lines):

    line = lines[i].rstrip()

    if not line.strip():
        i += 1
        continue
    
    if line.strip().startswith("#"):
        i += 1
        continue

    # SAY
    if line.startswith("say:"):
      say_execute(memory, line.strip())

    # REMEMBER
    elif line.strip().startswith("remember "):
        remember_execute(memory, line.strip())

    # ASK
    elif line.strip().startswith("ask "):
         ask_execute(memory, line.strip())

    # IF
       # IF
    elif line.strip().startswith("if "):

        last_if_result = False

        condition = line.strip()[3:]
        parts = condition.split()

        variable = parts[0]

        if len(parts) == 3:
            operator = parts[1]
            value = parts[2]

        elif len(parts) == 4:
            operator = parts[1] + " " + parts[2]
            value = parts[3]

        elif len(parts) == 6:
            operator = " ".join(parts[1:5])
            value = parts[5]

        else:
            i += 1
            continue

        if variable in memory:

            try:
                left = float(memory[variable])
                right = float(value)
            except:
                left = memory[variable]
                right = value

            if operator == "greater than":
                last_if_result = left > right

            elif operator == "less than":
                last_if_result = left < right

            elif operator == "equals":
                last_if_result = str(left) == str(right)

            elif operator == "not equals":
                last_if_result = str(left) != str(right)

            elif operator == "greater than or equals":
                last_if_result = left >= right

            elif operator == "less than or equals":
                last_if_result = left <= right

            if last_if_result:

                if i + 1 < len(lines):

                    next_line = lines[i + 1]

                    if next_line.startswith("    "):

                        next_line = next_line.strip()

                        if next_line.startswith("say:"):
                            msg = next_line[4:].strip()
                            execute_say(msg)

                        i += 1

        # ACTION
    elif line.strip().startswith("action "):

        action_name = line.strip()[7:].strip()

        if i + 1 < len(lines):

            next_line = lines[i + 1]

            if next_line.startswith("    "):

                command = next_line.strip()

                action_execute(
                    actions,
                    action_name,
                    command
                )
                

                i += 1    

        # CHANGE
    elif line.strip().startswith("change "):

        content = line.strip()[7:]

        if ":" in content:

            variable_name, value = content.split(":", 1)

            change_execute(
                memory,
                variable_name.strip(),
                value.strip()
            )            

        # CALCULATE
    elif line.strip().startswith("calculate "):

        content = line.strip()[10:]

        if ":" in content:

            result_name, expression = content.split(":", 1)

            result_name = result_name.strip()

            parts = expression.strip().split()

            if len(parts) == 3:

                left_var = parts[0]
                operator = parts[1]
                right_var = parts[2]

                calculate_execute(
                    memory,
                    result_name,
                    left_var,
                    operator,
                    right_var
                )            

        # DO
    elif line.strip().startswith("do "):

        action_name = line.strip()[3:].strip()

        command = do_execute(
            actions,
            action_name
        )

        if command:

            if command.startswith("say:"):

                say_execute(
                    memory,
                    command
                )

        # REPEAT
    elif line.strip().startswith("repeat "):

        words = line.strip().split()

        if len(words) >= 3:

            count = int(words[1])

            if i + 1 < len(lines):

                next_line = lines[i + 1]

                if next_line.startswith("    "):

                    next_line = next_line.strip()

                    if next_line.startswith("say:"):

                        repeat_execute(
                            count,
                            {
                                "type": "say",
                                "function": say_execute,
                                "memory": memory,
                                "line": next_line
                            }
                        )

                        i += 1                        

    # OTHERWISE
    elif line.strip() == "otherwise":

        if not last_if_result:

            if i + 1 < len(lines):

                next_line = lines[i + 1]

                if next_line.startswith("    "):

                    next_line = next_line.strip()

                    if next_line.startswith("say:"):
                        msg = next_line[4:].strip()
                        execute_say(msg)

                    i += 1

    i += 1