# 我的第一个 Python 程序
# 运行方法: 打开本文件后, 点右上角的 ▶ 运行按钮

name = input("同学你好! 你叫什么名字? ")
print(f"欢迎你, {name}! 这是你 Python 之旅的第一步。")

# 电气人的浪漫: 算个功率 P = U × I
print("\n--- 顺手验证一下欧姆定律的亲戚: 功率公式 ---")
u = float(input("请输入电压 U (伏特): "))
i = float(input("请输入电流 I (安培): "))
print(f"功率 P = U × I = {u} × {i} = {u * i:.2f} 瓦 (W)")

print("\n搞定! 你已经跑通了人生第一个 Python 程序 🎉")
