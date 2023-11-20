#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#
from typing import List
# @lc code=start
import random
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.map={}

        valid_tail=n-1
        for black in blacklist:
            if valid_tail==black:
                valid_tail-=1
                continue
            self.map[black]=valid_tail
            valid_tail-=1
        self.right=n-len(blacklist)-1
        

    def pick(self) -> int:
        
        r=random.randint(0,self.right) if self.right>0 else 0
        if r not in self.map:
            return r
        rr=r
        while rr in self.map:
            rr=self.map[rr]
        self.map[r]=rr
        return rr


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end
fDu116864
s=Solution(5,[2,0,4])
for _ in range(10):
    print(s.pick())