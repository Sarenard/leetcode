import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
        # 1 <= n <= 100
        # The answer is guaranteed to fit in a 32-bit signed integer.
        # 1 <= n <= 100
        # The answer is guaranteed to fit in a 32-bit signed integer.
        def isPrime(n):
            if n == 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        primes = 0
        for i in range(1, n + 1):
            if isPrime(i):
                primes += 1
        return (math.factorial(primes) * math.factorial(n - primes)) % (10 ** 9 + 7)