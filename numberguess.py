import random
import sys

count = 4
get_B = 0
get_num_times = 0


#檢查輸入
while True:
    try:
        user_guess = input("猜一個0001~9999四位數字")
        if int(user_guess) == False:
            raise Exception("非數字或為0000")
        if len(user_guess) != 4:
            raise Exception("非四位數字")
        break
    except Exception as e:
        print("非數字或非四位數字或輸入0000，請重新檢查輸入: ", e)
    except:
        # sys.exc_info()[0] 就是用來取出except的錯誤訊息的方法
        print("Unexpected error:", sys.exc_info()[0])

user_guess = list(user_guess)

#顯示使用者輸入
#print(user_guess)

sy_num = str(random.randint(0, 9999))

#未滿四位數字要補0
if len(sy_num) < count:
    sy_num = sy_num.zfill(count)
sy_num = list(sy_num)

#顯示系統隨機產生數值
#print("sys_num=", sy_num)

while count != 0:
    print("get_B0=", get_B)
    get_B = 0
    get_num_times = 0
    count = 4
    #mi_dual_num=0
    for x in range(1, count + 1):
        print("x= ", x)
        print("user_guess[x-1]=", user_guess[x - 1], sy_num[x - 1])
        if user_guess[x - 1] == sy_num[x - 1]:
            print("user_guess[x-1]=", user_guess[x - 1], sy_num[x - 1])
            get_num_times = get_num_times + 1
            print("get_num_times= ", get_num_times)
            print("count=", count)
            print("count-get_num_times=?", count - get_num_times)
            count = count - 1
        if user_guess[x - 1] in sy_num[:]:
            #if user_guess[x - 1] in user_guess[x - 2:]:
            #mi_dual_num=mi_dual_num+1
            get_B = get_B + 1
            ##print("getB,count,mi_dual_num =", get_B, count)
    ##print("get_B=", get_B)
    get_B = get_B - get_num_times
    if get_B < 0:
        get_B = 0

    print("結果是{}A{}B".format(get_num_times, get_B))

    if count != 0:
        #重新數字判讀
        while True:
            try:
                user_guess = input("猜一個0001~9999四位數字")
                if int(user_guess) == False:
                    raise Exception("非數字或為0000")
                if len(user_guess) != 4:
                    raise Exception("非四位數字")
                break
            except Exception as e:
                print("非數字或非四位數字或輸入0000，請重新檢查輸入: ", e)
            except:
                # sys.exc_info()[0] 就是用來取出except的錯誤訊息的方法
                print("Unexpected error:", sys.exc_info()[0])
    print("sys_num=", sy_num)
    print("get_num_times= ", get_num_times)
    print("count=", count)
