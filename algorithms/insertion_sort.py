import constants


def sort(unsorted_list: list) -> list:
    list_length = len(unsorted_list)
    for i in range(1, list_length):
        current = unsorted_list[i]
        j = i - 1

        while j >= 0 and unsorted_list[j] > current:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1

        unsorted_list[j+1] = current
    return unsorted_list


def default_array_sort() -> list:
    return sort(constants.MY_DEFAULT_ARRAY)


def one_to_nine_sort() -> list:
    return sort(constants.ARRAY_ONE_TO_NINE)

