#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
from typing import List
# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # max_h=3
        # max_min=5
        if turnedOn>8:
            return []
        h_min=max(0,turnedOn-5)
        h_max=min(turnedOn,3)
        def count_bits(n):
            ret=0
            while n>0:
                n&=n-1
                ret+=1
            return ret
        def get_hours(count:int):
            ret=[]
            for i in range(12):
                if count_bits(i)==count:
                    ret.append(str(i))
            return ret

        def get_minutes(count:int):
            ret=[]
            for i in range(60):
                if count_bits(i)==count:
                    ret.append(str(i) if i >9 else '0'+str(i))
            return ret
        ret=[]
        for h in range(h_min,h_max+1):
            hours=get_hours(h)
            minuts=get_minutes(turnedOn-h)
            for hour in hours:
                for minute in minuts:
                    ret.append(hour+':'+minute)
        return ret
# @lc code=end
print(Solution().readBinaryWatch(5))
print(Solution().readBinaryWatch(1))
print(Solution().readBinaryWatch(2))
print(Solution().readBinaryWatch(9))
