#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
from typing import List
# @lc code=start
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        counter=Counter(tasks)
        max_cnt=max(counter.values())
        max_type_cnt=sum([1 for k in counter if counter[k]==max_cnt])
        return max((n+1)*(max_cnt-1)+max_type_cnt,len(tasks))
            


        
# @lc code=end
tasks=["A","B","C","D","E","A","B","C","D","E"]
n=4
assert Solution().leastInterval(tasks,n)==10

tasks = ["A","A","A","B","B","B"]
n = 2
assert Solution().leastInterval(tasks,n)==8

tasks = ["A","A","A","B","B","B"]
n = 0
assert Solution().leastInterval(tasks,n)==6

tasks=["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
assert Solution().leastInterval(tasks,n)==16
