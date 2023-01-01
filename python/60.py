class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1. Create a list of numbers from 1 to n.
        # 2. Create a list of factorials from 0! to (n-1)!.
        # 3. Subtract 1 from k.
        # 4. Create an empty string.
        # 5. Loop from n-1 to 0.
        # 6. Find the index of the current number in the list of numbers.
        # 7. Append the current number to the string.
        # 8. Remove the current number from the list of numbers.
        # 9. Divide k by the factorial of the current index.
        # 10. Set k to the remainder.
        # 11. Return the string.
        nums:list = [i for i in range(1, n+1)]
        factorials:list = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * i)
        k -= 1
        result:str = ''
        for i in range(n-1, -1, -1):
            index:int = k // factorials[i]
            result += str(nums[index])
            nums.pop(index)
            k %= factorials[i]
        return result