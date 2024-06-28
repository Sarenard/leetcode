from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        assert solution.letterCombinations("") == []
        assert solution.letterCombinations("2") == ["a","b","c"]

Test.run()
