class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        step = k % len(nums)
        if k == 0:
            nums = nums
            return None
        else:
            if len(nums)==1 or len(nums)==0:
                nums = nums
                return None
            else:
                nums[:] = nums[-step:]+nums[:-step]
                return None