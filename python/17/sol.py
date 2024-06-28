from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dico = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }
        ma_liste = []
        if not digits:
            return []
        if len(digits) == 1:
            return dico[digits]
        for letter in dico[digits[0]]:
            combi = self.letterCombinations(digits[1:])
            for x in combi:
                ma_liste.append(letter + x)
        return ma_liste