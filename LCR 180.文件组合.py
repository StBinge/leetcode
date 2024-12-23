#
# @lc app=leetcode.cn id=LCR 180 lang=python3
# @lcpr version=30204
#
# [LCR 180] 文件组合
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        ret=[]
        l,r=1,2
        while r<=target//2+1:
            s=(l+r)*(r-l+1)//2
            if s==target:
                ret.append(list(range(l,r+1)))
                l+=1
            elif s<target:
                r+=1
            else:
                l+=1
        return ret
# @lc code=end
assert sorted(Solution().fileCombination(10))==[[1,2,3,4]]
assert sorted(Solution().fileCombination(18))==sorted([[3,4,5,6],[5,6,7]])
assert Solution().fileCombination(12)==[[3,4,5]]


#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 18\n
# @lcpr case=end

#

