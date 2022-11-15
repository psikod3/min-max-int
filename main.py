# Takes user inputs (numbers) and checks which ones are smallest and largest numbers.
# If input is invalid, users get error message.

largest = None
smallest = None
while True:
    num = input("Enter a number or 'check': ")
    if num == "check":
        break
    else:
        try:
            num = float(num)  # try "checks" if input is float (would give error if we try to float('bob')

            # can't compare numbers to None, so we need to assign 'starting numbers' to the variables
            if largest is None and smallest is None:
                largest = float(num)
                smallest = float(num)
                continue  # so loop will prompt for new input

            elif float(num) > largest:
                largest = float(num)
                continue

            elif float(num) < smallest:
                smallest = float(num)
                continue

        except:
            print("Invalid input.")
            continue

print("Maximum is", largest)
print("Minimum is", smallest)
