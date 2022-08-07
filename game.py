"""用python设计第一个游戏 """


counts =3
while counts>0:
    temp=input("不妨猜一下我现在心里想的是那个数字:")
    guess=int(temp)

    if guess==54188:
        
        print("我的好大儿，")
        print("快叫爸爸！")
        break
    else:
        
        if guess<54188:
            
            print("小了")
        else:
            print("大了")
    couns= counts - 1
print("你个菜鸡o >ω< o")
    
