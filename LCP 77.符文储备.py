#
# @lc app=leetcode.cn id=LCP 77 lang=python3
# @lcpr version=30204
#
# [LCP 77] 符文储备
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        ret=0
        pre=runes[0]
        cnt=0
        for r in runes:
            if pre+1>=r:
                cnt+=1
    
            else:
                ret=max(cnt,ret)
                cnt=1
            pre=r
        return max(ret,cnt)
# @lc code=end
assert Solution().runeReserve([1,3,4,5,1,7])==3


#
# @lcpr case=start
# [1,3,5,4,1,7]`>\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,3,2,4]`>\n
# @lcpr case=end

#

