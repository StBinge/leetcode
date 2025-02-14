#
# @lc app=leetcode.cn id=2453 lang=python3
# @lcpr version=30204
#
# [2453] 摧毁一系列目标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        cnt=defaultdict(int)
        num_map={}
        for n in nums:
            t=n%space
            cnt[t]+=1
            num_map[t]=min(num_map.get(t,float('inf')),n)
        
        ret=float('inf')
        mx=0
        for k,v in cnt.items():
            if v>mx:
                mx=v
                ret=num_map[k]
            elif v==mx:
                ret=min(ret,num_map[k])
        return ret
            

# @lc code=end
assert Solution().destroyTargets([1,5,3,2,2],10000)==2


#
# @lcpr case=start
# [3,7,8,1,1,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,2,4,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [6,2,5]\n100\n
# @lcpr case=end

#

