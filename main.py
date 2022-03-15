arr=input("输入一个一维数组，每个数之间使空格隔开：")
nums=[int(n) for n in arr.split()]#初始化数组,命名为nums
target=int(input("输入一个数："))
left=1
right=len(nums)
mid=int((left+right)/2)
if nums[0]>target:#target超出数组范围，直接返回-1
    print(0)
if nums[right-1]<target:
    print(right)
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
        print(mid)