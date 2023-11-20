#
# @lc app=leetcode.cn id=672 lang=python3
#
# [672] 灯泡开关 Ⅱ
#

# @lc code=start
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        pressArr=[0]*4
        ret=set()
        for i in range(2**4):
            for j in range(4):
                pressArr[j]=(i>>j) &1
            
            s=sum(pressArr)
            if s%2==presses%2 and s<=presses:
                state=pressArr[0]^pressArr[2]^pressArr[3]
                if n>1:
                    state|=(pressArr[0]^pressArr[1])<<1
                if n>2:
                    state|=(pressArr[0] ^ pressArr[2])<<2
                # if n>3:
                #     state|=(pressArr[0]^pressArr[1]^pressArr[3])<<3
                ret.add(state)
        return len(ret)

# @lc code=end

assert Solution().flipLights(1,1)==2
assert Solution().flipLights(2,1)==3
assert Solution().flipLights(3,1)==4