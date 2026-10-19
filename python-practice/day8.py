x=input("请输入本月用电量(度):")
if x<=180:
    print(f"花费了{x}*0.52元")
elif 180<x<=280:
    print(f"花费了{X}*0.57元")
else :
    print(f"花费了{X}*0.82元")
