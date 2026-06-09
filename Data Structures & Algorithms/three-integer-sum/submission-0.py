class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        n = len(nums)
        list_of_lists = []
        for i in range(n):
            if i > 0 and sorted_list[i] == sorted_list[i-1]:
                continue 
            j = i + 1
            k = n - 1
            if i != j and i != k:
                while j < k:
                    if sorted_list[j] + sorted_list[k] > -(sorted_list[i]):
                        k -= 1
                    elif sorted_list[j] + sorted_list[k] < -(sorted_list[i]):
                        j += 1
                    else:
                        list_of_lists.append([sorted_list[i], sorted_list[j], sorted_list[k]])
                        j += 1
                        k -= 1

                        while j < k and sorted_list[j] == sorted_list[j - 1]:
                            j +=1
                        while j < k and sorted_list[k] == sorted_list[k + 1]:
                            k -= 1
        return list_of_lists
                        
                 



        
        
                    




        


        