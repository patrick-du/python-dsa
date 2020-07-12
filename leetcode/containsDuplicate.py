class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    def naiveBruteForceSolution(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False

    def dictionarySolution(self, nums):
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1
