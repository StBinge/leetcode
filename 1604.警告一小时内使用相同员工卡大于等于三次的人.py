#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] 警告一小时内使用相同员工卡大于等于三次的人
#
from sbw import *
# @lc code=start
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        cache=defaultdict(list)
        for name,time in zip(keyName,keyTime):
            h,m=map(int,time.split(':'))
            cache[name].append(h*60+m)
        
        ret=[]
        for name,times in cache.items():
            times.sort()
            if any(times[i]-times[i-2]<=60 for i in range(2,len(times)) ):
                ret.append(name)
        return sorted(ret)
# @lc code=end

assert Solution().alertNames(keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"])==["bob"]
assert Solution().alertNames(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"])==["daniel"]