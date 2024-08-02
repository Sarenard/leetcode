from sol import Solution

class Test:
    def run():
        solution = Solution()
        
        sol = [1,2,3,4,5,6,7]
        solution.rotate(sol, 3)
        assert sol == [5,6,7,1,2,3,4]
        
        sol = [-1,-100,3,99]
        solution.rotate(sol, 2)
        assert sol == [3,99,-1,-100]

Test.run()
