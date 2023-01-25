def add_nums(list):
    """Adds given set of numbers. """
    print(f"The sum is {sum(list)}")

# Adding numbers to a list so the function can add them
numbers = []
active = True
while active:
    add = input("Please enter a number: ")
    try:
        add = int(add)
    except:
        if add == "":
            pass
        else:
            print("Please enter a number.")
    if add == "":
        print("You entered a blank line. Adding 0 to the list of numbers.")
        numbers.append(0)
    else:
        print(f"{add} added to list of numbers.")
        numbers.append(add)
    again = input("Would you like to add another number? \n Type Y or N: ").upper()
    if again == "Y":
        print("OK.")
        continue
    elif again == "N":
      add_nums(numbers)
      active = False
      