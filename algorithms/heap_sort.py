import constants


def swap(lst: list, i: int, j: int):
    lst[i], lst[j] = lst[j], lst[i]


def shift_down(lst: list, i: int, upper: int):
    while True:
        l, r = i*2+1, i*2+2
        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]):
                break
            elif lst[l] > lst[r]:
                swap(lst, l, i)
                i = l
            else:
                swap(lst, r, i)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, l, i)
                i = l
            else:
                break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, r, i)
                i = r
            else:
                break
        else:
            break


def sort(unsorted_list: list):
    list_length = len(unsorted_list)
    for j in range((list_length-2//2), -1, -1):
        shift_down(unsorted_list, j, list_length)

    for end in range(list_length-1, 0, -1):
        swap(unsorted_list, 0, end)
        shift_down(unsorted_list, 0, end)


def default_array_sort() -> list:
    sort(constants.MY_DEFAULT_ARRAY)
    return constants.MY_DEFAULT_ARRAY


def one_to_nine_sort() -> list:
    sort(constants.ARRAY_ONE_TO_NINE)
    return constants.ARRAY_ONE_TO_NINE

