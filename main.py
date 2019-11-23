user_input, output = str(input()), []
integers = [str(i) for i in range(10)]


def decimal_to_binary(number):
    if number == 0:
        return "0"

    result = ""

    while number > 0:
        result += str(number % 2)
        number = number // 2

    return result[::-1]


first_symbol_of_chunk = 0
for index, symbol in enumerate(user_input):
    try:

        if (symbol not in integers
                and user_input[index+1] in integers
                and index >= first_symbol_of_chunk)\
                or (symbol in integers
                    and user_input[index+1] not in integers
                    and index >= first_symbol_of_chunk):
            output.append(user_input[first_symbol_of_chunk:index+1])
            first_symbol_of_chunk = index+1

    except IndexError:
        output.append(user_input[first_symbol_of_chunk:])

for index, chunk in enumerate(output):
    try:
        output[index] = decimal_to_binary(int(chunk))
    except ValueError:
        pass

print(''.join(output))
