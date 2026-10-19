print("日报机器人上线")
name=input("你叫什么名字？")
print(f"hi,{name}")
time=int(input("你今天学习了多久？(min)"))
if time>=60:
  print("狠人")
elif time>=30:
  print("不错")
else :
  print("明天再来")
guess="要"
x=input("还要再报一天吗(要/不要)?")
while x==guess:
  print("明天见")
  x=input("还要再报一天吗(要/不要)?")
else :
  print("好吧")