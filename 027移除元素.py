class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        p = 0
        for item in nums:
            if item != val:
                nums[p] = item
                p += 1
        return p


# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         j=len(nums)
#         for i in range(j-1,-1,-1):
#             if nums[i]==val:
#                 nums.pop(i)
#                 print(nums)
#         return len(nums)
if __name__ == '__main__':
    cls = Solution()
    print(cls.removeElement([3,2,2,3], 3))