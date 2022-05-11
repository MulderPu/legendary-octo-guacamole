class Solution:
    def isValid(self, s: str) -> bool:
        checkList = []
        openBracket = ["(", "[", "{"]
        closeBracket = [")", "]", "}"]
        pair = {')': '(', ']': '[', '}': '{'}

        for value in s:
            if value in openBracket:
                # add to check list
                checkList.append(value)
            if value in closeBracket:
                if not checkList:
                    # if empty check list, then no need check because no opening bracket
                    return False
                elif checkList.pop() != pair[value]:
                    # if check list last element not pair with closing, quit
                    return False
                else:
                    continue
        # check if check list still have unmatch brackets
        if not checkList:
            return True
        else:
            return False


s = "({})"
print(Solution().isValid(s))
