def check(value):
    result = 0
    #Create Logic Here
    #Look a numbers in a pair. If they match then add it to result
    #Go to next number
    for index in range(0, len(value)):
        if value[index-1] == value[index]:
            result += int(value[index])
    return result


if __name__ == '__main__':
    assert check("1122") == 3
    assert check("1111") == 4
    assert check("1234") == 0
    assert check("9121212129") == 9
