#方法一，暴力搜索
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i+1
#方法二, 二分查找
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

if __name__ == '__main__':
    cls = Solution()
    print(cls.searchInsert([1,3], 4))