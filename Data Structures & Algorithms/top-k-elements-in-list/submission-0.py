class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1
        
        sorted_list = sorted(list(frequency.items()), key= lambda item: item[1], reverse = True)
        
        res = []
        for pair in sorted_list[:k]:
            res.append(pair[0])
        return res


        