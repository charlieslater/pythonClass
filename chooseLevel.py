def input_loop(prompt):
    while True:
        try:
            s = raw_input(prompt)
            if s:
                return s
        except EOFError:
            print("\nThanks for playing!")
            exit(0)

rowsFromLevel = { "Level 1" : 2, "Level 2" : 2, "Level 3" : 3, "Level 4" : 4, "Level 5" : 6, "Level 6" : 8}
colsFromLevel = { "Level 1" : 3, "Level 2" : 4, "Level 3" : 4, "Level 4" : 6, "Level 5" : 6, "Level 6" : 8}
selected = input_loop("Level? ")
print "rows =", rowsFromLevel[selected]
print "cols =", colsFromLevel[selected]
