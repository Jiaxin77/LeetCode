class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype=[]
        for i in range(0,len(nums)) :
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target :
                
                    rtype.append(i)
                    rtype.append(j)
                    return rtype
                
            
    
        return rtype
        
