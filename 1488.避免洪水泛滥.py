#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
#
from sbw import *
# @lc code=start
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # counter=Counter(rains)
        # pool_cnt=len(counter)-1
        # tot_days=len(rains)
        # no_rain_days=counter[0]
        # rain_days=tot_days-no_rain_days
        # if rain_days-pool_cnt>no_rain_days:
        #     return []
        
        full_pools={}
        can_removed=deque()
        ret=[-1]*len(rains)

        for i,p in enumerate(rains):
            if p==0:
                if len(full_pools)==0:
                    ret[i]=1
                elif len(full_pools)==1:
                    k,_=full_pools.popitem()
                    ret[i]=k
                    continue
                can_removed.append([i,True])
                continue
            if p in full_pools:
                while can_removed and can_removed[0][1]==False:
                    can_removed.popleft()
                for entry in can_removed:
                    if entry[1]==False:
                        continue
                    if entry[0]>full_pools[p]:                        
                        ret[entry[0]]=p
                        entry[1]=False
                        break
                else:
                    return []
            full_pools[p]=i
        for idx,flag in can_removed:
            if not flag:
                continue
            ret[idx]=1
        return ret
            

# @lc code=end
def test(rains):
    ret=Solution().avoidFlood(rains)
    if ret==[]:
        return
    full=set()
    for p1,p2 in zip(rains,ret):
        if p1>0:
            if p1 in full:
                raise
            full.add(p1)
        else:
            if p2>0:
                full.discard(p2)
    


test([1,0,2,3,0,1,2])
test([1,2,0,1,2])
test([1,2,0,0,2,1])
test([1,2,3,4])
