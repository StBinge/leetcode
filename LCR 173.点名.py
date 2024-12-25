#
# @lc app=leetcode.cn id=LCR 173 lang=python3
# @lcpr version=30204
#
# [LCR 173] 点名
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        left,right=0,len(records)-1
        while left<right:
            mid=(left+right)>>1
            if records[mid]==mid:
                left=mid+1
            else:
                right=mid
        return left if records[left]!=left else len(records)
# @lc code=end



#
# @lcpr case=start
# [0,1,2,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [0, 1, 2, 3, 4, 5, 6, 8]\n
# @lcpr case=end

#

