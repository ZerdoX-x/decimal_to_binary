# get string
# user_input = str(input("Enter string: ")).split()
user_input = str(input("Enter string: "))
integers = [str(i) for i in range(10)]


# converting function
def decimal_to_binary(num):
    res = ""

    while num > 0:
        res += str(num % 2)
        num = num // 2

    return res[::-1]


for letter in user_input:
    if letter in integers:
        start = -1
        end = 0
        if start == -1 or user_input.index(letter) < start:           # if this is first digit of a number
            start = user_input.index(letter)                          # index of first digit of a number
            tmp = start                                               # increasing index of a number

        try:
            if user_input[tmp + 1] in integers:                       # if number goes on
                try:
                    while isinstance(int(user_input[tmp + 1]), int):  # while number goes on
                        tmp += 1                                      # increase index of last digit of a number
                    end = tmp
                except IndexError:                                    # if digit is a last character of a string
                    end = tmp                                         # 'end' is last available value
                    pass
        except ValueError:                                            # if number consists of one digit
            end = start                                               # number starts and ends on the same index


print(start, end)

# output
# print('Result: ', end="")
# for chunk in user_input:
#     print(chunk, end=" ")
# print('')
