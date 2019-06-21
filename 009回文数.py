# 方法一
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        return True if x_str == x_str[::-1] else False

# 方法二
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        while x > y:
            y = 10 * y + x % 10
            x = x // 10
            # print('x:{},y:{}'.format(x, y))
        return x == y or x == y // 10



if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(0))