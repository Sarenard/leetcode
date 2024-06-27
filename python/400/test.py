from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.findNthDigit(3) == 3
        assert solution.findNthDigit(10) == 1
        assert solution.findNthDigit(11) == 0
        assert solution.findNthDigit(12) == 1
        assert solution.findNthDigit(13) == 1
        assert solution.findNthDigit(14) == 1
        assert solution.findNthDigit(15) == 2
        assert solution.findNthDigit(1000000) == 1
        assert solution.findNthDigit(1000001) == 8

Test.run()
