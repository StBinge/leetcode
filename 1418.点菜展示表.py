#
# @lc app=leetcode.cn id=1418 lang=python3
#
# [1418] 点菜展示表
#
from sbw import *
# @lc code=start
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables={}
        foods=set()
        for _,table,food in orders:
            tab=tables.setdefault(table,defaultdict(int))
            tab[food]+=1
            foods.add(food)
        foods=sorted(foods)
        foods_idx={f:i for i,f in enumerate(sorted(foods))}
        ret=[]
        ret.append(['Table']+foods)
        L=len(foods)
        for tab in sorted(tables.keys(),key=int):
            cnt=[0]*L
            for f,v in tables[tab].items():
                cnt[foods_idx[f]]+=v
            row=[tab]+[str(v) for v in cnt]
            ret.append(row)
        return ret
# @lc code=end
assert Solution().displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]])==[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]  
assert Solution().displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])==[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
