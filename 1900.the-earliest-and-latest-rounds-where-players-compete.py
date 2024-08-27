#
# @lc app=leetcode.cn id=1900 lang=python3
# @lcpr version=30204
#
# [1900] 最佳运动员的比拼回合
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @cache
        def dfs(n:int,f,s):
            if f+s==n+1:
                return [1,1]
            if f+s>n+1:
                f,s=n+1-s,n+1-f
            half=(n+1)//2
            Min=n
            Max=0
            if s<=half:
                for i in range(f):
                    for j in range(s-f):
                        mi,mx=dfs(half,i+1,i+j+2)
                        Min=min(mi,Min)
                        Max=max(Max,mx)
            else:
                ss=n+1-s
                mid=(n-2*ss+1)//2
                for i in range(f):
                    for j in range(ss-f):
                        mi,mx=dfs(half,i+1,i+j+mid+2)
                        Min=min(mi,Min)
                        Max=max(Max,mx)
            return [1+Min,1+Max]
        
        if firstPlayer>secondPlayer:
            firstPlayer,secondPlayer=secondPlayer,firstPlayer

        ret= dfs(n,firstPlayer,secondPlayer)
        return ret



# @lc code=end
assert Solution().earliestAndLatest(18,6,12) == [3, 5]
assert Solution().earliestAndLatest(11, 2, 4) == [3, 4]
assert Solution().earliestAndLatest(11, 2, 4) == [3, 4]
assert Solution().earliestAndLatest(10,1,2) == [4, 4]
assert Solution().earliestAndLatest(5, 1, 5) == [1, 1]


#
# @lcpr case=start
# 11\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# 5\n1\n5\n
# @lcpr case=end

#
