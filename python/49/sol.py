from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = []
        for mot in strs:
            dico = {a:0 for a in "abcdefghijklmnopqrstuvwxyz"}
            for lettre in mot:
                dico[lettre] += 1
            new_list.append((mot, dico))
        groupes = {}
        while new_list != []:
            liste = new_list.pop()
            tuples = tuple(list(liste[1].items()))
            try:
                groupes[tuples].append(liste[0])
            except Exception:
                groupes[tuples] = [liste[0]]
        return list(groupes.values())