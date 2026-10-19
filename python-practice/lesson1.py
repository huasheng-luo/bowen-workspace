# 第一课：最小的"猜数字"程序
# 今天不要求你写，只要求你看懂 + 改动几个字

answer = 5                        # ① 把答案偷偷定成 7
guess = input("猜猜我心里的数字: ")   # ② 问你，把你的回答存进 guess
guess = int(guess)                # ③ input 得到的是"文字"，int() 把它变成数字

if guess == answer:               # ④ 如果 guess 和 answer 相等
    print("恭喜你猜对了! 🎉")      # ⑤ 就打印恭喜
else:                             # ⑥ 否则（没猜对）
    print(f"猜错啦，答案是 {answer}")  # ⑦ 公布答案
