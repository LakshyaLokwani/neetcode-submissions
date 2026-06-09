class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} 
        bucket_sort = {}
        answer = []
    
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        for num, count in frequency.items():
            if count in bucket_sort:
                bucket_sort[count].append(num)
            else:
                bucket_sort[count] = [num]
        
        for count in range(len(nums), 0, -1):
            if count not in bucket_sort:
                continue
            for _ in bucket_sort[count]:
                answer.append(_)
                if len(answer) == k:
                    return answer
        
        