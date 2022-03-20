#给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
def reverse_string(nums):
    nums=list(nums)#字符串转列表
    nums.reverse()#列表元素反转
    nums=''.join(nums)#列表转字符串
    nums=nums.split()#字符串切片变列表
    nums.reverse()#列表元素反转
    for i in nums:#列表以字符串格式输出
        print(i,end=' ')
if __name__ == '__main__':
    arr = input("输入一个字符串：")
    reverse_string(arr)
