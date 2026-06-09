class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starting = set()
        lengths = set()
        if len(nums) == 0:
            return 0
        for num in nums:
            if num - 1 not in nums_set:
                starting.add(num)
        for x in starting:
            length = 1
            while x + 1 in nums_set:
                length += 1
                x += 1
            lengths.add(length)
        return max(lengths)