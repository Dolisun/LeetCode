class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mylen = len(nums)
        if mylen <= 1:
            return mylen
        p = 0
        for tem in nums:
            if nums[p] != tem:
                nums[p + 1] = tem
                p += 1
        return p + 1


if __name__ == '__main__':
    cls = Solution()
    print(cls.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))