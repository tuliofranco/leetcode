
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(word) for word in strs)

        if (min_length == 0):
            return ""

        if (len(strs) == 1):
            return strs[0]

        for i in range(min_length):
            caractere = strs[0][i]
            
            for j in range(1, len(strs)):
                if(caractere != strs[j][i]):
                    return strs[0][:i]
                
        return strs[0][:min_length]


