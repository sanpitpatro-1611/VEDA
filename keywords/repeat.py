def execute(count, action):

    for _ in range(count):

        if action["type"] == "say":

            action["function"](action["memory"], action["line"])