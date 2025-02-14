#
# @lc app=leetcode.cn id=3386 lang=python3
# @lcpr version=30204
#
# [3386] 按下时间最长的按钮
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        mx_time=events[0][1]
        ret=events[0][0]

        for i in range(1,len(events)):
            dif=events[i][1]-events[i-1][1]
            if dif>mx_time:
                mx_time=dif
                ret=events[i][0]
            elif dif==mx_time:
                ret=min(ret,events[i][0])
        return ret
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,5],[3,9],[1,15]]\n
# @lcpr case=end

# @lcpr case=start
# [[10,5],[1,7]]\n
# @lcpr case=end

#

