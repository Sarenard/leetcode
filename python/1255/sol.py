from typing import List
from string import ascii_lowercase

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def calcul_score(word):
            # first we calculate the score
            total = 0
            for letter in word:
                letter_score = score[ord(letter)-ord("a")]
                total += letter_score
            return total
        scores = {word:calcul_score(word) for word in words}
        present = {x:0 for x in ascii_lowercase}
        for letter in letters:
            present[letter] += 1
        
        def compare(dict1, dict2):
            return all(dict1[x] <= dict2[x] for x in ascii_lowercase)
        
        best_score = 0
        for i in range(2**len(words)):
            binary = format(i, f'0{len(words)}b')
            liste_mots = []
            for index, mot in enumerate(words):
                if binary[index] == "1":
                    liste_mots.append(mot)
            current_present = {x:0 for x in ascii_lowercase}
            for mot in liste_mots:
                for letter in mot:
                    current_present[letter] += 1
            if compare(current_present, present):
                new_score = 0
                for mot in liste_mots:
                    new_score += scores[mot]
                best_score = max(new_score, best_score)
        
        return best_score