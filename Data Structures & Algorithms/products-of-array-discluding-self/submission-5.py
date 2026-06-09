class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        lvar = 1
        for i in range(len(nums)):
            left.append(lvar)
            lvar *= nums[i]
        
        right = []
        rvar = 1
        for x in range(len(nums) - 1, -1, -1):
            right.append(rvar)
            rvar *= nums[x]
        right = right[::-1]
        
        answer = []
        for i in range(len(nums)):
            answer.append(right[i]*left[i])
        return answer 
        