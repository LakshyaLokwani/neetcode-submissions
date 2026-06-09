class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1

        n = len(nums)

        buckets = [[] for _ in range(n+1)]

        for num, c in frequency.items():
            buckets[c].append(num)
        
        res = []

        for c in range(n, 0, -1):
            for num in buckets[c]:
                res.append(num)
                if len(res) == k:
                    return res
        

            