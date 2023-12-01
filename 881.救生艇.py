#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#
from typing import List
# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        l,r=0,n-1
        ret=0
        while l<=r:
            s=people[l]+people[r]
            if s>limit:
                r-=1
            else:
                l+=1
                r-=1
            ret+=1

        return ret
# @lc code=end
people = [3,5,3,4]
limit = 5
assert Solution().numRescueBoats(people,limit)==4

people = [3,2,2,1]
limit = 3
assert Solution().numRescueBoats(people,limit)==3

people = [1,2]
limit = 3
assert Solution().numRescueBoats(people,limit)==1
