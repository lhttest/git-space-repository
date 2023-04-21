# 实现一个冒泡排序
list = [10,2,3,1,11,9,100,22,35,56,33,5,6]
def bubble_sort():
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j+1],list[j]=list[j],list[j+1]
    return list

result = bubble_sort()
print(result)