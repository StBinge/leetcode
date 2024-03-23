#
# @lc app=leetcode.cn id=1352 lang=python3
#
# [1352] 最后 K 个数的乘积
#
from sbw import *
# @lc code=start
class ProductOfNumbers:

    def __init__(self):
        self.pre_prods=[1]

    def add(self, num: int) -> None:
        if num==0:
            self.pre_prods=[1]
        else:
            self.pre_prods.append(num*self.pre_prods[-1])

    def getProduct(self, k: int) -> int:
        if k+1>len(self.pre_prods):
            return 0
        return self.pre_prods[-1]//self.pre_prods[-(k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end
obj=ProductOfNumbers()
ops=["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
args=[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
res='[null,null,null,null,null,null,20,40,0,null,32]'
res=eval_list_str(res)
for op,arg,r in list(zip(ops,args,res))[1:]:
    if op=='add':
        assert obj.add(arg[0])==r
    else:
        assert obj.getProduct(arg[0])==r