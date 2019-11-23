user_input, output = str(input()), []  # переменные: ввод, вывод
integers = [str(i) for i in range(10)]  # генерируется список всех цифр в СС с основанием 10


# создаётся функция: принимает число в десятичной СС, возвращает число в двоичной СС
def decimal_to_binary(number):
    if number == 0:
        return "0"

    result = ""

    while number > 0:
        result += str(number % 2)
        number = number // 2

    return result[::-1]


first_symbol_of_chunk = 0  # переменная, отвечающая за начало каждого элемента в новом списке

# цикл, разбивающий строку на список:
for index, symbol in enumerate(user_input):
    try:
        # если ((символ в строке - не число) & (следующий символ - число) & (индекс символа не ниже начала элемента))
        # ИЛИ ((символ в строке - число) & (следующий символ - не число) & (индекс символа не ниже начала элемента)):
        if (symbol not in integers
                and user_input[index+1] in integers
                and index >= first_symbol_of_chunk)\
                or (symbol in integers
                    and user_input[index+1] not in integers
                    and index >= first_symbol_of_chunk):
            # добавить срез[от начала элемента:до индекса символа, прошедшего проверку включительно] в новый список
            output.append(user_input[first_symbol_of_chunk:index+1])
            # начало следующего элемента (чанка) = это конец предыдущего чанка + 1
            first_symbol_of_chunk = index+1
    # если достигли конца списка, т.е. если не существует элемента user_input[index+1], тогда:
    # исключение - добавить срез[от начала элемента:до конца строки] в новый список
    except IndexError:  # IndexError: list index out of range
        output.append(user_input[first_symbol_of_chunk:])

# цикл, проверяющий каждый элемент списка "output" (вывод) на то, является ли он числом:
for index, chunk in enumerate(output):
    # число = это число, обработанное функцией
    try:
        output[index] = decimal_to_binary(int(chunk))
    # если возникла ошибка (т.е. элемент не является числом): пропустить элемент
    except ValueError:
        pass

print(''.join(output))  # вывести в консоль все элементы списка "output" по порядку, без разделителя
