#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#请注意 ，必须在不复制数组的情况下原地对数组进行操作。
def remove_zero(nums):
    for i in nums:
        if i==0:
            nums.append(i)
            nums.remove(i)
    return nums

if __name__ == '__main__':
    arr = input("输入一个一维数组，每个数之间使空格隔开：")
    nums = [int(n) for n in arr.split()]  # 初始化数组,命名为nums
    print(remove_zero(nums))
