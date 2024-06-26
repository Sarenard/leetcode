from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.isValid("()") == True
        assert solution.isValid(r"()[]{}") == True
        assert solution.isValid("(]") == False
        assert solution.isValid("[") == False

Test.run()
