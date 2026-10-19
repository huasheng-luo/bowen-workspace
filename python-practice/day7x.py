import random
name=("小艾")
print(f"你好，我是{name}")
name=input("你叫什么名字？")
if name=="孙博文":
    print("你好啊，孙博文，来玩一个猜数游戏吧！")
else:
    print("别来烦我！")
    exit()
secret=random.randint(1,20)
guess=0
n=0
while guess!=secret:
    n=n+1
    guess=int(input("猜一个数"))
    if guess>secret:
        print("猜大了！")
    elif guess<secret:
        print("猜小了！")
print(f"猜对了！答案就是{secret}")
print(f"你一共用了{n}次")
if n<=2:
    print("好运")
elif n>2:
    print("还可以")


