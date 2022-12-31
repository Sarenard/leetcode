class Solution:
    def shortestPalindrome(self, s: str) -> str:
        new_str:str = s
        # we add characters in front of the string until it is a palindrome
        i = 1
        while not self.is_palin(new_str):
            new_char = s[i]
            new_str = new_char + new_str
            i += 1
        return new_str
        
    def is_palin(self, s:str) -> bool:
        return s == s[::-1]
    
print(Solution().shortestPalindrome("abcd"))