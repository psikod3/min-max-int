# Takes user inputs (integers) and checks which ones are smallest and largest numbers.
# If input is invalid, users gets error message.


largest = None
smallest = None
while True:
    num = input("Enter a number or 'done': ")
    if num == "done":
        break

    else:
        try:
            num = int(num)  # try "checks" if input is integer (would give error if you try to int('bob')

            if largest is None: # can't compare numbers to None, so we need to assign 'starting number' to the variable
                largest = int(num)
                continue  # so loop will prompt for new input

            elif smallest is None:
                smallest = int(num)
                continue

            elif int(num) > largest:
                largest = int(num)
                continue

            elif int(num) < smallest:
                smallest = int(num)
                continue

        except:
            print("Invalid input (must be integer).")
            continue

print("Maximum is", largest)
print("Minimum is", smallest)