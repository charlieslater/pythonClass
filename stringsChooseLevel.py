def input_loop(prompt):
    while True:
        try:
            s = raw_input(prompt)
            if s:
                return s
        except EOFError:
            print("\nThanks for playing!")
            exit(0)

def print_error_and_exit():
    print selected,"indicates level:", level
    print "valid levels are 1 through 6"
    exit (-1)

rows_cols = [[2,3],[2,4],[3,4],[4,6],[6,6],[8,8]]
selected = input_loop("Level? ")
try: 
    level = int(selected[-1])
except ValueError:
    print "selected string '" + selected + "' should end in a digit"
    exit(-1)
print "level =", level
if level < 1:
    print_error_and_exit()
try:
    rows, cols = rows_cols[level - 1]
except IndexError:
    print_error_and_exit()

print "rows =", rows
print "cols =", cols
