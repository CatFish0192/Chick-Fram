# :coding:utf-8
# 打包代码：pyinstaller --paths D:\code_storehouse\Python3.11.5\Lib\site-packages\colorama -F XJZY.py
"""
 ·1.0：初始版本
 ·1.1：BUG修复
 ·1.2：玩法升级+BUG修复
 ·1.3：玩法升级+BUG修复+注释修改
 ·1.4：BUG修复+注释修改
 ·1.5：玩法升级+BUG修复+注释修改
 ·1.6：玩法升级+注释修改

 ·2.0：数据保存功能+BUG修复+注释修改
 ·2.0.1：玩法升级+BUG修复
 ·2.0.2：玩法升级+注释修改
 ·2.1：玩法升级+BUG修复
 ·2.2：BUG修复+彩色字体
 ·2.3：数据保存功能2+注释修改
 ·2.3（bug）：BUG修复
 ·2.4：BUG修复
 ·2.5：数据保存功能3
 ·2.6：菜单1.1+BUG修复
 ·2.7：进度条+成就系统+BUG修复（当前）

 ·状态：更新中······
 
 ·XJZY 1x只更新到1.6版本
 ·XJZY 2x增加了数据保存、彩色字体功能，目前正在更新

 ·开发：白猫
 ·调试：橘猫、白水（电脑不见了，可能是被马桶冲走了）
 ·邮箱：白猫：3589326704@qq.com
 ·网址：https://gitee.com/bxl24563/XJZY
 ·备用网址：https://gitcode.com/bxl24563/XJZY
 ·联系：
      Bilibili：白猫：白猫猫猫猫猫猫猫儿、橘猫：橘猫猫猫猫猫猫猫儿、白水：白水Whusacr
"""
def prco(text, color=3):
    """
    PRint COlor
    颜色模块
    """
    from colorama import init, Fore  # ←导入颜色模块(prco的依赖)
    init() #初始化colorama

    if color == 1:
        print(Fore.LIGHTRED_EX + text + Fore.RESET) #red:坏、失败、错误
    elif color == 2:
        print(Fore.CYAN + text + Fore.RESET) #cyan:菜单
    elif color == 3:
        print(Fore.LIGHTWHITE_EX + text + Fore.RESET) #white:信息
    elif color == 4:
        print(Fore.LIGHTGREEN_EX + text + Fore.RESET) #green:好、成功
    elif color == 5:
        print(Fore.YELLOW + text + Fore.RESET) #yellow:提示、旁白
    elif color == 6:
        print(Fore.LIGHTBLUE_EX + text + Fore.RESET) #blue:选择

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='='):
    """
    进度条（感谢国外佚名大佬提供）
    """
    from colorama import init, Fore
    init() #初始化colorama

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))  
    filledLength = int(length * iteration // total)
    bar = (Fore.LIGHTGREEN_EX + fill + Fore.RESET) * filledLength + (Fore.LIGHTWHITE_EX + fill + Fore.RESET) * (length - filledLength)  
    
    print(f'\r{prefix} [{bar}] {percent}% {suffix}', end="\r")
    
    if iteration == total:
        print("", end="\r")

def wjf(wdate=None):
    """Write Json File"""
    import json
    import os
    if os.name == "nt":
        username = os.getlogin()+"\\XJZY.json"
        userpath = os.path.join("C:\\Users\\",username)
    else:
        userpath = ".XJZY.json"

    if wdate == None:
        date = {
                    "date":{
                        "Gold":5,
                        "Stealth_potions":0,
                        "How_much_feed_the_chicks_ate_in_total":10,
                        "Accelerator_card":0,
                        "How_much_corn_is_there_in_total":0,
                        "How_many_corn_seeds_there_were":0
                    },
                    "accomplishment":{
                        "haveAccomplishment":False,
                        "mmod":False,
                        "pope":False,
                        "ripe":False
                    }
               }
        json_date = json.dumps(date, indent=4)
        with open(userpath, "w+") as json_file:
            json_file.write(json_date)
    else:
        date = wdate
        json_date = json.dumps(date, indent=4)
        with open(userpath, "w+") as json_file:
            json_file.write(json_date)

def rjf():
    """Read Json File"""
    import json
    import os
    if os.name == "nt":
        username = os.getlogin()+"\\XJZY.json"
        userpath = os.path.join("C:\\Users\\",username)
    else:
        userpath = ".XJZY.json"

    with open(userpath, "r") as json_file:
        json_date = json.loads(json_file.read())
        return json_date

def XJZY(): #主函数
    from colorama import init, Fore  # ←导入颜色模块(prco的依赖)
    import os as o  # ←导入系统模块
    import random as r  # ←导入随机数模块
    import re as e  # ←导入格式化字符模块
    import time as t  # ←导入时间模块
    import sqlite3 # ←导入数据库模块

    init() #←初始化colorama

    # ↓声明不保存到数据库的变量,从而预防UnboundLocalError错误
    about = """
 ·1.0：初始版本
 ·1.1：BUG修复
 ·1.2：玩法升级+BUG修复
 ·1.3：玩法升级+BUG修复+注释修改
 ·1.4：BUG修复+注释修改
 ·1.5：玩法升级+BUG修复+注释修改
 ·1.6：玩法升级+注释修改

 ·2.0：数据保存功能+BUG修复+注释修改
 ·2.0.1：玩法升级+BUG修复
 ·2.0.2：玩法升级+注释修改
 ·2.1：玩法升级+BUG修复
 ·2.2：BUG修复+彩色字体
 ·2.3：数据保存功能2+注释修改
 ·2.3（bug）：BUG修复
 ·2.4：BUG修复
 ·2.5：数据保存功能3
 ·2.6：菜单1.1+BUG修复
 ·2.7：进度条+成就系统+BUG修复（当前）

 ·状态：更新中······
 
 ·XJZY 1x只更新到1.6版本
 ·XJZY 2x增加了数据保存、彩色字体功能，目前正在更新

 ·开发：白猫
 ·调试：橘猫、白水（电脑不见了，可能是被马桶冲走了）
 ·邮箱：白猫：3589326704@qq.com
 ·网址：https://gitee.com/bxl24563/XJZY
 ·备用网址：https://gitcode.com/bxl24563/XJZY
 ·联系：
      Bilibili：白猫：白猫猫猫猫猫猫猫儿、橘猫：橘猫猫猫猫猫猫猫儿、白水：白水Whusacr
"""

    menu = """
╭─────────────────────────╮
│        小鸡庄园         │
├─────────────────────────┤
│1.偷吃                   │
│2.种玉米                 │
│3.商店                   │
│4.仓库                   │
│5.关于                   │
├─────────────────────────┤
│0.退出                   │
╰─────────────────────────╯
           """                       #对，你没看错，就是这样（因为某些奇奇怪怪的字符问题）
    shopmenu = """
╭─────────────────────────╮
│          商店           │
├─────────────────────────┤
│1.买加速卡               │
│2.卖饲料                 │
│3.买种子                 │
│4.卖玉米                 │
│5.卖隐身药剂             │
├─────────────────────────┤
│0.退出                   │
╰─────────────────────────╯
           """
    debugmenu = """
╭─────────────────────────╮
│          debug          │
├─────────────────────────┤
│1.关闭数据保存           │
│2.报错                   │
├─────────────────────────┤
│0.退出                   │
╰─────────────────────────╯
    """
    menuAndAccomplishment = """
╭─────────────────────────╮
│        小鸡庄园         │
├─────────────────────────┤
│1.偷吃                   │
│2.种玉米                 │
│3.商店                   │
│4.仓库                   │
│5.成就                   │
│6.关于                   │
├─────────────────────────┤
│0.退出                   │
╰─────────────────────────╯
           """

    What_to_do = ""
    Whether_to_use_an_accelerator_card = ""
    Manor_Lord_1 = ""
    How_many_minutes_were_eaten = 0
    How_many_grams_were_eaten = 0
    How_many_acceleration_cards_to_buy = 0
    How_much_feed_to_buy = 0
    Why = ""
    How_much_to_plant = 0
    How_many_corn_seeds_to_buy = 0
    How_much_corn = 0
    Already_treated = None
    Whether_to_be_beaten_or_not = None
    plead = None
    Whether_to_use_stealth_potions = None
    How_much_stealth_potion_to_buy = None
    Stealing_probability = ["T", "F", "F", "F", "F"]
    Whether_or_not_to_steal_it = ""
    Data_Logging_one = ""
    Data_Logging_two = ""
    if o.name == "nt":
        username = o.getlogin()+"\\XJZY.json"
        userpath = o.path.join("C:\\Users\\",username)
    else:
        userpath = ".XJZY.json"
    savedate = True

    haveAccomplishment = False
    mmod = False
    pope = False
    ripe = False

    wdate = {}
    if not o.path.exists("XJZY.db"):
        #新手引导
        debug = input("欢迎来到小鸡庄园")
        if debug == "db": #调试模式
            prco(debugmenu, 2)
            opendebug = input(Fore.BLUE + "请选择开启项目：")
            if opendebug == "1":
                savedate = False
                Gold = 5
                Stealth_potions = 0
                How_much_feed_the_chicks_ate_in_total = 10
                Accelerator_card = 0
                How_much_corn_is_there_in_total = 0
                How_many_corn_seeds_there_were = 0
                prco("已开启", 4)
                t.sleep(1)
            elif opendebug == "2":
                print(我是错误代码) #这是一段错误代码
            elif opendebug == 0:
                pass
        else:
            input("这里就是我们的庄园。看，那些分别是AA、BB、CC、DD的庄园")
            input("我们可以去那里偷一点饲料回来；当然我们也要小心被偷吃")
            input("看到那个大房子了吗？那个就是商店，你可以去那里做一些卖买")
            input("喏，这些送给你(5个金币、10克饲料)")
            input("好了，我就不打扰了，再见！")
            input("(老人离开了这里······)")
            t.sleep(1)
        if savedate:
            json_Gold = 5
            json_Stealth_potions = 0
            json_How_much_feed_the_chicks_ate_in_total = 10
            json_Accelerator_card = 0
            json_How_much_corn_is_there_in_total = 0
            json_How_many_corn_seeds_there_were = 0
            wjf()
            #初始化
            conn = sqlite3.connect("XJZY.db") #创建数据库文件
            cursor = conn.cursor() #创建游标
            cursor.execute("create table xjzy (id int(1) primary key, Gold float, Stealth_potions int,How_much_feed_the_chicks_ate_in_total int, Accelerator_card int,How_much_corn_is_there_in_total int,How_many_corn_seeds_there_were int)") #数据库结构
            cursor.execute("insert into xjzy (id, Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were) values (1, 0, 0, 0, 0, 0, 0)") #给数据库赋值
        Gold = 5
        Stealth_potions = 0
        How_much_feed_the_chicks_ate_in_total = 10
        Accelerator_card = 0
        How_much_corn_is_there_in_total = 0
        How_many_corn_seeds_there_were = 0
    else:
        prco("版本：2.7")
        prco("通知：进度条、成就系统还有一大堆乱七八糟的更新/BUG修复")
        conn = sqlite3.connect("XJZY.db") #选择数据库文件
        cursor = conn.cursor()
        cursor.execute("select * from xjzy") #执行SQL语句
        xjzydbresult = cursor.fetchone() #查找全部的数据
        if o.path.exists(userpath):
            date = rjf()
            json_Gold = date["date"]["Gold"]
            json_Stealth_potions = date["date"]["Stealth_potions"]
            json_How_much_feed_the_chicks_ate_in_total = date["date"]["How_much_feed_the_chicks_ate_in_total"]
            json_Accelerator_card = date["date"]["Accelerator_card"]
            json_How_much_corn_is_there_in_total = date["date"]["How_much_corn_is_there_in_total"]
            json_How_many_corn_seeds_there_were = date["date"]["How_many_corn_seeds_there_were"]

            haveAccomplishment = date["accomplishment"]["haveAccomplishment"]
            mmod = date["accomplishment"]["mmod"]
            pope = date["accomplishment"]["pope"]
            ripe = date["accomplishment"]["ripe"]

            json_Gold = float(json_Gold)
            json_Stealth_potions = int(json_Stealth_potions)
            json_How_much_feed_the_chicks_ate_in_total = int(json_How_much_feed_the_chicks_ate_in_total)
            json_Accelerator_card = int(json_Accelerator_card)
            json_How_much_corn_is_there_in_total = int(json_How_much_corn_is_there_in_total)
            json_How_many_corn_seeds_there_were = int(json_How_many_corn_seeds_there_were)
        else:
            Gold = xjzydbresult[1]
            Stealth_potions = xjzydbresult[2]
            How_much_feed_the_chicks_ate_in_total = xjzydbresult[3]
            Accelerator_card = xjzydbresult[4]
            How_much_corn_is_there_in_total = xjzydbresult[5]
            How_many_corn_seeds_there_were = xjzydbresult[6]

            json_Gold = Gold
            json_Stealth_potions = Stealth_potions
            json_How_much_feed_the_chicks_ate_in_total = How_much_feed_the_chicks_ate_in_total
            json_Accelerator_card = Accelerator_card
            json_How_much_corn_is_there_in_total = How_much_corn_is_there_in_total
            json_How_many_corn_seeds_there_were = How_many_corn_seeds_there_were
        if xjzydbresult != None: #数据库为空
            # xjzydbresult[0]是id字段
            Gold = xjzydbresult[1]
            Stealth_potions = xjzydbresult[2]
            How_much_feed_the_chicks_ate_in_total = xjzydbresult[3]
            Accelerator_card = xjzydbresult[4]
            How_much_corn_is_there_in_total = xjzydbresult[5]
            How_many_corn_seeds_there_were = xjzydbresult[6]
            if json_Gold != Gold or json_Stealth_potions != Stealth_potions or json_How_much_feed_the_chicks_ate_in_total != How_much_feed_the_chicks_ate_in_total or json_Accelerator_card != Accelerator_card or json_How_much_corn_is_there_in_total != How_much_corn_is_there_in_total or json_How_many_corn_seeds_there_were != How_many_corn_seeds_there_were:
                Gold = json_Gold
                Stealth_potions = json_Stealth_potions
                How_much_feed_the_chicks_ate_in_total = json_How_much_feed_the_chicks_ate_in_total
                Accelerator_card = json_Accelerator_card
                How_much_corn_is_there_in_total = json_How_much_corn_is_there_in_total
                How_many_corn_seeds_there_were = json_How_many_corn_seeds_there_were
                prco("不要再偷鸡了，这样不会有好下场的-.-",1)
                t.sleep(1)
                if mmod == False:
                    print("获得成就[" + Fore.LIGHTGREEN_EX + "偷鸡贼" + Fore.RESET + "]")
                    haveAccomplishment = True
                    mmod = True
                t.sleep(1)
        else:
            Gold = 5
            Stealth_potions = 0
            How_much_feed_the_chicks_ate_in_total = 10
            Accelerator_card = 0
            How_much_corn_is_there_in_total = 0
            How_many_corn_seeds_there_were = 0

    # ↓死循环
    while True:
        if ripe == False and Gold >= 100:
            print("获得成就[" + Fore.LIGHTGREEN_EX + "大富翁" + Fore.RESET + "]")
            haveAccomplishment = True
            ripe = True
            t.sleep(1)
        if What_to_do == "你好":
            if pope == False:
                prco("你好，有什么事吗？")
                t.sleep(0.5)
                print("获得成就[" + Fore.LIGHTGREEN_EX + "礼貌问候" + Fore.RESET + "]")
                haveAccomplishment = True
                pope = True
                t.sleep(0.5)
            else:
                prco("你好，有什么事吗？")
                t.sleep(1)
        if savedate:
            wdate = {
                        "date":{
                            "Gold":Gold,
                            "Stealth_potions":Stealth_potions,
                            "How_much_feed_the_chicks_ate_in_total":How_much_feed_the_chicks_ate_in_total,
                            "Accelerator_card":Accelerator_card,
                            "How_much_corn_is_there_in_total":How_much_corn_is_there_in_total,
                            "How_many_corn_seeds_there_were":How_many_corn_seeds_there_were
                        },
                        "accomplishment":{
                            "haveAccomplishment":haveAccomplishment,
                            "mmod":mmod,
                            "pope":pope,
                            "ripe":ripe
                        }
                    }
            wjf(wdate)

            # ↓保存数据
            cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were))
            conn.commit() #提交事务

        Whether_or_not_to_steal_it = r.choice(Stealing_probability)
        if Whether_or_not_to_steal_it == "T" and How_much_feed_the_chicks_ate_in_total >= 20:
            Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
            Manor_Lord_1 = r.choice(Manor_Lord_1)
            How_many_minutes_were_eaten = r.randint(15, 30)
            if 15 <= How_many_minutes_were_eaten < 20:
                How_many_grams_were_eaten = 10
            elif 20 < How_many_minutes_were_eaten < 25:
                How_many_grams_were_eaten = 15
            else:
                How_many_grams_were_eaten = 20
            t.sleep(0.5)
            prco("\n")
            prco(
                str(Manor_Lord_1) +
                "的小鸡在你的的庄园偷吃了" +
                str(How_many_minutes_were_eaten) +
                "分钟，吃掉了" +
                str(How_many_grams_were_eaten) +
                "克饲料"
            , 1)
            How_much_feed_the_chicks_ate_in_total -= How_many_grams_were_eaten
        t.sleep(1)
        prco("\n" + "─"*50, 3)
        if haveAccomplishment == False:
            prco(menu, 2) #输出菜单
        else:
            prco(menuAndAccomplishment, 2) #输出菜单
        What_to_do = input(Fore.BLUE + "你要干什么呢？" + Fore.RESET)
        if What_to_do == "1":
            if Accelerator_card > 0:
                prco("1、要", 2)
                prco("2、不要", 2)
                t.sleep(0.5)
                Whether_to_use_an_accelerator_card = input(Fore.BLUE + "你要用加速卡吗？" + Fore.RESET)
            else:
                Whether_to_use_an_accelerator_card = "2"
            if Stealth_potions > 0:
                prco("1、要", 2)
                prco("2、不要", 2)
                t.sleep(0.5)
                Whether_to_use_stealth_potions = input(Fore.BLUE + "你要用隐身药剂吗？" + Fore.RESET)
            else:
                Whether_to_use_stealth_potions = "2"

            if (
                Whether_to_use_an_accelerator_card == "1"
                and Whether_to_use_stealth_potions == "1"
            ):
                if Accelerator_card > 0 and Stealth_potions > 0:
                    Accelerator_card -= 1
                    Stealth_potions -= 1
                    prco("你使用了1张加速卡和1瓶隐身药剂，小鸡撸起袖子开始双手吃饲料，进食速度大大加快", 4)
                    Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
                    Manor_Lord_1 = r.choice(Manor_Lord_1)
                    How_many_minutes_were_eaten = r.randint(15, 30)
                    if 15 <= How_many_minutes_were_eaten < 20:
                        How_many_grams_were_eaten = 10
                    elif 20 < How_many_minutes_were_eaten < 25:
                        How_many_grams_were_eaten = 15
                    else:
                        How_many_grams_were_eaten = 20
                    for i in range(100):
                        print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                        t.sleep(How_many_minutes_were_eaten/1000)

                    prco(
                        "你的小鸡在" +
                        str(Manor_Lord_1) +
                        "的庄园偷吃了" +
                        str(How_many_minutes_were_eaten) +
                        "分钟，吃掉了" +
                        str(How_many_grams_were_eaten) +
                        "克饲料，就被" +
                        str(Manor_Lord_1) +
                        "赶了回来，因为你使用了隐身药剂，所以你的小鸡没被" +
                        str(Manor_Lord_1) +
                        "打到"
                    , 4)
                    How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                    prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)
                else:
                    prco("你还没有辅助道具哦！快去商店购买吧！", 5)
            if (
                Whether_to_use_an_accelerator_card == "2"
                and Whether_to_use_stealth_potions == "2"
            ):
                Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
                Manor_Lord_1 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 5
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 10
                else:
                    How_many_grams_were_eaten = 15
                Whether_to_be_beaten_or_not = ["T", "T", "F", "F", "F"]
                Whether_to_be_beaten_or_not = r.choice(Whether_to_be_beaten_or_not)
                if Whether_to_be_beaten_or_not == "F":
                    for i in range(100):
                        print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                        t.sleep(How_many_minutes_were_eaten/1000)
                    prco(
                        "你的小鸡在" +
                        str(Manor_Lord_1) +
                        "的庄园偷吃了" +
                        str(How_many_minutes_were_eaten) +
                        "分钟，吃掉了" +
                        str(How_many_grams_were_eaten) +
                        "克饲料，就被" +
                        str(Manor_Lord_1) +
                        "赶了回来，你的小鸡很幸运，没有被" +
                        str(Manor_Lord_1) +
                        "打到"
                    , 4)
                    How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                    prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)
                else:
                    if How_many_grams_were_eaten >= 10:
                        How_much_feed_the_chicks_ate_in_total += (
                            How_many_grams_were_eaten
                        )
                        How_much_feed_the_chicks_ate_in_total -= 10
                        Already_treated = "T"
                        plead = "F"
                    else:
                        Already_treated = "F"
                    if How_much_feed_the_chicks_ate_in_total >= 10:
                        if Already_treated == "F":
                            How_much_feed_the_chicks_ate_in_total += (
                                How_many_grams_were_eaten
                            )
                            How_much_feed_the_chicks_ate_in_total -= 10
                        plead = "F"
                    if (
                        How_much_feed_the_chicks_ate_in_total < 10
                        and How_many_grams_were_eaten < 10
                    ):
                        How_much_feed_the_chicks_ate_in_total += (
                            How_many_grams_were_eaten
                        )
                        if How_much_feed_the_chicks_ate_in_total >= 10:
                            How_much_feed_the_chicks_ate_in_total -= 10
                            plead = "F"
                        #if plead != "F":
                        #    plead = "T"
                    if plead == "T":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)

                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_1) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_1) +
                            "赶了回来，倒霉的是：你的小鸡被" +
                            str(Manor_Lord_1) +
                            "打到了。因为你没有足够的饲料，所以医生免费把你的小鸡治好了"
                        , 4)
                    if plead == "F":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)

                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_1) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_1) +
                            "赶了回来，倒霉的是：你的小鸡被" +
                            str(Manor_Lord_1) +
                            "打到了。你给了医生10克饲料，医生把你的小鸡治好了"
                        , 1)
                        prco("饲料-10", 1)
            if (
                Whether_to_use_an_accelerator_card == "1"
                and Whether_to_use_stealth_potions == "2"
            ):
                if Accelerator_card > 0:
                    Accelerator_card -= 1
                    prco("你使用了1张加速卡，小鸡撸起袖子开始双手吃饲料，进食速度大大加快", 4)
                    Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
                    Manor_Lord_1 = r.choice(Manor_Lord_1)
                    How_many_minutes_were_eaten = r.randint(15, 30)
                    if 15 <= How_many_minutes_were_eaten < 20:
                        How_many_grams_were_eaten = 10
                    elif 20 < How_many_minutes_were_eaten < 25:
                        How_many_grams_were_eaten = 15
                    else:
                        How_many_grams_were_eaten = 20
                    t.sleep(0.5)
                    Whether_to_be_beaten_or_not = ["T", "T", "F", "F", "F"]
                    Whether_to_be_beaten_or_not = r.choice(Whether_to_be_beaten_or_not)
                    if Whether_to_be_beaten_or_not == "F":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)

                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_1) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_1) +
                            "赶了回来，你的小鸡很幸运，没有被" +
                            str(Manor_Lord_1) +
                            "打到"
                        , 4)
                        How_much_feed_the_chicks_ate_in_total += (
                            How_many_grams_were_eaten
                        )
                        prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)
                    else:
                        if How_many_grams_were_eaten >= 10:
                            How_much_feed_the_chicks_ate_in_total += (
                                How_many_grams_were_eaten
                            )
                            How_much_feed_the_chicks_ate_in_total -= 10
                            Already_treated = "T"
                            plead = "F"
                        else:
                            Already_treated = "F"
                        if How_much_feed_the_chicks_ate_in_total >= 10:
                            if Already_treated == "F":
                                How_much_feed_the_chicks_ate_in_total += (
                                    How_many_grams_were_eaten
                                )
                                How_much_feed_the_chicks_ate_in_total -= 10
                            plead = "F"
                        if (
                            How_much_feed_the_chicks_ate_in_total < 10
                            and How_many_grams_were_eaten < 10
                        ):
                            How_much_feed_the_chicks_ate_in_total += (
                                How_many_grams_were_eaten
                            )
                            if How_much_feed_the_chicks_ate_in_total >= 10:
                                How_much_feed_the_chicks_ate_in_total -= 10
                                plead = "F"
                            plead = "T"
                        if plead == "T":
                            for i in range(100):
                                print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                                t.sleep(How_many_minutes_were_eaten/1000)

                            prco(
                                "你的小鸡在" +
                                str(Manor_Lord_1) +
                                "的庄园偷吃了" +
                                str(How_many_minutes_were_eaten) +
                                "分钟，吃掉了" +
                                str(How_many_grams_were_eaten) +
                                "克饲料，就被" +
                                str(Manor_Lord_1) +
                                "赶了回来，倒霉的是：你的小鸡被" +
                                str(Manor_Lord_1) +
                                "打了。因为你没有饲料，所以医生免费把你的小鸡治好了"
                            , 4)
                        if plead == "F":
                            for i in range(100):
                                print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                                t.sleep(How_many_minutes_were_eaten/1000)

                            prco(
                                "你的小鸡在" +
                                str(Manor_Lord_1) +
                                "的庄园偷吃了" +
                                str(How_many_minutes_were_eaten) +
                                "分钟，吃掉了" +
                                str(How_many_grams_were_eaten) +
                                "克饲料，就被" +
                                str(Manor_Lord_1) +
                                "赶了回来，倒霉的是：你的小鸡被" +
                                str(Manor_Lord_1) +
                                "打了。你给了医生10克饲料，医生把你的小鸡治好了"
                            , 1)
                            prco("饲料-10", 1)
                else:
                    prco("你还没有加速卡哦！快去商店购买吧！", 5)
            if (
                Whether_to_use_an_accelerator_card == "2"
                and Whether_to_use_stealth_potions == "1"
            ):
                prco("你使用了1瓶隐身药剂，小鸡隐身了")
                Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
                Manor_Lord_1 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 5
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 10
                else:
                    How_many_grams_were_eaten = 15
                for i in range(100):
                    print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                    t.sleep(How_many_minutes_were_eaten/1000)

                prco(
                    "你的小鸡在" +
                    str(Manor_Lord_1) +
                    "的庄园偷吃了" +
                    str(How_many_minutes_were_eaten) +
                    "分钟，吃掉了" +
                    str(How_many_grams_were_eaten) +
                    "克饲料，就被" +
                    str(Manor_Lord_1) +
                    "赶了回来，因为你使用了隐身药剂，所以你的小鸡没被" +
                    str(Manor_Lord_1) +
                    "打到"
                , 4)
                How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)
        elif What_to_do == "2":
            if How_many_corn_seeds_there_were == 0:
                prco("你还没有玉米的种子呢！快去购买吧！", 1)
            else:
                prco("你有" + str(How_many_corn_seeds_there_were) + "个种子", 5)
                try:
                    How_much_to_plant = int(input(Fore.BLUE + "你要种多少玉米？" + Fore.RESET))
                except ValueError:
                    prco("额，看来你不想种玉米", 1)
                # ↓没有发生错误时执行else语句
                else:
                    if How_much_to_plant > How_many_corn_seeds_there_were != 0:
                        prco("你还没有那么多种子呢！快去买吧！", 5)
                    elif How_much_to_plant > How_many_corn_seeds_there_were == 0:
                        prco("你还没有玉米种子呢！快去买吧！", 5)
                    elif How_much_to_plant <= How_many_corn_seeds_there_were and How_much_to_plant != 0:
                        How_many_corn_seeds_there_were -= How_much_to_plant
                        if How_much_to_plant < 10:
                            Corn_that_grows = r.randint(0, How_much_to_plant)
                        else:
                            Corn_that_grows = r.randint(How_much_to_plant-10, How_much_to_plant)
                        How_much_corn_is_there_in_total += Corn_that_grows

                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix='播种中:', length=25)
                            t.sleep(How_much_to_plant/1000)

                        prco("你种了" + str(How_much_to_plant) + "个玉米种子,长出来了" + str(Corn_that_grows) + "个",4)
                    elif How_much_to_plant == 0:
                        prco("你去地里逛了一圈，什么都没干")
        elif What_to_do == "3":
            prco(shopmenu, 2)
            Why = input(Fore.BLUE + "你要做什么买卖？")
            if Why == "1":
                prco("1张加速卡=1个金币", 5)
                prco("你现在一共有" + str(Gold) + "个金币", 5)
                try:
                    How_many_acceleration_cards_to_buy = int(input(Fore.BLUE + "你要买多少加速卡："))
                except ValueError:
                    prco("老板把你赶了出去", 1)
                else:
                    if int(How_many_acceleration_cards_to_buy) > int(Gold):
                        if Gold == 0:
                            prco("你现在没有金币哦！", 1)
                        else:
                            prco("你的金币还不够哦！你现在只有" + str(Gold) + "个金币", 1)
                    elif int(How_many_acceleration_cards_to_buy) < 0:
                        prco("老板把你赶了出去", 1)
                    elif int(How_many_acceleration_cards_to_buy) <= int(Gold) and How_many_acceleration_cards_to_buy != 0:
                        Accelerator_card += int(How_many_acceleration_cards_to_buy)
                        Gold -= int(How_many_acceleration_cards_to_buy)
                        prco("你获得了" + str(How_many_acceleration_cards_to_buy) + "个加速卡", 4)
                    elif How_many_acceleration_cards_to_buy == 0:
                        prco("你去商店逛了一圈，什么都没买")
            elif Why == "2":
                prco("5克饲料=1个金币", 5)
                prco("你有" + str(How_much_feed_the_chicks_ate_in_total) + "克饲料", 5)
                try:
                    How_much_feed_to_buy = int(input(Fore.BLUE + "你要卖多少饲料？"))
                except ValueError:
                    prco("客人不知道你要干嘛，你什么都没卖出去", 1)
                else:
                    if int(How_much_feed_to_buy) < 0:
                        prco("老板把你赶了出去", 1)
                    elif How_much_feed_to_buy != 0:
                        if How_much_feed_the_chicks_ate_in_total >= How_much_feed_to_buy:
                            How_much_feed_to_buy -= How_much_feed_to_buy % 5
                            How_much_feed_the_chicks_ate_in_total -= int(
                                How_much_feed_to_buy
                            )
                            Gold += int(How_much_feed_to_buy) / 5
                            prco("你获得了了" + str(int(How_much_feed_to_buy) / 5) + "个金币", 4)
                        else:
                            prco("你还没有那么多饲料！", 1)
                    else:
                        prco("你去商店逛了一圈，什么都没卖", 3)
            elif Why == "3":
                prco("你有" + str(Gold) + "个金币", 5)
                prco("1个玉米种子=5个金币", 5)
                try:
                    How_many_corn_seeds_to_buy = int(input(Fore.BLUE + "你要买多少玉米种子？"))
                except ValueError:
                    prco("老板把你赶了出去", 1)
                else:
                    if int(How_many_corn_seeds_to_buy) < 0:
                        prco("老板把你赶了出去", 1)
                    elif How_many_corn_seeds_to_buy != 0:
                        if (How_many_corn_seeds_to_buy * 5) > Gold:
                            prco("你的金币还不够哦！", 1)
                        elif (How_many_corn_seeds_to_buy * 5) <= Gold:
                            Gold -= How_many_corn_seeds_to_buy * 5
                            How_many_corn_seeds_there_were += How_many_corn_seeds_to_buy
                            prco("购买成功！", 4)
                            prco("你获得了" + str(How_many_corn_seeds_to_buy) + "个玉米种子", 4)
                    else:
                        prco("你去商店逛了一圈，什么都没买", 3)
            elif Why == "4":
                prco("你有" + str(How_much_corn_is_there_in_total) + "个玉米", 5)
                prco("1个玉米=10个金币", 5)
                try:
                    How_much_corn = int(input(Fore.BLUE + "你要卖多少玉米？"))
                except ValueError:
                    prco("客人不知道你要干嘛，你什么都没卖出去", 1)
                else:
                    if int(How_much_corn) < 0:
                        prco("老板把你赶了出去", 1)
                    elif How_much_corn == 0:
                        prco("你去商店逛了一圈，什么都没卖", 3)
                    elif How_much_corn_is_there_in_total < How_much_corn:
                        prco("你还没有那么多玉米哦！", 1)
                    elif How_much_corn_is_there_in_total >= How_much_corn:
                        Gold += How_much_corn * 10
                        How_much_corn_is_there_in_total -= How_much_corn
                        prco("你获得了" + str(How_much_corn * 10) + "个金币", 4)
            elif Why == "5":
                prco("你有" + str(Gold) + "个金币", 5)
                prco("1瓶隐身药剂=15个金币", 5)
                try:
                    How_much_stealth_potion_to_buy = int(input(Fore.BLUE + "你要买多少隐身药剂？"))
                except ValueError:
                    prco("老板把你赶了出去", 1)
                else:
                    if int(How_much_stealth_potion_to_buy) < 0:
                        prco("老板把你赶了出去", 1)
                    elif How_much_stealth_potion_to_buy == 0:
                        prco("你去商店逛了一圈，什么都没买", 3)
                    elif (How_much_stealth_potion_to_buy * 15) > Gold:
                        prco("你的金币还不够哦！", 1)
                    elif (How_much_stealth_potion_to_buy * 15) <= Gold:
                        Gold -= How_much_stealth_potion_to_buy * 15
                        Stealth_potions += How_much_stealth_potion_to_buy
                        prco("你获得了" + str(How_much_stealth_potion_to_buy) + "个隐身药剂", 4)
            elif Why == "0":
                pass #退出
        elif What_to_do == "4":
            prco("饲料 = " + str(How_much_feed_the_chicks_ate_in_total), 5)
            prco("加速卡 = " + str(Accelerator_card), 5)
            prco("金币 = " + str(Gold), 5)
            prco("隐身药剂 = " + str(Stealth_potions), 5)
            prco("玉米 = " + str(How_much_corn_is_there_in_total), 5)
            prco("玉米种子 = " + str(How_many_corn_seeds_there_were), 5)
            t.sleep(2)
        elif What_to_do == "5" and haveAccomplishment == False:
            prco(about)
            t.sleep(1)
        elif What_to_do == "5" and haveAccomplishment == True:
            prco("你获得的成就：")
            if mmod:
                prco("[" + Fore.LIGHTGREEN_EX + "偷鸡贼" + Fore.RESET + "]")
            if pope:
                prco("[" + Fore.LIGHTGREEN_EX + "礼貌问候" + Fore.RESET + "]")
            if ripe:
                prco("[" + Fore.LIGHTGREEN_EX + "大富翁" + Fore.RESET + "]")
        elif What_to_do == "6" and haveAccomplishment == True:
            prco(about)
            t.sleep(1)
        elif What_to_do == "0":
            if savedate == True:
                wdate = {
                            "date":{
                                "Gold":Gold,
                                "Stealth_potions":Stealth_potions,
                                "How_much_feed_the_chicks_ate_in_total":How_much_feed_the_chicks_ate_in_total,
                                "Accelerator_card":Accelerator_card,
                                "How_much_corn_is_there_in_total":How_much_corn_is_there_in_total,
                                "How_many_corn_seeds_there_were":How_many_corn_seeds_there_were
                            },
                            "accomplishment":{
                                "haveAccomplishment":haveAccomplishment,
                                "mmod":mmod,
                                "pope":pope,
                                "ripe":ripe
                            }
                        }
                wjf(wdate)
                cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were)) #保存数据
                cursor.close() #关闭游标
                conn.commit() #提交事务
                conn.close() #关闭数据库
            prco("拜拜\n")
            t.sleep(0.5)

            break #退出循环，结束程序

if __name__ == "__main__":
    try:
        XJZY()
    except Exception as e:
        prco("程序出现错误", 1)
        prco(f"请复制以下代码:\n{e}", 1)
        prco("到\"https://gitee.com/bxl24563/XJZY/issues/\"新建issues", 1)