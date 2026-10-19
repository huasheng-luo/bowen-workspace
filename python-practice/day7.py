import random
secret=random.randint(1,100)
guess=0
while guess !=secret:
    guess=int(input("猜一个1-100的数字:"))
    if guess> secret:
        print("猜大了")
    elif guess<secret:
        print("猜小了")
print("猜对了！答案就是",secret)
