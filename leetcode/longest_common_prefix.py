class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        # take first element if not empty, later use for compare
        result = strs[0]
        for index in range(1, len(strs)):  # start from next element
            temp = ""
            if len(result) == 0:  # if first element empty quit
                break
            for index2 in range(len(strs[index])):
                if index2 < len(result):
                    if result[index2] == strs[index][index2]:
                        # same so append to temp var
                        temp += strs[index][index2]
                    else:
                        # not same so stop compare
                        break
                else:
                    break
            result = temp
        return result


input_list = ["school", "schedule", "scotland"]
ob1 = Solution()
print(ob1.longestCommonPrefix(input_list))
