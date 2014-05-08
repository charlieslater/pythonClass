def input_loop(prompt):
    while True:
        try:
            s = raw_input(prompt)
            if s:
                return s
        except EOFError:
            print("\nThanks for playing!")
            exit(0)

# Illustrated dictionary of lists
fromSelected = { "Level 1" : [2,3], "Level 2" : [2,4], "Level 3" : [3,4],
                 "Level 4" : [4,6], "Level 5" : [6,6], "Level 6" : [8,8]}
selected = input_loop("Level? ")
try:
    
    rows, cols = fromSelected[selected] # multiple assignement from list
except KeyError:
    print "'" + selected + "'",
    print "not of the form 'Level 1', 'Level 2', ..., 'Level 6'"
    exit(-1)
print "rows =", rows
print "cols =", cols
