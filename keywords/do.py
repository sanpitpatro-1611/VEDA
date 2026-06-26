def execute(actions, action_name):

    if action_name in actions:
        return actions[action_name]

    return []