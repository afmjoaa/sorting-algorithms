import algorithms.bubble_sort as bubble_sort
import algorithms.selection_sort as selection_sort
import algorithms.insertion_sort as insertion_sort
import algorithms.quick_sort as quick_sort
import algorithms.merge_sort as merge_sort
import algorithms.heap_sort as head_sort
import datetime

if __name__ == '__main__':
    a = datetime.datetime.now()
    print(head_sort.default_array_sort())
    b = datetime.datetime.now()
    print(f'Difference is {b-a}')

