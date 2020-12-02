start = 137683
end = 596253


def evalNumber(number):
    numberList = [int(x) for x in list(str(number))]
    double = False
    for n, num in enumerate(numberList[1:]):
        if numberList[n] > num:
            return False

        if numberList[n] == num:
            if numberList.count(num) == 2:
                double = True

    return double

possible_pwd = []
for num in range(start, end+1):
    if evalNumber(num):
        possible_pwd.append(num)



print(len(possible_pwd))

