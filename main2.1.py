#2.1给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
arr=input("输入一个一维数组，每个数之间使空格隔开：")
nums=[int(n) for n in arr.split()]#初始化数组,命名为nums
newnums1=[]#降序排序数组
x=0
y=0#计数器
for i in nums:
    if abs(nums[x])>abs(nums[len(nums)-y-1]):#还未排序的第一位和还未排序的最后一位比较
        newnums1.append(nums[x]**2)
        x+=1
        if x+y==len(nums):#检索过所有元素后结束循环
            break
    if abs(nums[x])<=abs(nums[len(nums)-y-1]):
        newnums1.append(nums[len(nums)-y-1]**2)
        y+=1
        if x+y==len(nums):
            break
newnums1.reverse()#将降序逆转，变成升序排序
print(newnums1)
