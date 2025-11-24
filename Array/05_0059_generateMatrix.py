from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0]*n for _ in range(n)]
        startx,starty = 0,0
        offset = 1
        count = 1
        mid = n//2
        while offset<=n//2 :    # Point: 理解循环矩阵结构 - n×n 矩阵需要画 ⌈n/2⌉ 圈（向上取整）
            for j in range(starty,n-offset):    # Point: 横向移动动y轴，纵向移动x轴
                nums[startx][j] = count        # 不应该使用+=，应该直接赋值 - 虽然初始化是0
                count += 1                      # Point:j会自动+1，要修改不会自动加的变量
            for i in range(startx,n-offset,):   # Point: 边界 [ , ) 左开右闭，最后的点留给下一个循环处理
                nums[i][n-offset] = count
                count += 1 
            for j in range(n-offset,starty,-1):
                nums[n-offset][j] = count
                count += 1
            for i in range(n-offset,startx,-1):
                nums[i][starty] = count         # 最后的时候，y轴在starty的位置
                count += 1
            startx += 1
            starty += 1
            offset +=1
        if n % 2 == 1:
            nums[mid][mid] = count
        return nums

if __name__ == "__main__":
    s = Solution()
    res = s.generateMatrix(3)
    print(res)


"""
思路：
    1.严格控制边界，使用[ , ) 左开右闭，最后的点留给下一个循环处理 
    2.画图确定4个点的坐标，分别是（stattx, starty）, (startx, n-offset), (n-offset, n-offset), (n-offset, starty)
    3.横向移动改变y轴，纵向移动改变x轴 
    4.如果n为奇数，则需要单独处理中心点
Point：
    1.j会自动+1，要修改不会自动加的变量count
    2.nums的修改不应该使用+=，应该直接赋值
    3.理解循环矩阵结构 - 必须清楚while循环的次数
        比如n=3，需要画1圈，n=4，需要画2圈，此时start与offset都要分别往里移一位

"""