#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#
from typing import List
# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        l=len(num)
        if l<3:
            return []
        nums=list(map(int,num))
        if l==3:
            return nums[0]+nums[1]==nums[2]

        ret=[]
        Max=2**31
        def dfs(idx):
            nonlocal l,ret
            if idx==l:
                if len(ret)>2:
                    return True
                return False
            cur=0
            
            for i in range(idx,l):
                if i>idx and nums[idx]==0:
                    break
                cur=cur*10+nums[i]
                if cur>=Max:
                    return False
                if len(ret)<2:
                    ret.append(cur)
                    if dfs(i+1):
                        return True
                    ret.pop()
                else:
                    target=ret[-1]+ret[-2]
                    if cur==target:
                        ret.append(cur)
                        if dfs(i+1):
                            return True
                        ret.pop()
                    if cur>target:
                        return False
            return False
        dfs(0)
        return ret

# @lc code=end
nums="539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
assert Solution().splitIntoFibonacci(nums)==[]

num = "112358130"
assert Solution().splitIntoFibonacci(num)==[]

num = "1101111"
ret=[11,0,11,11]
assert Solution().splitIntoFibonacci(num)==ret