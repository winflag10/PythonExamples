def convert(number)
    number = reversed(number)
    column_value = 1
    total = 0
    for bit in number:
        bit = int(bit)
        bit = bit * column_value
        column_value = column_value * 2
        total += bit
    return total
