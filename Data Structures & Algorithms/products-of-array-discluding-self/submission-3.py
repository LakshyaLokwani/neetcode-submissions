class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                continue 

        if count >= 2:
            return [0] * len(nums)

        solution = []

        if count == 1:
            total1 = 1
            for num in nums:
                if num == 0:
                    continue
                total1 *= num 
            for num in nums:
                if num == 0:
                    solution.append(total1)
                else:
                    solution.append(0)
        if count == 0:
            total0 = 1
            for num in nums:
                total0 *= num
            for num in nums:
                solution.append(total0 // num)
        
        return solution