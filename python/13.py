class Solution:
    def romanToInt(self, s: str) -> int:
        total:int = 0
        data_dict:dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i > 0 and data_dict[s[i]] > data_dict[s[i-1]]:
                total += data_dict[s[i]] - 2 * data_dict[s[i-1]]
            else:
                total += data_dict[s[i]]
        return total