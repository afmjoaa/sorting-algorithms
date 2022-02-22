import constants


def sort(unsorted_list: list) -> list:
    list_length = len(unsorted_list)
    for i in range(list_length):
        current_min = i
        for j in range(i+1, list_length):
            if unsorted_list[current_min] > unsorted_list[j]:
                current_min = j
        if current_min != i:
            unsorted_list[i], unsorted_list[current_min] = unsorted_list[current_min], unsorted_list[i]

    return unsorted_list


def default_array_sort() -> list:
    return sort(constants.MY_DEFAULT_ARRAY)


def one_to_nine_sort() -> list:
    return sort(constants.ARRAY_ONE_TO_NINE)


