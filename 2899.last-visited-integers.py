#
# @lc app=leetcode.cn id=2899 lang=python3
# @lcpr version=30204
#
# [2899] 上一个遍历的整数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen=[]
        k=0
        ret=[]
        for n in nums:
            if n!=-1:
                seen.append(n)
                k=0
            else:
                k+=1
                if k<=len(seen):
                    ret.append(seen[-k])
                else:
                    ret.append(-1)
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,-1,-1,-1]\n
# @lcpr case=end

# @lcpr case=start
# [1,-1,2,-1,-1]\n
# @lcpr case=end

#

