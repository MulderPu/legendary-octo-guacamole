class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list = s.rstrip().split(" ")
        return len(list.pop())


# s = "Hello World"
s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))
