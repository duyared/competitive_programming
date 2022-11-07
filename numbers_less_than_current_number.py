class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counterArray = []
        for i in nums:
            counter =0
            for j in nums:
                if j!=i and j< i:
                    counter += 1
            counterArray.append(counter)
        return counterArray
                
        
