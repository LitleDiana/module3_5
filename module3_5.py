def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if int(str_number) == 0:
    return 1

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result1 = get_multiplied_digits(10205)
result2 = get_multiplied_digits(91100)

print(result1)
print(result2)
