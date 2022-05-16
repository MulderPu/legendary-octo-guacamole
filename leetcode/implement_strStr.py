class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        h_len = len(haystack)
        n_len = len(needle)
        if h_len == 0 or h_len < n_len:
            return -1
        while i < h_len:
            if haystack[i] == needle[j]:
                temp = i  # save temp first occurence
                while j < n_len and i < h_len and needle[j] == haystack[i]:
                    i += 1
                    j += 1
                if j == n_len:
                    return temp

                # continue loop, reset j
                i = temp+1
                j = 0
            else:
                i += 1
        return -1


haystack = "hello"
needle = "ll"

print(Solution().strStr(haystack, needle))
