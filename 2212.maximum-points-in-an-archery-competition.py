#
# @lc app=leetcode.cn id=2212 lang=python3
# @lcpr version=30204
#
# [2212] 射箭比赛中的最大得分
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        Mask=1<<11
        mx=0
        ret=None
        for mask in range(1,Mask):
            cnt=0
            score=0
            for i in range(12):
                if mask & (1<<i):
                    cnt+=aliceArrows[i+1]+1
                    score+=i+1
            if cnt<=numArrows and score>mx:
                mx=score
                ret=mask   

        arrows=[0]
        for i in range(11):
            if ret & (1<<i):
                arrows.append(aliceArrows[i+1]+1)
            else:
                arrows.append(0)
        arrows[-1]+=numArrows-sum(arrows)
        return arrows

# @lc code=end
def check(numArrows, aliceArrows,answer:list):
    ret=Solution().maximumBobPoints(numArrows,aliceArrows)
    if sum(ret)!=numArrows:
        error=f'Arrows nums not equal!'
        print(error)
        return
    ans=0
    res=0
    for i in range(12):
        if answer[i]>aliceArrows[i]:
            ans+=i
        if ret[i]>aliceArrows[i]:
            res+=i
    
    assert ans==res, 'score not equal'

check(3,[0,0,1,0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,0,1,1,1,0])
check(numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0],answer=[0,0,0,0,1,1,0,0,1,2,3,1])

#
# @lcpr case=start
# 9\n[1,1,0,1,0,0,2,1,0,1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[0,0,1,0,0,0,0,0,0,0,0,2]\n
# @lcpr case=end

#

