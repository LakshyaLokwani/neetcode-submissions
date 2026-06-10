class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency = {}
        answer = []
        for string in strs:
            count = [0] * 26
            for i in string:
                count[ord(i) - ord("a")] += 1
            count = tuple(count)
            if count in frequency:
                frequency[count].append(string)
            else:
                frequency[count] = [string]
        
        for count, freq in frequency.items():
            answer.append(frequency[count])
        return answer
        
