"""
项目名称：RPSLS游戏
作者：杨敬升
"""
import random
y=random.randint(0,4)

# def RPSLS(x):
#     if x==0 y==1  or  y==2 :
#         print('您赢了1')
#     if x == 0   y == 3 or y==4:
#             print('您输了2')
#     if x==1 and y==3 or y==2 :
#         print('您赢了3')
#     if x == 1 and y == 4 or y==0:
#               print('您输了4')
#     if x==2 and y==4 or y==3 :
#         print('您赢了3')
#     if x == 2 and y == 1 or y==0:
#               print('您输了4')
#     if x==3 and y==0 or y==4 :
#        print('你赢了7')
#     if x == 3 and y == 1 or y==2:
#           print('您输了8')
#     if x==4 and y==0 or y==1 :
#         print('您赢了9')
#     if x == 4 and y == 3 or y==2:
#            print('您输了10')
#     return x
# print('请猜拳')
# a=input()
# result=RPSLS(a)
print('请猜拳')
x=int(input())
if x==0 or y==0 :
    ind='rock 石头'
if x==1 or y==1:
    ind=('Spock 史波克')
if x==2 or y==2:
    ind=('paper 布')
if x==3 or y==3 :
    ind=('lizard 蜥蜴 ')
if x==4 or y==4 :
    ind=('scissors 剪刀')

while x==0:
    if y==1 or y==2 :
        print('您赢了')
    if y==3 or y==4:
        print('您输了')
    if x==y:
        print('平局')

    print(str(x))
    print(str(y))
    break
# while x==1:
#     if y==3 or y==2 :
#         print('您赢了')
#     if y==0 or y==4:
#         print('您输了')
#     if x==y:
#         print('平局')
#     print(1)
#     print(y)
#     break
# while x==2:
#     if y==3 or y==4 :
#         print('您赢了')
#     if y==0 or y==1:
#         print('您输了')
#     if x==y:
#         print('平局')
#     print(2)
#     print(y)
#     break
# while x==3:
#     if y==0 or y==4 :
#         print('您赢了')
#     if y==1 or y==2:
#         print('您输了')
#     if x==y:
#         print('平局')
#     print(3)
#     print(y)
#     break
# while x==4:
#     if y==0 or y==1 :
#         print('您赢了')
#     if y==3 or y==2:
#         print('您输了')
#     if x==y:
#         print('平局')
#     print(4)
#     print(y)
#     break
while x!=0 or 1 or 2 or 3 or 4 :
    print('Error: No Correct Name')
    break