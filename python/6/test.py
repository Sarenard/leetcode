from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
        assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

Test.run()
