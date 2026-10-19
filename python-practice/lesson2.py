# 第二课：真正的猜数字游戏！（while 循环 + 随机数）
# 昨天学的零件都在，今天只加 2 个新东西：random 和 while

import random                    # ① 引入"随机"工具包

answer = random.randint(1, 100)  # ② 让电脑随机想一个 1~100 的数
print("我已经想好一个 1~100 的数字，来猜吧!")

while True:                      # ③ 无限循环：反复执行下面缩进的代码
    guess = input("你猜: ")       # ④ 问你
    guess = int(guess)            # ⑤ 文字转数字（昨天学过）

    if guess > answer:            # ⑥ 猜大了
        print("大了，再试试!")     # ⑦
    elif guess < answer:          # ⑧ 猜小了
        print("小了，再试试!")     # ⑨
    else:                         # ⑩ 不大不小 = 猜对了
        print("恭喜你猜对了! 🎉")  # ⑪
        break                     # ⑫ break = 跳出循环，游戏结束
