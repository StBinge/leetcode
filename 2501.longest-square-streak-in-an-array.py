#
# @lc app=leetcode.cn id=2501 lang=python3
# @lcpr version=30204
#
# [2501] 数组中最长的方波
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s=set(nums)
        sorted_s=sorted(s)
        ret=-1
        for x in sorted_s:
            cnt=0
            while x in s:
                s.remove(x)
                x*=x
                cnt+=1
            if cnt>1:
                ret=max(ret,cnt)
        return ret


# @lc code=end



#
# @lcpr case=start
# [4,3,6,16,8,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,6,7]\n
# @lcpr case=end

#

