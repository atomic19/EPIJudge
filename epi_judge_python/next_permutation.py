from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    r_till = None
    for i in range(0, len(perm) - 1):
        if perm[i] < perm[i + 1]:
            r_till = i

    print('\n', perm, 'r_till', r_till)

    def find_and_sawp(idx, arr):
        vl = arr[idx]
        mn, found = None, None
        for i in range(idx + 1, len(arr)):
            if arr[i] > vl:
                if mn is None or mn >= arr[i]:
                    found, mn = i, arr[i]
        if found:
            arr[found], arr[idx] = arr[idx], arr[found]
            arr[idx + 1:] = list(sorted(arr[idx + 1:]))
            return True
        return False

    if r_till is None or r_till + 1 == len(perm) - 1:
        if r_till is None:
            return []
        if perm[r_till] >= perm[r_till + 1]:
            # return list(reversed(perm))
            return []
        else:
            perm[r_till], perm[r_till + 1] = perm[r_till + 1], perm[r_till]
            return perm
    else:
        if find_and_sawp(r_till + 1, perm):
            return perm
        else:
            find_and_sawp(r_till, perm)
            return perm


# print([3,2,1], next_permutation([3,2,1]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
