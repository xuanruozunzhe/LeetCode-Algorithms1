# LeetCode-Algorithms1
二分查找、第一个错误的版本、搜索插入位置

1.1给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
示例1：
输入: -1 0 3 5 9 12
9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例2：
输入: -1 0 3 5 9 12
2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

1.2你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
示例1：
输入：5
4
输出：left=3mid=4
错误版本号为：4

1.3给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
示例1：
输入: 1 3 5 6
5
输出: 2
示例2：
输入: 1 3 5 6
2
输出: 1
示例3：
输入: 1 3 5 6
7
输出: 4
示例4：
输入: 1 3 5 6
0
输出: 0

有序数组的平方、轮转数组

2.1给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例1: 
输入: -6 -1 0 4
输出: [0, 1, 16, 36]
示例2: 
输入: -4 -3 0 3 5
输出: [0, 9, 9, 16, 25]

有序数组的平方、轮转数组

2.2给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
示例1：
输入:1 2 3 4 5 6 7
3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例2：
输入：nums = -1 -100 3 99
2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

移动零、两数之和Ⅱ-输入有序数组

3.1给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例1：
输入: 0 1 0 3 12
输出: [1,3,12,0,0]
示例2：
输入: 0
输出: [0]

3.2给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
你所设计的解决方案必须只使用常量级的额外空间。
示例1：
输入：2 7 11 15
9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 
示例2：
输入：2 3 4
6
输出：[1,3]
示例3：
输入：-1 0
-1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

反转字符串、反转字符串中的单词Ⅲ

4.1
