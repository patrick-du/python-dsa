class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementMap=dict()
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i
                
    
    def bruteForceTwoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, (len(nums))):
                sum = nums[i] + nums[j]
                if target == sum:
                    return [i, j]
        
        
        