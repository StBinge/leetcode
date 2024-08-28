#
# @lc app=leetcode.cn id=1792 lang=python3
#
# [1792] 最大平均通过率
#
from sbw import *
# @lc code=start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap=[]
        def growth(p,t):
            return (p+1)/(t+1)-p/t
        for p,t in classes:
            g=-growth(p,t)
            heapq.heappush(heap,[g,p,t])
        
        for i in range(extraStudents):
            _,p,t=heap[0]
            p+=1
            t+=1
            heapq.heapreplace(heap,[-growth(p,t),p,t])
        return sum(p/t for _,p,t in heap)/len(classes)
# @lc code=end
ret=Solution().maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4)
assert_answer(0.53485,ret)
ret=Solution().maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
assert_answer(0.78333,ret)