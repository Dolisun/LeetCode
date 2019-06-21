class Solution(object):
    # 方法一使用zip函数
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        tmp = zip(*strs)
        ss = ''
        for item in tmp:
            if len(set(item)) == 1:
                ss += item[0]
            else:
                break
        return ss


class Solution(object):

    def longestCommonPrefix(self, strs):
        # write your code here
        if strs is None or len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            tmp = res
            res = ''
            for j in range(min(len(strs[i]), len(tmp))):
                if tmp[j] == strs[i][j]:
                    res += tmp[j]
                else:
                    break
        return res


if __name__ == '__main__':
    cls = Solution()
    print(cls.longestCommonPrefix(["flower","flow","flight"]))
