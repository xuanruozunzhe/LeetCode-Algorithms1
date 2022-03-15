right=int(input("请输入一共有几个版本(1~n)："))
num=int(input("请输入第一个错误的版本(1~n)："))
left=1
mid=int((left+right)/2)
while mid!=num:
    if mid>num:
        right=mid
        mid=int((left+right)/2)
        continue
    if mid<num and mid!=right-1:
        left=mid
        mid=int((left+right)/2)
        continue
    if mid==right-1:
        mid=mid+1
        break
print("错误版本号为："+str(mid))