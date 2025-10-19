class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = [i for i in s if i.isalpha() == True]
        s = " ".join(s)
        return s == s[::-1]