def checkStepNumbers(systemNames, stepNumbers):
    systems = {}
    for system, step in zip(systemNames, stepNumbers):
        if system not in systems:
            systems[system] = [step]
        else:
            systems[system].append(step)
    
    for system in systems:
        steps = systems[system]
        if any([step <= steps[i-1] for i, step in enumerate(steps)][1:]):
            return False
    return True


systemNames = ["tree_1", "tree_2", "house", "tree_1", "tree_2", "house"]
stepNumbers = [1, 33, 10, 2, 44, 20]

print(checkStepNumbers(systemNames, stepNumbers))