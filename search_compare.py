#Stephon Kumar

import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

# Implement sequential search, ordered sequential search, binary search iterative and recursive
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

# Benchmarking function for a specific search algorithm
def benchmark_search(search_func, search_name, list_size):
    total_time = 0
    for i in range(100):
        mylist = get_me_random_list(list_size)
        mylist = sorted(mylist)  # Sorting for ordered and binary searches

        start = time.time()
        search_func(mylist, 99999999)  # Non-existent element for worst-case scenario
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"{search_name} took {avg_time:10.7f} seconds to run, on average for a list of {list_size} elements")

if __name__ == "__main__":
    """Main entry point"""
    sizes = [500, 1000, 5000]

    # Run each search for each list size
    for size in sizes:
        print(f"\nBenchmarking for list size: {size}")

        # Sequential Search
        benchmark_search(sequential_search, "Sequential Search", size)

        # Ordered Sequential Search
        benchmark_search(ordered_sequential_search, "Ordered Sequential Search", size)

        # Binary Search Iterative
        benchmark_search(binary_search_iterative, "Binary Search Iterative", size)

        # Binary Search Recursive
        benchmark_search(binary_search_recursive, "Binary Search Recursive", size)
