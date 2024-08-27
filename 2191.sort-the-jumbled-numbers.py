#
# @lc app=leetcode.cn id=2191 lang=python3
# @lcpr version=30204
#
# [2191] 将杂乱无章的数字排序
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(x):
            if x<10:
                return mapping[x]
            digits=[]
            while x:
                digits.append(x%10)
                x//=10
            ret=0
            for d in reversed(digits):
                ret=ret*10+mapping[d]
            return ret
        
        nums.sort(key=convert)
        return nums
# @lc code=end

assert Solution().sortJumbled([9,8,7,6,5,4,3,2,1,0],[0,1,2,3,4,5,6,7,8,9])==[9,8,7,6,5,4,3,2,1,0]
assert Solution().sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38])==[338,38,991]

#
# @lcpr case=start
# [8,9,4,0,2,1,3,5,7,6]\n[991,338,38]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,3,4,5,6,7,8,9]\n[789,456,123]\n
# @lcpr case=end

#

