class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            x = nums[i]

            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        
            
        