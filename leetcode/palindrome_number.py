x = 131


def is_palindrome(x) -> bool:
    # check if negative then ignore
    if x >= 0:
        testDel = x
        result = 0
        while (testDel != 0):
            lastDigit = testDel % 10
            result = result * 10 + lastDigit

            # remove last digit
            testDel = int(testDel / 10)

        if result == x:
            return True
    else:
        return False


print(is_palindrome(x))
