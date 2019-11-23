user_input, output = str(input()), []  # ask for input, name output
integers = [str(i) for i in range(10)]  # generate all digits with base 10


# function that takes number in num. system with base 10, and returns num. system with base 2
def decimal_to_binary(number):
    result = ""

    while number > 0:
        result += str(number % 2)
        number = number // 2

    return result[::-1]


first_symbol_of_chunk = 0  # variable that keeps index of first symbol for next chunk

# loop that splits string to a list:
for index, symbol in enumerate(user_input):
    try:
        # if ((symbol is not an integer)
        # & (next symbol is an integer)
        # & (index of a symbol is not lower than first symbol of next chunk))
        # OR ((symbol is an integer)
        # & (next symbol is not an integer)
        # & (index of a symbol is not lower than first symbol of next chunk)):
        if (symbol not in integers
                and user_input[index+1] in integers
                and index >= first_symbol_of_chunk)\
                or (symbol in integers
                    and user_input[index+1] not in integers
                    and index >= first_symbol_of_chunk):
            # add slice[from first symbol:to symbol's index that passed the conditions(incl.)] to the "output" list
            output.append(user_input[first_symbol_of_chunk:index+1])
            # next chunk's start = is the end of the previous chunk+1
            first_symbol_of_chunk = index+1
    # if you have reached the end of the list:
    # add slice[from first symbol:to the end of the string] to the "output" list
    except IndexError:  # IndexError: list index out of range
        output.append(user_input[first_symbol_of_chunk:])

# check if chunk is a number:
for index, chunk in enumerate(output):
    # number = number with base 2
    try:
        output[index] = decimal_to_binary(int(chunk))
    # if it's error (not a number) - pass
    except ValueError:
        pass

print(''.join(output))  # print all elements of list without separator
