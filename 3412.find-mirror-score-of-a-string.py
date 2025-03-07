#
# @lc app=leetcode.cn id=3412 lang=python3
# @lcpr version=30204
#
# [3412] 计算字符串的镜像分数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def calculateScore(self, s: str) -> int:
        indices=[[] for _ in range(26)]
        ret=0
        for i,ch in enumerate(s):
            code=ord(ch)-97
            _code=25-code
            if indices[_code]:
                ret+=i-indices[_code].pop()
            else:
                indices[code].append(i)
        return ret
# @lc code=end
assert Solution().calculateScore('abcdef')==0
assert Solution().calculateScore('aczzx')==5


#
# @lcpr case=start
# "aczzx"\n
# @lcpr case=end

# @lcpr case=start
# "abcdef"\n
# @lcpr case=end

#

