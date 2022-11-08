class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numOfpairs = 0
        left , right = 0,len(nums)-1
        nums = sorted(nums)
        while(left < right):
            answer = nums[right] + nums[left]
            if answer > k:
                right -= 1    
            elif answer < k:
                left += 1
            else:
                right -= 1
                left += 1
                numOfpairs += 1
        return numOfpairs;
                    
        
