from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    idx  = 0
    while idx < len(perm):
        if perm[idx] is not None:
            run = idx
            cur = A[run]
            while perm[run] is not None:
                nxt_cur = A[perm[run]]
                nxt_run = perm[run]

                A[perm[run]] = cur
                perm[run] = None

                run = nxt_run
                cur = nxt_cur
        idx += 1
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
