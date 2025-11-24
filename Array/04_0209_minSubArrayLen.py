from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 定义最终返回的子数组长度
        result = float("inf")       # Point: 初始化为无穷大，否则会一直返回0
        # 定义起始指针
        i = 0
        # 定义子数组和
        sum = 0
        # 按照双指针方式定义，定义终点指针
        for j in range(len(nums)):
            sum += nums[j]
            j += 1
            while sum>=target:     # Point: if or while? 如果使用if，则不会在sum>=target时，继续移动i指针，导致结果不正确
                subl = j - i
                result = min(result,subl)
                sum -= nums[i]      # Point： 移动起始指针的同时需要将值从子数组和中减去
                i += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    result = solution.minSubArrayLen(target, nums)
    print(result)

# 思路总结
"""
思路
    1.使用双指针实现滑动窗口
    2.for循环的j代表终点指针
    3.当子数组和>target的时候操作起始指针
Point
    1.if or while? 如果使用if，则不会在sum>=target时，继续移动i指针，导致结果不正确
    2.移动起始指针的同时需要将值从子数组和中减去
    3.初始化result为无穷大，否则会一直返回0 
"""