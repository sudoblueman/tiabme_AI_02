import random
import sys

count = 4
count_A = 4
get_B = 0
get_num_times = 0
user_guess=[]
sy_num=[]
vacant_not_match_user = []
vacant_not_match_sys = []
overlap = 0
cheat_mode = 1
cheat_mode = int(input("是否開啟作弊看答案模式?,是請給1,否則按ENTER繼續")or "0")
print(cheat_mode)
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

user_guess = tuple(user_guess)

#顯示使用者輸入
#print(user_guess)

#sy_num = "6"

sy_num = str(random.randint(0, 9999))

#未滿四位數字要補0
if len(sy_num) < count:
    sy_num = sy_num.zfill(count)
sy_num = tuple(sy_num)
vacant_not_match_user = list(user_guess)




vacant_not_match_sys = list(sy_num)

##print ("vas",vacant_not_match_sys)

#顯示系統隨機產生數值
print("答案sys_num=", sy_num)

while count_A != 0:
    print("get_B0=", get_B)
    get_B = 0
    get_num_times = 0
    count_A = 4
    count = 4
    vacant_not_match_user = list(user_guess)
    vacant_not_match_sys = list(sy_num)
    #mi_dual_num=0
    for x in range(1, count + 1):
        i = 0
        print("count=", count)
        print("x= ", x)
        print("user_guess[x-1] & sy_num=", user_guess[x - 1], sy_num[x - 1])
        if user_guess[x - 1] == sy_num[x - 1]:
            ##print("user_guess[x-1]=", user_guess[x - 1], sy_num[x - 1])
            get_num_times = get_num_times + 1  #找到A加1
            if cheat_mode == 1:
                print("get_num_times= ", get_num_times)
                print("count=", count)
                print("count-get_num_times=?", count - get_num_times)
            count_A = count_A - 1  #找到一個A扣總數
            #符合A的位置換成獨一無二元素
            vacant_not_match_user[x - 1] = '!' + str(x - 1)
            vacant_not_match_sys[x - 1] = '@' + str(x - 1)
            if cheat_mode == 1:            
                print("vacant_not_match_user=", vacant_not_match_user,
                      "vacant_not_match_sys=", vacant_not_match_sys)

    #經過A的置換後的list，要找B
    for k in range(1, count + 1):  
        for i in range(1, count + 1):
            if cheat_mode == 1:          
              print("k,i=", k, i)
            #找到B後，將兩者置換成獨一無二符號，避免下次重複計算
            if vacant_not_match_user[k - 1] == vacant_not_match_sys[i - 1]:
                print("B 出現在第 ", i - 1)

                vacant_not_match_sys[i - 1] = '#' + str(i - 1)
                vacant_not_match_user[k - 1] = '$' + str(k - 1)
                get_B = get_B + 1
            if cheat_mode == 1:
                print('## vacant_not_match_user', vacant_not_match_user)
                print('## 剩下 vacant_not_match_sys= ', vacant_not_match_sys)
            if cheat_mode == 1:
                print("getB,count =", get_B, count_A)
    if cheat_mode == 1:               
        print("get_B=", get_B)
    print("結果是{}A{}B".format(get_num_times, get_B))

    if count_A != 0:
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
    if cheat_mode == 1:                
        print("###答案sys_num=", sy_num)
        print("###get_num_times= ", get_num_times)
        print("###count_A=", count_A)
