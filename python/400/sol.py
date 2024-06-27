from typing import List

class Solution:
    def findNthDigit(self, n: int) -> int:
        liste = [9]
        def add(liste):
            nb = len(liste) + 1 # la longueur des nombres à ajouter
            # combien de nombres à nb chiffres ?
            total = 9 * 10 ** (nb-1) * nb + liste[-1]
            liste.append(total)
        while liste[-1] < n:
            add(liste)
        liste.pop()
        if n < 10:
            return n
        offset = n - liste[-1] - 1 # how many characters after 10**liste3[-1]
        # we need to find the number we are in
        number_in = offset // (len(liste)+1)
        rest = offset % (len(liste)+1)
        real_number_in = number_in + 10 ** (len(liste))
        return int(str(real_number_in)[rest])