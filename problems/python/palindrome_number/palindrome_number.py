class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        if (x < 9):
            return True
        value = str(x)
        low, high = 0, len(value) - 1
        while (low < high):
            if (value[low] != value[high]):
                return False
            low += 1
            high -= 1
        return True
