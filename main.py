#编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
#不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题
def reverse_string(nums):
    i=0#计数器
    while i<len(nums)/2:#左右两端字符对调，左二右二对调，以此类推执行数组长度的一半次
        x=nums[i]
        nums[i]=nums[len(nums)-i-1]
        nums[len(nums)-i-1]=x
        i+=1
    return nums
if __name__ == '__main__':
    arr = input("输入一个一维字符数组，每个字符之间使空格隔开：")
    nums = [n for n in arr.split()]  # 初始化数组,命名为nums
    print(reverse_string(nums))