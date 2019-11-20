# get string
user_input = str(input("Enter string: ")).split()


# converting function
def decimal_to_binary(num):
    res = ""

    while num > 0:
        res += str(num % 2)
        num = num // 2

    return res[::-1]


# parse string, convert nums
for chunk in user_input:
    try:
        if int(chunk):  # if chunk(word) can be translated to integer: convert this number
            user_input[user_input.index(chunk)] = decimal_to_binary(int(chunk))
    except ValueError:
        pass  # exception for chunks that can't be translated into integer

# output
print('Result: ', end="")
for chunk in user_input:
    print(chunk, end=" ")
print('')
