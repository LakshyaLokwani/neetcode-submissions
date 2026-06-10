class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        answer = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for i in range(len(nums), -1, -1):
            for key, value in frequency.items():
                if len(answer) == k:
                    return answer
                if i == value:
                    answer.append(key)                

