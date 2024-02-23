"Stephon Kumar"
"sort_compare.py"

import argparse
import random
import time


def get_me_random_list(n):
    
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    return time.time() - start_time


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def shell_sort(a_list):
    start_time = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    return time.time() - start_time


def python_sort(a_list):
    start_time = time.time()
    sorted_list = sorted(a_list)
    return time.time() - start_time


def main():
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        total_time_python_sort = 0
        total_time_insertion_sort = 0
        total_time_shell_sort = 0

        for i in range(100):
            my_list = get_me_random_list(the_size)

            # Python Sort
            time_python_sort = python_sort(my_list.copy())
            total_time_python_sort += time_python_sort

            # Insertion Sort
            time_insertion_sort = insertion_sort(my_list.copy())
            total_time_insertion_sort += time_insertion_sort

            # Shell Sort
            time_shell_sort = shell_sort(my_list.copy())
            total_time_shell_sort += time_shell_sort

        avg_time_python_sort = total_time_python_sort / 100
        avg_time_insertion_sort = total_time_insertion_sort / 100
        avg_time_shell_sort = total_time_shell_sort / 100

        print(f"For list size {the_size}:")
        print(f"Python's Sort took {avg_time_python_sort:.7f} seconds to run, on average")
        print(f"Insertion Sort took {avg_time_insertion_sort:.7f} seconds to run, on average")
        print(f"Shell Sort took {avg_time_shell_sort:.7f} seconds to run, on average")
        print()


if __name__ == "__main__":
    main()
