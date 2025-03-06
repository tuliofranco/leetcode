class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        last_word = s[-1]
        return len(last_word)