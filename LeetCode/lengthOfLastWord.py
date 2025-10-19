class Solution(object):
    def lengthOfLastWord(self, s):
        st = s.split(" ")
        st = [s for s in st if len(s) != 0]
        l = len(st[-1])
        return l
        