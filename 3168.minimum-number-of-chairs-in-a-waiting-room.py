#
# @lc app=leetcode.cn id=3168 lang=python3
# @lcpr version=30204
#
# [3168] 候诊室中的最少椅子数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumChairs(self, s: str) -> int:
        cur=mx=0
        for ch in s:
            if ch=='E':
                cur+=1
                mx=max(mx,cur)
            else:
                cur-=1
        return mx
# @lc code=end



#
# @lcpr case=start
# "EEEEEEE"\n
# @lcpr case=end

# @lcpr case=start
# "ELELEEL"\n
# @lcpr case=end

# @lcpr case=start
# "ELEELEELLL"\n
# @lcpr case=end

#

