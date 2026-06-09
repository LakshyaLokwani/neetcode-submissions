class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1

        for _ in t:
            countT[_] = countT.get(_, 0) + 1

        return countS == countT



        
        