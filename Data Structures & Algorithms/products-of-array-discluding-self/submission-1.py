class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        zero_index = -1
        prod_nonzero = 1
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                zero_index = i
            else:
                prod_nonzero *= nums[i]
        
        out = {}
        if zero_count >= 2:
            for i in range(n):
                out[i] = 0
        elif zero_count == 1:
            for i in range(n):
                if nums[i] != 0:
                    out[i] = 0
                else:
                    out[i] = prod_nonzero
        elif zero_count == 0:
            for i in range(n):
                out[i] = prod_nonzero // nums[i]
        return list(out.values())
        