#
# @lc app=leetcode.cn id=2399 lang=python3
# @lcpr version=30204
#
# [2399] 检查相同字母间的距离
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i,ch in enumerate(s):
            code=ord(ch)-ord('a')
            if distance[code]>=0:
                distance[code]=-distance[code]-i-1
            elif distance[code]!=-i:
                return False


        return True
# @lc code=end
assert Solution().checkDistances("abaccb",[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
assert Solution().checkDistances("aa",[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])==False


#
# @lcpr case=start
# "abaccb"\n[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]\n
# @lcpr case=end

#

