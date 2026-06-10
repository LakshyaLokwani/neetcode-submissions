class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        answer = []
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for key, value in frequency.items():
            bucket[value].append(key)

        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                answer.append(num)

                if len(answer) == k:
                    return answer
            
            
