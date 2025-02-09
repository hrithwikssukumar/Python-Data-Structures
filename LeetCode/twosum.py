from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num

            
            if complement in num_indices:
                
                return [num_indices[complement], i]

            
            num_indices[num] = i

        
        return []


solution = Solution()
result = solution.two_sum([2, 7, 11, 15], 9)
print(result)  
