class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        best = 0
        

        for x in numbers:
            if x - 1 in numbers:
                continue 
            else:
                curr = x
                length = 1
                while curr + 1 in numbers:

                    curr += 1
                    length += 1
                best = max(best, length)
        return best
            
            
            


            

            
        