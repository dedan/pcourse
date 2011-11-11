

# this small exercise will improve your algorithmic thinking.
# Play with the short script. For some input it works perfectly, for some
# it produces an error. Please fix the script in a way that it works for all
# input and explain what the error was.

siblings_string = raw_input("do you have siblings? ")

if siblings_string == "yes":
    no_string = raw_input("how many? ")
    no_int = int(no_string)

if no_int > 0:
    print("You have")
    print(no_int)
    print("siblings. Very nice.")
