"""
In this Kata, you will be given boolean values and boolean operators.
Your task will be to return the number of arrangements that evaluate to True.

t,f will stand for true,
false and the operators will be Boolean AND (&), OR (|), and XOR (^).

For example, solve("tft","^&") = 2, as follows:

"((t ^ f) & t)" = True
"(t ^ (f & t))" = True
Notice that the order of the boolean values
and operators does not change.
 What changes is the position of braces.

More examples in the test cases.

Good luck!



Test.it("Basic tests")
Test.assert_equals(solve("tft","^&"),2)
Test.assert_equals(solve("ttftff","|&^&&"),16)
Test.assert_equals(solve("ttftfftf","|&^&&||"),339)
Test.assert_equals(solve("ttftfftft","|&^&&||^"),851)
Test.assert_equals(solve("ttftfftftf","|&^&&||^&"),2434)
"""


def solve(s, ops):
    replaced_c = s.replace("t", True)
    print(replaced_c)


def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False


def OR(a, b):
    if a == 1:
        return True
    elif b == 1:
        return True
    else:
        return False


def XOR(a, b):
    if a != b:
        return 1
    else:
        return 0


#solve("tft", "^&")



def this_is_an_example (*aqrgs, **kwargs) :

    print(aqrgs)
    print(**kwargs)

this = {1:"denis"}
this_is_an_example(5,7,this)

