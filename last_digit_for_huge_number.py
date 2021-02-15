"""
For a given list [x1, x2, x3, ..., xn] compute the last (decimal)
digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

E. g.,

last_digit([3, 4, 2]) == 1
because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast.
For example, 9 ^ (9 ^ 9) has more than 369 millions of digits.
lastDigit has to deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.

This kata generalizes Last digit of a large number;
you may find useful to solve it beforehand.

"""

"""
test.it('Basic tests')
test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]
for test_input, test_output in test_data:
    test.assert_equals(last_digit(test_input), test_output)
    
"""


def last_digit(lst):
    sum = 1
    if len(lst) == 0:
        return sum
    return (lst[0] ** lst_digit_help(0, lst[0:]))
    pass


def lst_digit_help(index, lst):
    if len(lst) == 1:
        return lst[0]
    index += 1
    return lst[0] ** lst_digit_help(index, lst[1:])


last_digit([7, 6, 21])
