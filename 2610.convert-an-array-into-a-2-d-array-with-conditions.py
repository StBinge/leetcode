#
# @lc app=leetcode.cn id=2610 lang=python3
# @lcpr version=30204
#
# [2610] 转换二维数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt=Counter(nums)
        ret=[]
        for k,v in cnt.items():
            for i in range(v):
                if i>=len(ret):
                    ret.append([])
                ret[i].append(k)
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,3,4,1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#

