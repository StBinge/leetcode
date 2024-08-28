#
# @lc app=leetcode.cn id=2121 lang=python3
# @lcpr version=30204
#
# [2121] 相同元素的间隔之和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        pos_map=defaultdict(list)
        for i,n in enumerate(arr):
            pos_map[n].append(i)
        
        ret=[0]*len(arr)
        for pos in pos_map.values():
            s=sum(p-pos[0] for p in pos)
            ret[pos[0]]=s
            n=len(pos)
            for i in range(1,n):
                s+=(2*i-n)*(pos[i]-pos[i-1])
                ret[pos[i]]=s
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,1,3,1,2,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [10,5,10,10]\n
# @lcpr case=end

#

