class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        import bisect
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
                continue
            elif numbers[l] + numbers[r] < target:
                l += 1
                continue
            else:
                break
        return [l+1, r+1]

    