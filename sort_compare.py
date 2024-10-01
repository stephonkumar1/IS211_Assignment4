#Stephon Kumar
import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    """Use Python built-in sorted function"""
    return sorted(a_list)


def benchmark_sort(sort_func, sort_name, list_size):
    total_time = 0
    for i in range(100):
        mylist = get_me_random_list(list_size)

        start = time.time()
        sort_func(mylist)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"{sort_name} took {avg_time:10.7f} seconds to run, on average for a list of {list_size} elements")


if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        print(f"\nBenchmarking for list size: {the_size}")

        # Python's built-in sort
        benchmark_sort(python_sort, "Python Sort", the_size)

        # Insertion Sort
        benchmark_sort(insertion_sort, "Insertion Sort", the_size)

        # Shell Sort
        benchmark_sort(shell_sort, "Shell Sort", the_size)
