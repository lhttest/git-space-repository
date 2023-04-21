# range()函数的使用 与切片很像

#直接使用range()函数定义列表/将range转换为list列表
# nember = list(range(9))
# print(nember)
#
# # 使用range()生成指定区间的数
# for i in range(1,8):
#     print(i)
#
# #while 循环
# a = 1
# while a<=100:
#     print(a)
#     a+=1
#
#
#
# c = 1
# sum = 0
# d = 1000
# while c<d:
#     sum+=c
#     c+=1
# print("1到1000的和为 %d" % sum)
#
# # for循环
# b = ['banana','potato','apple','tomato']
# for i in b:
#     if i=="apple":
#         print("结束")
#         break
#     print("其他结果%s"%(i))
# else:
#     print("没找到相关结果")
#
#
# code = int(input("请输入status:"))
# response_code = [100,200,201,204,307,401,403,404,500]
# for i in response_code:
#     if code == i:
#         print("匹配成功")
#         break
# else:
#     print("status无含义")

# 无限循环，可以放在一行，但是只限while后只有一条语句
# i = 1
# while i :print("按ctrl+c结束哦")

# i = 1
# while i<=20:
#     print("%d小于20" %(i))
#     i+=1
# else:
#     print("%d大于20" %(i))

# 奇偶求和

# print(bool(0))
#
# i = 1
# sum = 0
# while i<=100:
#     if not bool(i%2):
#         sum+=i
#     i+=1
# print("偶数的和为",sum)

# 求100-999的水仙花数
# 153=1*1*1+5*5*5+3*3*3
for i in range(100,1000):
    ge = i%10
    shiwei = i//10%10
    baiwei = i//100
    # print(baiwei,shiwei,ge)
    if baiwei**3+shiwei**3+ge**3 == i:
        print("水仙花数为",i)



