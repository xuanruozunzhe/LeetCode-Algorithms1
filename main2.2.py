#2.2给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
arr=input("输入一个一维数组，每个数之间使空格隔开：")
nums=[int(n) for n in arr.split()]#初始化数组,命名为nums
target=int(input("输入轮转次数："))
newnums=nums
x=0#计数器
while x<target:#轮转次数
    newnums.insert(0,nums[len(nums)-1])#数组最后一项添加到轮转后数组第一项
    del nums[len(nums)-1]#删除最后一项
    x+=1
print(newnums)
