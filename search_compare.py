"Stephon Kumar"
"search_compare.py"

import time
import random


def get_me_random_list(n):

    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def main():
    the_size = 500
    num_iterations = 100

    total_time_seq = 0
    total_time_ordered_seq = 0
    total_time_binary_iter = 0
    total_time_binary_rec = 0

    for _ in range(num_iterations):
        mylist = get_me_random_list(the_size)
        # Sorting is not needed for sequential search.
        mylist = sorted(mylist)

        # Sequential Search
        start_time_seq = time.time()
        check_seq = sequential_search(mylist, 99999999)
        time_spent_seq = time.time() - start_time_seq
        total_time_seq += time_spent_seq

        # Ordered Sequential Search
        start_time_ordered_seq = time.time()
        check_ordered_seq = ordered_sequential_search(mylist, 99999999)
        time_spent_ordered_seq = time.time() - start_time_ordered_seq
        total_time_ordered_seq += time_spent_ordered_seq

        # Binary Search Iterative
        start_time_binary_iter = time.time()
        check_binary_iter = binary_search_iterative(mylist, 99999999)
        time_spent_binary_iter = time.time() - start_time_binary_iter
        total_time_binary_iter += time_spent_binary_iter

        # Binary Search Recursive
        start_time_binary_rec = time.time()
        check_binary_rec = binary_search_recursive(mylist, 99999999)
        time_spent_binary_rec = time.time() - start_time_binary_rec
        total_time_binary_rec += time_spent_binary_rec

    avg_time_seq = total_time_seq / num_iterations
    avg_time_ordered_seq = total_time_ordered_seq / num_iterations
    avg_time_binary_iter = total_time_binary_iter / num_iterations
    avg_time_binary_rec = total_time_binary_rec / num_iterations

    print(f"Sequential Search took {avg_time_seq:10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Ordered Sequential Search took {avg_time_ordered_seq:10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Binary Search Iterative took {avg_time_binary_iter:10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Binary Search Recursive took {avg_time_binary_rec:10.7f} seconds to run, on average for a list of {the_size} elements")


if __name__ == "__main__":
    main()
