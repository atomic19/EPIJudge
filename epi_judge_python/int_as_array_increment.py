from typing import List

from test_framework import generic_test

def plus_one_inplace(A: List[int]) -> List[int]:
    carry = 1
    for idx in range(len(A)-1, -1, -1):
        sm = carry + A[idx]
        if sm >= 10:
            sm = sm - 10
            carry = 1
        else:
            carry = 0
        A[idx] = sm
    if carry != 0:
        A = [carry] + A
    return A

def plus_one(A: List[int]) -> List[int]:
    return plus_one_inplace(A)
    ot = []
    carry = 1
    for i in reversed(A):
        sm = i + carry
        if sm >= 10:
            carry = 1
            sm = sm - 10
        else:
            carry = 0
        ot.append(sm)
    if carry != 0:
        ot.append(carry)
    return list(reversed(ot))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
