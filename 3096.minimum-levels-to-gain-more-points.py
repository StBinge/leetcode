#
# @lc app=leetcode.cn id=3096 lang=python3
# @lcpr version=30204
#
# [3096] 得到更多分数的最少关卡数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        pos=possible.count(1)
        neg=len(possible)-pos
        s=pos-neg
        ap=0
        for i in range(len(possible)-1):
            v=1 if possible[i]==1 else -1
            ap+=v
            s-=v
            if ap>s:
                return i+1
        return -1
# @lc code=end
assert Solution().minimumLevels([0,1,0])==2
assert Solution().minimumLevels([1,1])==-1
assert Solution().minimumLevels([0,0])==-1
assert Solution().minimumLevels([1,1,1,1,1])==3
assert Solution().minimumLevels([1,0,1,0])==1


#
# @lcpr case=start
# [1,0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

#

