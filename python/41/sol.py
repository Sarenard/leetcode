from typing import List

# ne marche pas
# flemme de faire les edge cases
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        longueur = len(nums)
        if longueur == 1:
            return 2 if 1 in nums else 1 # edge case
        
        # on vire les nombres négatifs et les nombres trop gros
        end = longueur - 1
        start = 0
        noevent = True
        while start != end:
            bad = (lambda nb : nb <= 0 or nb > longueur)
            if bad(nums[start]):
                nums[start], nums[end] = nums[end], nums[start]
                noevent = False
                end -= 1
            else:
                start += 1
        if noevent:
            end += 1
        nouvelle_longueur = end # = len(nouvelle_liste)
        # on met à 0 tout les trucs mauvais
        for i in range(nouvelle_longueur, longueur):
            nums[i] = 0
            
        # on fais un premier pass et on modifie liste[liste[i]] quand on a le nb
        index = 0
        while index < nouvelle_longueur:
            elt = min(nums[index], nums[index] ^ (1 << longueur))
            if nums[elt-1] ^ (1 << longueur) > nums[elt-1]:
                nums[elt-1] ^= (1 << longueur)
            index += 1
            
        # on regarde en boucle qui a le flag présent
        index = 0
        while index != nouvelle_longueur - 1:
            if nums[index] > nums[index] ^ (1 << longueur):
                index += 1
            else:
                break
        
        if index == nouvelle_longueur - 1 and nouvelle_longueur == longueur:
            return index+1
        return index+1