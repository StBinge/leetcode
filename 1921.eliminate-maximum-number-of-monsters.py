#
# @lc app=leetcode.cn id=1921 lang=python3
# @lcpr version=30204
#
# [1921] 消灭怪物的最大数量
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        N=len(dist)
        # 最晚消灭时间
        cnt=[0]*(N+1)
        for d,s in zip(dist,speed):
            # 如果时间大于N肯定能被消灭
            cnt[min((d-1)//s,N)]+=1
        
        # 累计开枪次数
        ret=0
        for i in range(N+1):
            # 在时刻i时, 开枪总数=i+1
            # 如果累计开枪次数+当前需要消灭的数量<=总开枪次数, 可以挺过这一次
            if ret+cnt[i]<=i+1:
                ret+=cnt[i]
            else:
                # 挺不过这次, 最多开i+1枪
                return i+1
        return N
# @lc code=end
assert Solution().eliminateMaximum(dist = [3,2,4], speed = [5,3,2])==1
assert Solution().eliminateMaximum(dist = [1,1,2,3], speed = [1,1,1,1])==1
assert Solution().eliminateMaximum(dist = [1,3,4], speed = [1,1,1])==3


#
# @lcpr case=start
# [1,3,4]\n[1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3]\n[1,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n[5,3,2]\n
# @lcpr case=end

#

