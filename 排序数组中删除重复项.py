class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0,0
        for k in nums[:-1]:
            i = i+1
            if nums[i]!=k:
                j = j+1
                nums[j]=nums[i]
        nums = nums[:j+1]
        return len(nums)