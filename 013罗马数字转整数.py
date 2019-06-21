class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        para = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        left_para = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        num = 0
        while len(s) > 0:
            if s[:2] in left_para.keys():
                num += left_para[s[:2]]
                s = s[2:]
            else:
                num += para[s[0]]
                s = s[1:]
        return num

if __name__ == '__main__':
    so = Solution()
    print(so.romanToInt("XCD"))