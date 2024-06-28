from sol import Solution

class Test:
    def run():
        solution = Solution()
        assert solution.largestNumber([10,2]) == "210"
        assert solution.largestNumber([3,30,34,5,9]) == "9534330"
        assert solution.largestNumber([432,43243]) == "43243432"

Test.run()
