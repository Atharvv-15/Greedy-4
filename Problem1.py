# Problem 2: Minimum Domino Rotations For Equal Row
from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def search(tops,bottoms,target):
            tRot, bRot = 0,0
            for i in range(len(tops)):
                if target != tops[i] and target != bottoms[i] : return -1
                if target != tops[i] : tRot += 1
                elif target != bottoms[i] : bRot += 1
            return min(tRot,bRot)
        k = search(tops,bottoms,tops[0])
        if k != -1:return k
        else: return search(tops,bottoms,bottoms[0])
        

        
        