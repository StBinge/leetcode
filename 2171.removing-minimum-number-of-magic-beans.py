#
# @lc app=leetcode.cn id=2171 lang=python3
# @lcpr version=30204
#
# [2171] 拿出最少数目的魔法豆
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        s=sum(beans)
        cnt=len(beans)
        beans=Counter(beans)
        ret=float('inf')
        for k in sorted(beans.keys()):
            ret=min(ret,s-k*cnt)
            cnt-=beans[k]
        return ret

# @lc code=end
assert Solution().minimumRemoval([2,10,3,2])==7
assert Solution().minimumRemoval([4,1,6,5])==4


#
# @lcpr case=start
# [4,1,6,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,10,3,2]\n
# @lcpr case=end

#

