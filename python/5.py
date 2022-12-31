class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Given a string s, return the longest palindromic substring in s.
        # we need to find the longest palindrome
        # we need to return the longest palindrome
        # we need to use a sliding window
        # we need to check if the window is a palindrome
        # we need to update the max length
        # we need to update the max palindrome
        # we need to return the max palindrome
        max_length:int = 0
        max_palindrome:str = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j+1]) and j - i + 1 > max_length:
                    max_length = j - i + 1
                    max_palindrome = s[i:j+1]
        return max_palindrome
    
    def is_palindrome(self, s:str) -> bool:
        # we need to check if the string is a palindrome
        # we need to return True if it is, False otherwise
        return s == s[::-1]
    
# TODO : optimise this solution to pass the time limit