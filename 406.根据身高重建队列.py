#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
from typing import List
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p:(-p[0],p[1]))
        # print(people)
        pos=[[] for _ in range(len(people))]
        cnt=0
        for i,p in enumerate(people):
            pos[p[1]].append(i)
        

        ret=[None]*len(people)
        idx=0
        for p in pos:            
            for pp in reversed(p):
                ret[idx]=people[pp]
                idx+=1
        return ret

# @lc code=end
r=Solution().reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])
print(r)
#[[3, 0], [6, 0], [7, 0], [5, 2], [3, 4], [5, 3], [6, 2], [2, 7], [9, 0], [1, 9]]

r=Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
print(r)
#[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]