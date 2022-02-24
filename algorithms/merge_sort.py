import constants


def sort(unsorted_list: list):
    list_length = len(unsorted_list)
    if list_length > 1:
        left_arr = unsorted_list[:list_length//2]
        right_arr = unsorted_list[list_length//2:]

        sort(left_arr)
        sort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                unsorted_list[k] = left_arr[i]
                i += 1
            else:
                unsorted_list[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            unsorted_list[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            unsorted_list[k] = right_arr[j]
            j += 1
            k += 1


def default_array_sort() -> list:
    sort(constants.MY_DEFAULT_ARRAY)
    return constants.MY_DEFAULT_ARRAY


def one_to_nine_sort() -> list:
    sort(constants.ARRAY_ONE_TO_NINE)
    return constants.ARRAY_ONE_TO_NINE

