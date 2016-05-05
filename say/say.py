
digits_to_words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

denominations = ['ones', 'tens', 'hundreds']


def say(integer):
    list_of_ints = [int(l) for l in str(integer)]
    if integer < 21:
        return digits_to_words[integer]
    elif integer < 99:
        return between_21_and_99(list_of_ints)
    elif integer == 100:
        return "one hundred"
    elif integer < 1000:
        return greater_than_100(list_of_ints)
    elif integer == 1000:
        return "one thousand"
    elif integer < 10000:
        return greater_than_1000(list_of_ints)


def between_21_and_99(integer_list):
    response = []
    tens = integer_list[0] * 10
    ones = integer_list[-1]
    response.append(digits_to_words[tens])
    response.append(digits_to_words[ones])
    return '-'.join(response)

def greater_than_100(integer_list):
    hundreds = say(integer_list[0])
    tens = get_tens(integer_list, 1,2)
    tens = say(int(tens))
    return hundreds + ' hundred and ' + tens

def greater_than_1000(integer_list):
    thousands = say(integer_list[0])
    hundreds = say(integer_list[1])
    tens = get_tens(integer_list, 2, 3)
    tens = say(int(tens))
    return thousands + ' thousand ' + hundreds +' hundred and ' + tens

def get_tens(integer_list, first_index, second_index):
    return str(integer_list[first_index]) + str(integer_list[second_index])


