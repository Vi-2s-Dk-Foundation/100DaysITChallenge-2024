# Repeat a block of code

# - Definite/Known number of times = for
# - Indefinite/Unknown = while

# avoid infinite loops!

# Simple

counter = 0

for counter in range(5):
    print(f"Counter: {counter}")
    # using f-string for output

# Set counter during while loop
# count down!

new_counter = 10

while new_counter >=0 :
    print(new_counter)
    new_counter -=1     # decrement operator
    # python does not use -- 

# No do-while loop present
