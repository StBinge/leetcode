#
# @lc app=leetcode.cn id=2404 lang=python3
# @lcpr version=30204
#
# [2404] 出现最频繁的偶数元素
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt=Counter([n for n in nums if n&1==0])
        ret=-1
        mx=0
        for k,v in cnt.items():
            if v>mx:
                mx=v
                ret=k
            elif v==mx:
                ret=min(ret,k)
        return ret
# @lc code=end



#
# @lcpr case=start
# [0,1,2,2,4,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,4,9,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [29,47,21,41,13,37,25,7]\n
# @lcpr case=end

#

