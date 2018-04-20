def checksum(row):
    #7 0 2 4
    numbers = row.split()
    min = None
    max = None
    for n in numbers:
        number = int(n)
        if min is None or min > number:
            min = number
        if max is None or max < number:
            max = number
    return max-min

if __name__ == '__main__':
    code = "5 1 9 5
7 5 3
2 4 6 8"
    rows = code.split("\n")
    checksum = 0
    for row in rows:
        checksum += checksum(row)
    print(checksum)