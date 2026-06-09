class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        
        
        for word in strs:
            count = [0] * 26
            for i in word:
                count[ord(i) - ord("a")] += 1
            structure = tuple(count)
            if structure in dictionary:
                dictionary[structure].append(word)
            else:
                dictionary[structure] = [word]
        return list(dictionary.values())

        

        