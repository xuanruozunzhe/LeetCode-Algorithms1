#给你一个下标从 1 开始的整数数组numbers，该数组已按 非递减顺序排列，请你从数组中找出满足相加之和等于目标数target的两个数。
#如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
#以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
#你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
#你所设计的解决方案必须只使用常量级的额外空间。
def split_search(nums,target):#拆分查询函数
    i=0
    j=len(nums)-1
    while nums[i]+nums[j]!=target:#双指针查询
        if nums[i]+nums[j]<target:
            i+=1
        if nums[i]+nums[j]>target:
            j-=1

    result=[]#结果数组，返回要找的两个元素
    result.append(i+1)
    result.append(j+1)
    return result

if __name__ == '__main__':
    arr = input("输入一个一维数组，每个数之间使空格隔开：")
    nums = [int(n) for n in arr.split()]  # 初始化数组,命名为nums
    target = int(input("输入一个目标数："))
    print(split_search(nums,target))