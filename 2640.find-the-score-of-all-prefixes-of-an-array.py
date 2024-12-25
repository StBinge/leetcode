#
# @lc app=leetcode.cn id=2640 lang=python3
# @lcpr version=30204
#
# [2640] 一个数组所有前缀的分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        s=0
        ret=[]
        mx=0
        for n in nums:
            mx=max(mx,n)
            s+=mx+n
            ret.append(s)
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,3,7,5,10]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,4,8,16]\n
# @lcpr case=end

#

