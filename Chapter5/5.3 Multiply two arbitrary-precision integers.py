"""
Two numbers are represented in two arrays (lists in python)
A few things to note:
1. there is signs of the number to take care of
2. unnecessary 0's in front should be taken care of, e.g. [0,0,1,2] should be [1,2]
3. in order to save space, we can incrementally add the terms rather than compute all of them individually and add up
4. when multiplying two numbers with n digits and m digits, the max digits of the new number is n+m

The time complexity of the following algorithm is O(nm) with O(1) space complexity.
"""


def mul_two(x, y):
    # take care of the signs of the first number
    sign = -1 if (x[0] < 0) ^ (y[0] < 0) else 1
    x[0], y[0] = abs(x[0]), abs(y[0])

    # initialize an array for all the digits
    result = [0] * (len(x) + len(y))
    for i in reversed(range(len(x))):
        for j in reversed(range(len(y))):
            result[i + j + 1] += x[i] * y[j]
            result[i + j] += result[i + j + 1]//10
            result[i + j + 1] %= 10

    # removing 0's
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]

    # adding the sign
    return [sign*result[0]] + result[1:]
def main():
    assert mul_two([0], [1,2]) == [0]
    assert mul_two([1,3], [3]) == [3,9]

if __name__ == '__main__':
    main()
