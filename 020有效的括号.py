# 方法1
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


# 方法2
class Solution:
    def isValid(self, s):
        stack = list(['1'])
        for st in s:
            if st in ['(', '[', '{']:
                stack.append(st)
            elif (stack[len(stack)-1]+st) not in ['()', '[]', '{}']:
                # stack.append(st)
                return False
            else:
                stack.pop()
        if stack == ['1']:
            return True
        else:
            return False

# #方法3
# class Solution:
#     def isValid(self, s):
#
#         matchStack = []  # 存放左开符号的栈
#         matchDist = {  # 存放符号对照表的字典
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }
#         for val in s:
#             # 左开符号不在符号对照表中，入栈
#             if val not in matchDist.keys():
#                 matchStack.append(val)
#
#             # 栈为空 or 栈尾元素和当前元素不匹配
#             elif not matchStack or matchDist[val] != matchStack.pop():
#                 return False
#
#         # 都匹配计算完毕后，栈不为空，表示有剩余未匹配到的。返回false
#         return not matchStack


if __name__ == '__main__':
    cls = Solution()
    print(cls.isValid(""))