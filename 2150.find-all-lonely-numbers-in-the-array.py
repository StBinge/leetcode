#
# @lc app=leetcode.cn id=2150 lang=python3
# @lcpr version=30204
#
# [2150] 找出数组中的所有孤独数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter=Counter(nums)
        ret=[]
        for k,v in counter.items():
            if v>1:
                continue
            if k-1 not in counter and k+1 not in counter:
                ret.append(k)
        return ret

# @lc code=end



#
# @lcpr case=start
# [10,6,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,3]\n
# @lcpr case=end

#

