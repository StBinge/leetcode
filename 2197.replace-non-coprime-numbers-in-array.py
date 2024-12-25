#
# @lc app=leetcode.cn id=2197 lang=python3
# @lcpr version=30204
#
# [2197] 替换数组中的非互质数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        changed=True
        while changed:
            changed=False
            temp=nums[:1]
            for n in nums[1:]:
                g=math.gcd(temp[-1],n)
                if g>1:
                    last=temp.pop()
                    temp.append(n*last//g)
                    changed=True
                else:
                    temp.append(n)
            nums=temp
        return nums
# @lc code=end



#
# @lcpr case=start
# [6,4,3,2,7,6,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,3,3,3]\n
# @lcpr case=end

#

