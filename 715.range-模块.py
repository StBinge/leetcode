#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#

# @lc code=start
# class SegmentTree:
#     def __init__(self,l,r,val=-1) -> None:
#         self.l=l
#         self.r=r
#         self.mid=(l+r)//2
#         self.val=val
#         self.left=self.right=None
#         self.lazy=0
    
#     def pushdown(self):
#         # mid=(self.l+self.r)>>1
#         if not self.left:
#             self.left=SegmentTree(self.l,self.mid)
#         if not self.right:
#             self.right=SegmentTree(self.mid+1,self.r)
#         if self.lazy:
#             # flag=self.lazy>0
#             self.left.val=self.right.val=self.left.lazy=self.right.lazy=self.lazy
#             # self.lazy=None
#             self.lazy=0

#     def pushup(self):
#         if self.left and self.left.val>0 and self.right and self.right.val>0:
#             self.val=1
#         else:
#             self.val=-1


#     def update(self,l,r,val):
#         if l>r:
#             return
#         if l<=self.l and self.r<=r:
#             self.val=val
#             self.lazy=val
#             return
#         self.pushdown()
#         if l<=self.mid:
#             self.left.update(l,r,val)
#         if r>self.mid:
#             self.right.update(l,r,val)
#         self.pushup()
    
#     def query(self,l,r):
#         # if l>r:
#         #     return True
#         if l<=self.l and self.r<=r:
#             return self.val>0
#         self.pushdown()
#         # ret=True
#         if l>self.mid:
#             return self.right.query(l,r)
#         if r<=self.mid:
#             return self.left.query(l,r)
#         return self.left.query(l,r) and self.right.query(l,r)
import bisect
class RangeModule:

    def __init__(self):
        self.range=[]


    def addRange(self, left: int, right: int) -> None:
        first=bisect.bisect_left(self.range,left,key=lambda r:r[1])
        last=bisect.bisect_right(self.range,right,key=lambda r:r[0])
        if first<last:
            start=min(self.range[first][0],left)
            end=max(self.range[last-1][1],right)
            self.range=self.range[:first]+[[start,end]]+self.range[last:]
        else:
            self.range.insert(first,[left,right])
        

    def queryRange(self, left: int, right: int) -> bool:
        idx=bisect.bisect_right(self.range,left,key=lambda r:r[0])-1
        if idx<0:
            return False
        return self.range[idx][1]>=right

    def removeRange(self, left: int, right: int) -> None:
        first=bisect.bisect_right(self.range,left,key=lambda r:r[1])
        last=bisect.bisect_left(self.range,right,key=lambda r:r[0])
        if first<last:
            r=[]
            if self.range[first][0]<left:
                r.append([self.range[first][0],left])
            if (e:=self.range[last-1][1])>right:
                r.append([right,e])
            self.range=self.range[:first]+r+self.range[last:]


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# @lc code=end

rangeModule = RangeModule()#
rangeModule.addRange(10, 20)#
rangeModule.removeRange(14, 16)#
assert rangeModule.queryRange(10, 14)# 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
assert not rangeModule.queryRange(13, 15)# 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
assert rangeModule.queryRange(16, 17)# 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）