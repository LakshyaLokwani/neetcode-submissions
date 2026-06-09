class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cleaned_list = list(set(nums))
        if len(cleaned_list) == len(nums):
            return False
        else:
            return True
        