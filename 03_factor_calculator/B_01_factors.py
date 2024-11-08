def statement_generator(statement, decoration):  # prints statement with fancy decoration
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
To use this program simply enter an integer between 
1 and 200. The program will show the factors of your 
chosen integer

It will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type "xxx"
    ''')


# check whether input is an integer between 1 and 200
def num_check(question):
    error = "Please enter an integer\n"
    while True:

        response = input(question).lower()
        if response == "xxx":  # check if user quits
            return response

        try:
            # ask user for a number
            response = int(response)

            if 1 <= response <= 200:  # check that response is within 1 to 200
                return response  # ends loop
            elif response < 1:
                print("Please enter an integer that is more than (or equal to) 1\n")
            elif response > 200:
                print("Please enter an integer that is less than (or equal to) 200\n")

        except ValueError:  # prevents string input
            print(error)


# works out factors and returns a sorted list
def factor(var_to_factor):
    # square root the number to work out when we stop working
    stop = int(to_factor ** 0.5)
    stop = int(stop)
    factors_list = []

    for item in range(1, stop + 1):

        # if modulo is zero, then the number is a factor
        if to_factor % item == 0:

            # find second factor by dividing 'to_factor' by the first factor
            partner = to_factor // item

            # add first factor to the list
            factors_list.append(item)

            # check second factor is not in the list and add it
            if partner not in factors_list:
                factors_list.append(partner)

    # output
    factors_list.sort()
    return factors_list


# Main routine here
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask user what number they want to factor

    to_factor = num_check("Enter an integer to factor (or press 'xxx' to quit): ")

    # quit
    if to_factor == "xxx":
        break

    # get factors for integers that are 2 or more. 1 is a unity number
    elif to_factor != 1:
        all_factors = factor(to_factor)

    # comment for unity
    else:
        all_factors = ""
        comment = "One is a unity number. It only has one factor which is itself.\n"

    # comments for squares/primes

    # prime numbers have two factors only
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number.\n"

    # check if the list has an odd amount of items
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square\n"

    # headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special."

    # output factors and comments
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator")