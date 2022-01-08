from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = list(range(0,n))
                                    
        for i in l:
            if i not in nums:
                print(i)

nums = [9,6,4,2,3,5,7,0,1]
#nums = [3,0,1]
obj = Solution()
obj.missingNumber(nums)
