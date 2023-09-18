import time  
  
def focus_clock(minutes):  
    # 将分钟转换为秒  
    seconds = minutes * 60  
      
    print("专注时钟已启动，倒计时开始！")  
      
    # 倒计时  
    while seconds > 0:  
        print(f"剩余时间：{int(seconds // 60)}分钟{int(seconds % 60)}秒")  
        time.sleep(1)  
        seconds -= 1  
      
    print("时间到！请休息一下吧。")  
  
# 调用函数，设置专注时间为25分钟  
focus_clock(25)
