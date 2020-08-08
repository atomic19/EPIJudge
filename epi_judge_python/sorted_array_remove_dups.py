import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    i = 0
    first_non = None
    while i + 1 < len(A):
        if A[i] == A[i+1]:
            A[i] = 'X'
            if first_non is None:
                first_non = i
        i += 1
    if first_non is not None:
        i = first_non
        next_num = i + 1
        while next_num < len(A):
            if A[next_num] != 'X':
                A[i], A[next_num] = A[next_num], A[i]
                i, next_num = i+1, next_num + 1
            else:
                next_num += 1
        return i
    else:
        return len(A)

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
