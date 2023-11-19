#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        segments=[0]*n
        segments[0]=1
        counter_idx=0
        pos=1
        ret=1
        while pos<n:
            counter_idx+=1
            next_char=1 if segments[pos-1]==2 else 2
            segments[pos]=next_char
            if next_char==1:
                ret+=1
            pos+=1
            if pos<n and segments[counter_idx]==2:
                segments[pos]=next_char
                pos+=1
                if next_char==1:
                    ret+=1
        
        return ret






# @lc code=end

assert Solution().magicalString(6)==3
assert Solution().magicalString(1)==1