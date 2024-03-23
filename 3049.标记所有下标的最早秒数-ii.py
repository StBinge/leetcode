#
# @lc app=leetcode.cn id=3049 lang=python3
#
# [3049] 标记所有下标的最早秒数 II
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        N=len(nums)
        M=len(changeIndices)
        if N>M:
            return -1
        slow=sum(nums)+N      
        first_t={}
        for s in range(M-1,-1,-1):
            first_t[changeIndices[s]-1]=s
        if not first_t:
            ret=slow
            return -1 if ret>M else ret
        # s_idx_sorted=sorted([s,idx] for idx,s in idx_s.items())

        def check(s:int):
            tot=slow
            cnt=0
            h=[]
            for t in range(s-1,-1,-1):
                idx=changeIndices[t]-1
                v=nums[idx]
                if v<=1 or t!=first_t.get(idx,-1):
                    cnt+=1
                    continue
                if cnt==0:
                    if not h or v<=h[0]:
                        cnt+=1
                        continue
                    tot+=heapq.heappop(h)+1
                    cnt+=2
                tot-=v+1
                cnt-=1
                heapq.heappush(h,v)
            return cnt>=tot

        ret=N+bisect_left(range(N,M+1),True,key=check)
        return ret if ret<=M else -1

# @lc code=end
assert Solution().earliestSecondToMarkIndices([0,0],[1,1,1,1])==2
assert Solution().earliestSecondToMarkIndices([5,3,2,0,3,5],[4,3,6,5,6,5,3,6,4,1,2,3,6,1])==13
assert Solution().earliestSecondToMarkIndices([0,3],[1,1,2,1,2,2,2,2,2])==4
assert Solution().earliestSecondToMarkIndices([0,2,4],[1,2,1,1,2,1,3,3,1,1])==8
assert Solution().earliestSecondToMarkIndices([0,2],[1,1,2,2,1])==4
assert Solution().earliestSecondToMarkIndices(nums = [1,2,3], changeIndices = [1,2,3])==-1
assert Solution().earliestSecondToMarkIndices(nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2])==7
assert Solution().earliestSecondToMarkIndices(nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3])==6
