#
# @lc app=leetcode.cn id=3202 lang=python3
# @lcpr version=30204
#
# [3202] 找出有效子序列的最大长度 II
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N=len(nums)
        pos_map=defaultdict(list)
        for i,n in enumerate(nums):
            pos_map[n%k].append(i)
        ret=0
        
        sorted_pos=sorted(pos_map.values(),key=len,reverse=True)
        for pos_ar in sorted_pos:
            ret=max(ret,len(pos_ar))
            pos_ar.append(N)
            pre=0
            cnt=Counter()
            for p in pos_ar:
                s=set(pos_ar[pre:p])
                cnt.update(s)
                pre=p+1
            mx=max(cnt.values())



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,3,1,4]\n3\n
# @lcpr case=end

#

