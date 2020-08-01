from test_framework import generic_test


def power(x: float, y: int) -> float:
    result, power = x, 1
    if y == 0:
        return 1
    if y < 0:
        y, x, result = -y, 1.0 / x, 1.0/result
    while power + power <= y:
        power += power
        result *= result

    while power < y:
        power += 1
        result *= x
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
