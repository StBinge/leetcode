#
# @lc app=leetcode.cn id=2359 lang=python3
# @lcpr version=30204
#
# [2359] 找到离给定两个节点最近的节点
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N=len(edges)
        def min_dist(x):
            dist=[N]*N
            d=0
            while x>=0 and dist[x]>d:
                dist[x]=d
                d+=1
                x=edges[x]
            return dist
        
        mi=N
        ret=-1
        for idx,[d1,d2] in enumerate(zip(min_dist(node1),min_dist(node2))):
            d=max(d1,d2)
            if mi>d:
                mi=d
                ret=idx
        return ret
# @lc code=end
assert Solution().closestMeetingNode([3,0,5,-1,3,4],2,0)==3
assert Solution().closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2)==2
assert Solution().closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1)==2


#
# @lcpr case=start
# [2,2,3,-1]\n0\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,-1]\n0\n2\n
# @lcpr case=end

#

