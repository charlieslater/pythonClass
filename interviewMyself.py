import sys

def getline(prompt):
    if int(sys.version_info.major) >= 3:
        input_str = input(prompt)
    else:
        input_str = raw_input(prompt)
    return input_str

def input_loop(prompt):
    while True:
        try:
            s = getline(prompt)
            if s:
                return s
        except EOFError:
            print("\ninterview ended early")
            exit(0)

answer = input_loop("Are you interested in programming? ")
if answer.lower().find("y") < 0:
    print("I'll take that as a 'no'")
    exit(0)
answer = input_loop("Do you know what you want to do? ")
if answer.lower().find("y") < 0:
    print("I'll take that as a 'no'.  We'll give you some ideas to think about.")
else:
    print("Excellent!")

