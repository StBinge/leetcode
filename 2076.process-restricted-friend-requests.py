#
# @lc app=leetcode.cn id=2076 lang=python3
# @lcpr version=30204
#
# [2076] 处理含限制条件的好友请求
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        p=list(range(n))
        
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
    
        
        forbids=[set() for i in range(n)]
        for x,y in restrictions:
            forbids[x].add(y)
            forbids[y].add(x)
        
        friends=[set([i]) for i in range(n)]

        ret=[]
        for x,y in requests:
            x,y=find(x),find(y)
            if friends[x].isdisjoint(forbids[y]) and friends[y].isdisjoint(forbids[x]):
                friends[x].update(friends[y])
                # friends[y]=friends[x]
                p[y]=x

                forbids[x].update(forbids[y])
                # forbids[y]=forbids[x]
                ret.append(True)
            else:
                ret.append(False)

        return ret
# @lc code=end
assert Solution().friendRequests(8,[[6,4],[7,5],[2,6],[1,5],[6,7],[6,5],[0,3],[5,4],[0,4],[2,7],[0,2]],[[6,3],[0,2],[0,5],[0,3],[6,4],[2,4],[1,0],[2,1],[2,5],[6,7],[7,0],[3,2],[3,5],[2,1],[1,6],[7,4],[6,3],[1,3],[6,5],[3,7],[7,0],[6,5],[0,5],[0,4],[7,5],[7,0],[7,0],[1,3]])==eval_list_str('[true,false,true,false,false,true,false,true,false,false,false,false,false,true,false,false,true,false,false,false,false,false,true,false,false,false,false,false]')
assert Solution().friendRequests(n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]])==eval_list_str('[true,false,true,false]')
assert Solution().friendRequests(n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]])==[True,False]
assert Solution().friendRequests(n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]])==[True,False]


#
# @lcpr case=start
# 3\n[[0,1]]\n[[0,2],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1]]\n[[1,2],[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,1],[1,2],[2,3]]\n[[0,4],[1,2],[3,1],[3,4]]\n
# @lcpr case=end

#

