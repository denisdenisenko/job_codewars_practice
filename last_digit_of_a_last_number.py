"""
Define a function that takes in two non-negative integers
 aaa and bbb and returns the last decimal digit of aba^ba
b
 . Note that aaa and bbb may be very large!

For example, the last decimal digit of 979^79
7
  is 999, since 97=47829699^7 = 47829699
7
 =4782969. The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2
200
 )
2
300

 , which has over 109210^{92}10
92
  decimal digits, is 666. Also, please take 000^00
0
  to be 111.

You may assume that the input will always be valid.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
Remarks
JavaScript, C++, R, PureScript
Since these languages don't have native arbitrarily large integers,
 your arguments are going to be strings representing non-negative integers instead.


"""

"""
Test.it("Example tests")
Test.assert_equals(last_digit(4, 1), 4)
Test.assert_equals(last_digit(4, 2), 6)
Test.assert_equals(last_digit(9, 7), 9)
Test.assert_equals(last_digit(10, 10 ** 10), 0)
Test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
Test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

Test.it("x ** 0")
for nmbr in range(1, 9):
    a = nmbr ** nmbr
    Test.it("Testing %d and %d" % (a, 0))
    Test.assert_equals(last_digit(a, 0), 1, "x ** 0 must return 1")

"""


def last_digit(n1, n2):
    x = n1**n2
    x = int(str(x)[-1])
    print(x)
    return


last_digit(10, 10 ** 10)