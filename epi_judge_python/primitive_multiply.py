from test_framework import generic_test


def add_bits(a, b, c):
    if a and b and not c: # 1
        return 0, 1
    elif a and b and c: # 2
        return 1, 1
    elif a and not b and not c:  # 3
        return 1, 0
    elif a and not b and c: # 4
        return 0, 1
    elif not a and b and not c:
        return 1, 0
    elif not a and b and c:
        return 0, 1
    elif not a and not b and not c:
        return 0, 0
    elif not a and not b and c:
        return 1, 0


def add_nums(n1, n2):
    run_sum, carry, ctr, cur_sum = 0, 0, 0, 0
    while n1 != 0 and n2 != 0:
        b1, b2 = n1 & 1, n2 & 1
        n1, n2 = n1 >> 1, n2 >> 1

        cur_sum, carry = add_bits(b1, b2, carry)

        run_sum = run_sum | (cur_sum << ctr)
        ctr += 1
    if n1 == 0 and n2 == 0 and carry == 0:
        return run_sum
    elif n2 != 0:
        n1, n2 = n2, n1

    # here n1 will not be 0
    if carry == 0:
        return run_sum | n1 << ctr
    else:
        remain = add_nums(n1, carry)
        return run_sum | remain << ctr


def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    run = 0
    while x != 0:
        if x & 1:
            run = add_nums(run, y)
        x, y = x >> 1, y << 1

    return run

def check_add(n1, n2):
    v = add_nums(n1, n2)
    print(n1, bin(n2), n1, bin(n2), 'added: ', v, bin(v))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
