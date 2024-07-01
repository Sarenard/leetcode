from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # sourcery skip: dict-comprehension
        importance = {x: 0 for x in range(n)}
        for road in roads:
            importance[road[0]] += 1
            importance[road[1]] += 1
        maliste = list(importance.items())
        maliste.sort(key = lambda x : x[1], reverse = True)
        valeurs = {}
        for i, item in enumerate(maliste):
            valeurs[item[0]] = n-i
        total = 0
        for road in roads:
            total += valeurs[road[0]]
            total += valeurs[road[1]]
        return total