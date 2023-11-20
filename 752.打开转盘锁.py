#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
from typing import List

# @lc code=start
import heapq
class Astar:
    @staticmethod
    def getH(code,target):
        ret=0
        for i in range(4):
            dist=abs(int(code[i])-int(target[i]))
            ret+=min(dist,10-dist)
        return ret

    def __init__(self,code,target,g) -> None:
        self.code=code
        self.g=g
        self.f=g+Astar.getH(code,target)
    
    def __lt__(self,other:'Astar'):
        return self.f<other.f

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        deads = set(deadends)
        if target in deads or '0000' in deads:
            return -1
        
        def get_next_code(code:str):
            code=list(code)
            for i in range(4):
                num=code[i]
                code[i]='0' if num=='9' else str(int(num)+1)
                yield ''.join(code)
                code[i]='9' if num=='0' else str(int(num)-1)
                yield ''.join(code)
                code[i]=num
        visited = {'0000'}

        queue = [Astar('0000',target,0)]

        while queue:
            node=heapq.heappop(queue)
            for next_code in get_next_code(node.code):
                if next_code==target:
                    return node.g+1
                if next_code in visited or next_code in deads:
                    continue
                heapq.heappush(queue,Astar(next_code,target,node.g+1))
                visited.add(next_code)
        return -1


# @lc code=end
assert Solution().openLock(["0000"], "8888") == -1

deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
assert Solution().openLock(deadends, target) == 6
