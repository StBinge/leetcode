#
# @lc app=leetcode.cn id=2937 lang=python3
# @lcpr version=30204
#
# [2937] 使三个字符串相等
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lcp=0
        for x,y,z in zip(s1,s2,s3):
            if (x==y==z):
                lcp+=1
            else:
                break
        return -1 if lcp==0 else len(s1)+len(s2)+len(s3)-3*lcp
# @lc code=end
assert Solution().findMinimumOperations(s1 = "abc",s2 = "abb",s3 = "ab")==2


#
# @lcpr case=start
# "ab"\n
# @lcpr case=end

# @lcpr case=start
# "cac"\n
# @lcpr case=end

#

