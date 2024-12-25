#
# @lc app=leetcode.cn id=LCP 72 lang=python3
# @lcpr version=30204
#
# [LCP 72] 补给马车
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        N=len(supplies)
        start=list(range(N))
        end=list(range(N))
        def find(x):
            if x!=start[x]:
                start[x]=find(start[x])
            return start[x]
        heap=[]
        for i in range(N-1):
            heapq.heappush(heap,[supplies[i]+supplies[i+1],i,i+1])
        
        cnt=(N+1)//2
        while cnt>0:
            s,i,j=heapq.heappop(heap)
            fi=find(i)
            fj=find(j)
            if i!=fi or j!=fj or s!=supplies[fi]+supplies[fj]:
                continue
            supplies[i]+=supplies[j]
            start[j]=i
            end[i]=end[j]
            if i>0:
                k=find(i-1)
                heapq.heappush(heap,[supplies[k]+supplies[i],k,i])
            if end[j]<N-1:
                k=find(end[j]+1)
                heapq.heappush(heap,[supplies[i]+supplies[k],i,k])
            cnt-=1
        
        return [supplies[i] for i,fa in enumerate(start) if i==fa]



# @lc code=end
assert Solution().supplyWagon([17,23,59,30,57,85,84,17,67,10,91,57,64,6,11,6,94,5,54,16,86,3,29,19,79,37,8,24,68,26,82,36,92,37,73,82,41,90,57,24,52,75,61,39,20,28,6,58,88,96,58,4,23,45,72,81,90,51,87,44,16,63,56,71,3,31,85,12,64,41,52,66,25,76,97,69,9,61,51,25,21,62,50,2,95,86,98,14,6,61,89,44,89]
)==[99,87,85,84,94,91,144,94,75,86,130,69,94,118,92,110,123,90,133,136,93,146,96,130,72,81,90,138,60,119,105,85,76,93,91,76,97,139,97,114,95,86,98,81,133,89]
assert Solution().supplyWagon([6,2,2,6,9,8,5,7])==[10,15,8,12]
assert Solution().supplyWagon([6,2,2,6,9,8,5,7])==[10,15,8,12]
assert Solution().supplyWagon( [1,3,1,5])==[5,5]
assert Solution().supplyWagon( [7,3,6,1,8])==[10,15]


#
# @lcpr case=start
# [7,3,6,1,8]`>\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1,5]`>\n
# @lcpr case=end

#

