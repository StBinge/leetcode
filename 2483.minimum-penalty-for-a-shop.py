#
# @lc app=leetcode.cn id=2483 lang=python3
# @lcpr version=30204
#
# [2483] 商店的最少代价
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ret=0
        min_cost=cost=customers.count('y')
        for i,ch in enumerate(customers):
            if ch=='N':
                cost+=1
            else:
                cost-=1
            if cost<min_cost:
                min_cost=cost
                ret=i+1
        return ret
# @lc code=end



#
# @lcpr case=start
# "YYNY"\n
# @lcpr case=end

# @lcpr case=start
# "NNNNN"\n
# @lcpr case=end

# @lcpr case=start
# "YYYY"\n
# @lcpr case=end

#

