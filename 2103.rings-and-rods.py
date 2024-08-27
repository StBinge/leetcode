#
# @lc app=leetcode.cn id=2103 lang=python3
# @lcpr version=30204
#
# [2103] 环和杆
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        mask=[0]*10
        for i in range(0,len(rings),2):
            color=rings[i]
            idx=int(rings[i+1])
            bit='RGB'.index(color)
            mask[idx]|=1<<bit
        return sum(m==0b111 for m in mask)
# @lc code=end



#
# @lcpr case=start
# "B0B6G0R6R0R6G9"\n
# @lcpr case=end

# @lcpr case=start
# "B0R0G0R9R0B0G0"\n
# @lcpr case=end

# @lcpr case=start
# "G4"\n
# @lcpr case=end

#

