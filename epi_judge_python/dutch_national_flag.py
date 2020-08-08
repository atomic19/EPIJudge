import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def simple_dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    eq = []
    small = []
    large = []
    el = A[pivot_index]
    for i in A:
        if i == el:
            eq.append(i)
        elif i > el:
            large.append(i)
        else:
            small.append(i)
    ret = small + eq + large
    print('\n', A, ret)
    return ret


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    #return simple_dutch_flag_partition(pivot_index, A)
    pv = A[pivot_index]
    eq = pivot_index
    large = len(A) - 1
    run = 0
    while eq < large:
        if run == eq:
            eq += 1
            A[run], A[eq] = A[eq], A[run]
        elif A[run] == pv:
            eq += 1
            A[run], A[eq] = A[eq], A[run]
        elif A[run] > pv:
            A[large], A[run] = A[run], A[large]
            large -= 1
        else:
            run += 1
    return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
