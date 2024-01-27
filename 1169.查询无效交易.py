#
# @lc app=leetcode.cn id=1169 lang=python3
#
# [1169] 查询无效交易
#
from sbw import *
# @lc code=start
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        convert_transactions=[]
        for trans in transactions:
            parts=trans.split(',')
            amount=int(parts[2])
            name=parts[0]
            time=int(parts[1])
            city=parts[3]
            convert_transactions.append([name,time,amount,city])
        convert_transactions.sort(key=lambda x:x[1])
        memo={}
        ret=set()

        def bisect(timeline:list,target):
            l,r=0,len(timeline)
            while l<r:
                mid=(l+r)>>1
                x=timeline[mid][0]
                if x<target:
                    l=mid+1
                else:
                    r=mid
            return l


        for i,trans in enumerate(convert_transactions):
            # parts=trans.split(',')
            # amount=int(parts[2])
            if trans[2]>1000:
                ret.add(i)

            name=trans[0]
            time=trans[1]
            city=trans[3]
            memo.setdefault(name,[])
            timeline=memo[name]
            idx=bisect(timeline,time-60)
            found=False
            for j in range(idx,len(timeline)):
                tid=timeline[j][1]
                if convert_transactions[tid][3]!=city:
                    ret.add(tid)
                    found=True
            if found:
                ret.add(i)
            timeline.append([time,i])
        return [','.join(map(str,convert_transactions[i])) for i in ret]

# @lc code=end
ret= Solution().invalidTransactions( ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
)
assert sorted(ret)==sorted(["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"])

ret= Solution().invalidTransactions( ["alice,20,800,mtv","alice,50,1200,mtv"])
assert sorted(ret)==sorted(["alice,50,1200,mtv"])

ret= Solution().invalidTransactions( ["alice,20,800,mtv","alice,50,1200,mtv"])
assert sorted(ret)==sorted(["alice,50,1200,mtv"])

ret= Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])
assert sorted(ret)==sorted(["alice,20,800,mtv","alice,50,100,beijing"])
