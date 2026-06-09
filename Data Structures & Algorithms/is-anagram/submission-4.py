class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}
        counter_t = {}
        for letter in s:
            if letter in counter_s:
                counter_s[letter] += 1
            else:
                counter_s[letter] = 1 
        
        for letter in t:
            if letter in counter_t:
                counter_t[letter] += 1
            else:
                counter_t[letter] = 1 

        if counter_s == counter_t:
            return True
        else: 
            return False