"""
# Instructions
The Collatz Conjecture or 3x+1 problem can be summarized as follows:

Take any positive integer n. If n is even, divide n by 2 to get n / 2.
If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process
indefinitely. The conjecture states that no matter which number you
start with, you will always reach 1 eventually.

Given a number n, return the number of steps required to reach 1.

# Examples

Starting with n = 12, the steps would be as follows:

1. 12
2. 6
3. 3
4. 10
5. 5
6. 16
7. 8
8. 4
9. 2
10. 1
"""


def steps(number: int) -> int:
    """Calculates the steps for a sequence of changes in the number.
    :param number: int - Number for a sequence of changes.
    :return: int - Number of changes steps.
    """
    if not number > 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number > 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1 
        steps += 1
    return steps
