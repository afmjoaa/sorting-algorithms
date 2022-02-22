import constants


def sort(unsorted_list: list) -> list:
    list_length = len(unsorted_list)
    if list_length <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list.pop()

    unsorted_list_greater = []
    unsorted_list_lower = []

    for item in unsorted_list:
        if item > pivot:
            unsorted_list_greater.append(item)
        else:
            unsorted_list_lower.append(item)

    return sort(unsorted_list_lower) + [pivot] + sort(unsorted_list_greater)


def default_array_sort() -> list:
    return sort(constants.MY_DEFAULT_ARRAY)


def one_to_nine_sort() -> list:
    return sort(constants.ARRAY_ONE_TO_NINE)

