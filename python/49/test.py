from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['nat', 'tan'], ['ate', 'tea', 'eat']]
        assert solution.groupAnagrams([""]) == [[""]]
        assert solution.groupAnagrams(["a"]) == [["a"]]

Test.run()
