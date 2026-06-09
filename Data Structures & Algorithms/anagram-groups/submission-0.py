class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string create a tuple which contains the count of all
        # letters from a-z. then create that as a key. then for each tuple
        # make the value of the tuple as the strings that match that value.

        groups = {}

        for word in strs:
            count = [0] * 26
            
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            if key not in groups:
                groups[key] = []

            groups[key].append(word)
         
        return list(groups.values())

    
