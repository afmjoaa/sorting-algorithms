import constants


def sort(unsorted_list: list) -> list:
    list_length = len(unsorted_list)
    swapped = True
    i = 0
    while swapped:
        swapped = False
        for j in range(list_length - i - 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                swapped = True
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
        i += 1
    return unsorted_list


def default_array_sort() -> list:
    return sort(constants.MY_DEFAULT_ARRAY)


def one_to_nine_sort() -> list:
    return sort(constants.ARRAY_ONE_TO_NINE)


