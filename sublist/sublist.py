
def SUBLIST():
    pass


def SUPERLIST():
    pass


def EQUAL():
    pass


def UNEQUAL():
    pass


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    elif len(first_list) == 0 or all(i in second_list for i in first_list):
        return SUBLIST
    elif len(second_list) == 0 or all(i in first_list for i in second_list):
        return SUPERLIST
    else:
        return UNEQUAL
