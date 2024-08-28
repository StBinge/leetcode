#
# @lc app=leetcode.cn id=2109 lang=python3
# @lcpr version=30204
#
# [2109] 向字符串添加空格
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret=''
        pre=0
        for idx in spaces:
            ret+=s[pre:idx]
            ret+=' '
            pre=idx
        ret+=s[pre:]
        return ret
# @lc code=end



#
# @lcpr case=start
# "LeetcodeHelpsMeLearn"\n[8,13,15]\n
# @lcpr case=end

# @lcpr case=start
# "icodeinpython"\n[1,5,7,9]\n
# @lcpr case=end

# @lcpr case=start
# "spacing"\n[0,1,2,3,4,5,6]\n
# @lcpr case=end

#

