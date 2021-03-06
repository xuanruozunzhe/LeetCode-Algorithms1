#1.1给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
arr=input("输入一个一维数组，每个数之间使空格隔开：")
nums=[int(n) for n in arr.split()]#初始化数组,命名为nums

target=int(input("输入一个数："))
left=1
right=len(nums)
mid=int((left+right)/2)
if nums[0]>target or nums[right-1]<target:#target超出数组范围，直接返回-1
    print(-1)
if nums[right-1]==target:#最后一个数比较特殊，需要单独列出
    print(right-1)
if nums[0]<=target and nums[right-1]>=target and nums[right-1]!=target:#target在数组范围内且不是最后一个数
    while left!=mid:
        if nums[mid - 1] > target:
            right = mid
            mid = int((left + right) / 2)
            continue
        if nums[mid - 1] < target:
            left = mid
            mid = int((left + right) / 2)
            continue
        if nums[mid - 1] == target:
            break
    if nums[mid-1] == target:
        print(mid-1)
    else:
        print(-1)
