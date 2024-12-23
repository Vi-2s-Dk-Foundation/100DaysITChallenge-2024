# Let us get some inputs, 
# we saw outputs with "Hello World"

# Also we will see some operators in use
# As well as expressions...

age = input("Enter your age:\n")

# Cast input
age_int = int(age)

# Also sanitize aka Error Checking


# Conditionals: simple decision

if (age >= 18):
    # Use indentations
    print("You are an adult!")

    # Add alternative?
else:
    print("Your are NOT an adult...")


# Conditions could get complicated
# Chained or nested...

# Different! No switch, we use elif
# elif = short for else if

day_entry = int(input("Enter day[1-7]:\n"))

if day_entry == 1:
    print("Monday")
elif day_entry == 2:
    print("Tuesday")
else:
    print("Invalid Entry!")
# etc etc