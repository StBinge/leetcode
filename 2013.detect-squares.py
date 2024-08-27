#
# @lc app=leetcode.cn id=2013 lang=python3
# @lcpr version=30204
#
# [2013] 检测正方形
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class DetectSquares:

    def __init__(self):
        self.points=defaultdict(Counter)
  

    def add(self, point: List[int]) -> None:
        x,y=point
        self.points[x][y]+=1


    def count(self, point: List[int]) -> int:
        x,y=point
        cols=self.points[x]
        ret=0
        for xx,ccols in self.points.items():
            if xx==x:
                continue
            d=xx-x
            ret+=ccols[y]*ccols[y+d]*cols[y+d]
            ret+=ccols[y]*ccols[y-d]*cols[y-d]
        return ret


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
ret='[null,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,2,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,2,null,null,null,2,null,null,null,2,null,null,null,2,null,null,null,5]'
ret=eval_list_str(ret)
detectSquares = DetectSquares()

ops=["DetectSquares","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add"]

args=[[],[[5,10]],[[10,5]],[[10,10]],[[5,5]],[[3,0]],[[8,0]],[[8,5]],[[3,5]],[[9,0]],[[9,8]],[[1,8]],[[1,0]],[[0,0]],[[8,0]],[[8,8]],[[0,8]],[[1,9]],[[2,9]],[[2,10]],[[1,10]],[[7,8]],[[2,3]],[[2,8]],[[7,3]],[[9,10]],[[9,5]],[[4,5]],[[4,10]],[[0,9]],[[4,5]],[[4,9]],[[0,5]],[[1,10]],[[10,1]],[[10,10]],[[1,1]],[[10,0]],[[2,0]],[[2,8]],[[10,8]],[[7,6]],[[4,6]],[[4,9]],[[7,9]],[[10,9]],[[10,0]],[[1,0]],[[1,9]],[[0,9]],[[8,1]],[[0,1]],[[8,9]],[[3,9]],[[10,9]],[[3,2]],[[10,2]],[[3,8]],[[9,2]],[[3,2]],[[9,8]],[[0,9]],[[7,9]],[[0,2]],[[7,2]],[[10,1]],[[1,10]],[[10,10]],[[1,1]],[[6,10]],[[2,6]],[[6,6]],[[2,10]],[[6,0]],[[6,2]],[[8,2]],[[8,0]],[[6,5]],[[7,4]],[[6,4]],[[7,5]],[[2,10]],[[8,4]],[[2,4]],[[8,10]],[[2,6]],[[2,5]],[[1,5]],[[1,6]],[[10,9]],[[10,0]],[[1,9]],[[1,0]],[[0,9]],[[5,9]],[[0,4]],[[5,4]],[[3,6]],[[9,0]],[[3,0]],[[9,6]],[[0,2]],[[1,1]],[[0,1]],[[1,2]],[[1,7]],[[8,0]],[[8,7]],[[1,0]],[[2,7]],[[4,5]],[[2,5]],[[4,7]],[[6,7]],[[3,7]],[[6,4]],[[3,4]],[[10,2]],[[2,10]],[[2,2]],[[10,10]],[[10,1]],[[1,10]],[[1,1]],[[10,10]],[[2,10]]]

for i in range(1,len(ret)):
    if ops[i]=='add':
        detectSquares.add(args[i][0])
    elif ops[i]=='count':
        assert detectSquares.count(args[i][0])==ret[i] 
    else:
        raise 'Wrong op:'+ops[i]

#
# @lcpr case=start
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"][[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]\n
# @lcpr case=end

#

