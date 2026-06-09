class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_dict = {}

        for i in range(len(nums)):
            if nums[i] in difference_dict:
                return [difference_dict[nums[i]], i]
            difference = target - nums[i]
            difference_dict[difference] = i
        
        