# :coding:utf-8
# 打包代码：pyinstaller --paths <colorama目录> -F <小鸡庄园文件名>.py
# 打包代码（小白专用）：pyinstaller --paths D:\code_storehouse\Python3.11.5\Lib\site-packages\colorama -F XJZY.py
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
 ·2.7：进度条+成就系统+BUG修复
 ·2.8：开始动画+玩法升级
 ·2.9：BUG修复+成就树（当前）

 ·状态：更新中······
 
 ·XJZY 1x只更新到1.6版本
 ·XJZY 2x增加了数据保存、彩色字体功能，目前正在更新

 ·XJZY 1.0~1.5、2.0、2.0.1已被删除QAQ

 ·开发：白猫
 ·调试：橘猫、白水（电脑不见了，可能是被马桶冲走了）
 ·邮箱：白猫：3589326704@qq.com
 ·网址：https://gitee.com/bxl24563/XJZY
 ·备用网址：https://gitcode.com/bxl24563/XJZY
 ·联系：
      Bilibili：白猫：白猫猫猫猫猫猫猫儿、橘猫：橘猫猫猫猫猫猫猫儿、白水：白水Whusacr
"""

version = "2.9Beta1"

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
        print(Fore.YELLOW + text + Fore.RESET) #yellow:提示
    elif color == 6:
        print(Fore.LIGHTBLUE_EX + text + Fore.RESET) #blue:选择
    elif color == 7:
        print(Fore.LIGHTMAGENTA_EX + text + Fore.RESET) #magenta:挑战专用

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
        print("", end="\n\b")

def wjf(wdate=None):
    """Write Json File"""
    import json
    import os

    global version #改变version作用域

    if os.name == "nt":
        datehome = "C:\\Users\\"+os.getlogin()+"\\AppData\\LocalLow\\"+"XJZY"
        datepath = datehome+f"\\XJZY-{version}.json"
        if not os.path.exists(datehome):
            os.mkdir(datehome)
    else:
        datepath = f".XJZY-{version}.json"

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
                        # 普通
                        "neco":False,
                        "frsc":False,
                        "figo":False,
                        "deal":False,
                        "coon":False,
                        "cnsc":False,
                        # 高级
                        "aoag":False,
                        "stol":False,
                        "cost":False,
                        "prof":False,
                        "pope":False,
                        "pogo":False,
                        "pref":False,
                        # 挑战
                        "soha":False,
                        "moex":False,
                        "golu":False,
                        "balu":False,
                        "eate":False,
                        "mmod":False,
                        "ripe":False
                    },
                    "accomplishment_date":{
                        "Number_of_thefts":0,
                        "Number_of_transactions":0,
                    }
               }
        json_date = json.dumps(date, indent=4)
        with open(datepath, "w+") as json_file:
            json_file.write(json_date)
    else:
        date = wdate
        json_date = json.dumps(date, indent=4)
        with open(datepath, "w+") as json_file:
            json_file.write(json_date)

def rjf():
    """Read Json File"""
    import json
    import os

    global version #改变version作用域

    if os.name == "nt":
        datehome = "C:\\Users\\"+os.getlogin()+"\\AppData\\LocalLow\\"+"XJZY"
        datepath = datehome+f"\\XJZY-{version}.json"
    else:
        datepath = f".XJZY-{version}.json"

    with open(datepath, "r") as json_file:
        json_date = json.loads(json_file.read())
        return json_date

def clear():
    """清屏"""
    import os

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def logo(status="start"):
    from colorama import init, Fore
    import os

    init()
    width = os.get_terminal_size().columns # 获取终端的长度
    height = os.get_terminal_size().lines # 获取终端的宽度
    
    clear()
    
    startlogo = {
    "1":"   _  __    _________  __",
    "2":"  | |/ /   / /__  /\ \/ /",
    "3":"  |   /_  / /  / /  \  /",
    "4":" /   / /_/ /  / /__ / /",
    "5":"/_/|_\____/  /____//_/"
    }

    endlogo = {
    "1":"   ______                ______",
    "2":"  / ____/___  ____  ____/ / __ )__  _____",
    "3":" / / __/ __ \/ __ \/ __  / __  / / / / _ \\",
    "4":"/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/",
    "5":"\____/\____/\____/\__,_/_____/\__, /\___/",
    "6":"                             /____/"
    }
    if status == "start": # 开始动画
        startlogo_width = 26 # logo的长度
        startlogo_height = 5 # logo的宽度
    
        line = 1
    
        startlogo_x = (width - startlogo_width) / 2 # 计算出logo的准确位置
        startlogo_y = (height - startlogo_height) / 2
    
        startlogo_x = int(startlogo_x) # 把不能整除的转换为整数
        startlogo_y = int(startlogo_y)

        for a in range(startlogo_y): # 上面的空行
            print()
        
        for c in range(startlogo_x): # 左边的空行
            print(" ", end="", flush=False)
        
        for b in range(1):
            for d in range(startlogo_height): #完善的一部分logo
                print(startlogo[str(line)])
                int(line)
        
                for c in range(startlogo_x): # 左边的空行
                    print(" ", end="", flush=False)
        
                if line < startlogo_height: #继续下一部分logo
                    line += 1
                else:
                    break # 完成
         
        for a in range(startlogo_y):# 下面的空行
            print()
    elif status == "end": # 结束动画
        prco(Fore.RESET)
        endlogo_width = 42 # logo的长度
        endlogo_height = 6 # logo的宽度
    
        line = 1
    
        endlogo_x = (width - endlogo_width) / 2 # 计算出logo的准确位置
        endlogo_y = (height - endlogo_height) / 2
    
        endlogo_x = int(endlogo_x) # 把不能整除的转换为整数
        endlogo_y = int(endlogo_y)

        for a in range(endlogo_y): # 上面的空行
            print()
        
        for c in range(endlogo_x): # 左边的空行
            print(" ", end="", flush=False)
        
        for b in range(1):
            for d in range(endlogo_height): #完善的一部分logo
                print(endlogo[str(line)])
                int(line)
        
                for c in range(endlogo_x): # 左边的空行
                    print(" ", end="", flush=False)
        
                if line < endlogo_height: #继续下一部分logo
                    line += 1
                else:
                    break # 完成
         
        for a in range(endlogo_y):# 下面的空行
            print()

def XJZY(): #主函数
    from colorama import init, Fore  # ←导入颜色模块(prco的依赖)
    import os as o  # ←导入系统模块
    import random as r  # ←导入随机数模块
    import re as e  # ←导入格式化字符模块
    import time as t  # ←导入时间模块
    import sqlite3 # ←导入数据库模块

    init() #←初始化colorama

    global version #改变version作用域

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
 ·2.7：进度条+成就系统+BUG修复
 ·2.8：开始动画+玩法升级
 ·2.9：（当前）

 ·状态：更新中······
 
 ·XJZY 1x只更新到1.6版本
 ·XJZY 2x增加了数据保存、彩色字体功能，目前正在更新

 ·XJZY 1.0~1.5、2.0、2.0.1已被删除QAQ

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
│5.成就                   │
│6.关于                   │
├─────────────────────────┤
│0.退出                   │
╰─────────────────────────╯
           """
    shopmenu = """
╭─────────────────────────╮
│          商店           │
├─────────────────────────┤
│1.买加速卡               │
│2.卖饲料                 │
│3.买种子                 │
│4.卖玉米                 │
│5.买隐身药剂             │
├─────────────────────────┤
│0.返回                   │
╰─────────────────────────╯
           """                 #对，你没看错，就是这样（因为某些奇奇怪怪的字符问题）
    debugmenu = """
╭─────────────────────────╮
│          debug          │
├─────────────────────────┤
│1.关闭数据保存           │
│2.删除数据               │
├─────────────────────────┤
│0.返回                   │
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

    Number_of_thefts = 0 # 偷吃的次数
    Number_of_transactions = 0 # 交易的次数
    Number_of_stolen = 0 # 被偷吃的次数
    Number_of_been_bullied = 0 # 被打的次数
    Number_of_not_bullied = 0 # 没被打的次数

    if o.name == "nt":
        datehome = "C:\\Users\\"+o.getlogin()+"\\AppData\\LocalLow\\"+"XJZY"
        datepath = datehome+f"\\XJZY-{version}.json"
        dbhome = o.path.dirname(o.path.abspath(__file__))
        dbpath = dbhome + f"\\XJZY-{version}.db"
    else:
        datepath = f".XJZY-{version}.json"
    savedate = True

    # 普通
    neco = False #[初来乍到]
    frsc = False #[白手起家]
    figo = False #[第一桶金]
    deal = False #[成交！]
    coon = False #[撸起袖子加油吃]
    cnsc = False #[看，看不清楚]
    # 高级
    aoag = False #[我会玩了]
    stol = False #[黑吃黑？]
    cost = False #[什么都是有代价的]
    prof = False #[专业小偷]
    pope = False #[礼貌问候]
    pogo = False #[真的是一桶金]
    pref = False #[老顾客，有优惠吗？]
    # 挑战
    soha = False #[来点更难的？]
    moex = False #[小偷院长]
    golu = False #[欧皇圣体]
    balu = False #[天生非酋体质]
    eate = False #[黑吃黑,我是被吃的]
    mmod = False #[真的是小偷！]
    ripe = False #[大富翁]

    wdate = {}

    logo()
    t.sleep(1)
    clear()

    if not o.path.exists(dbpath):
        #新手引导
        name = input("你好，怎么称呼：")
        debug = input(f"你好啊{name},欢迎你来到小鸡镇。")
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
                input(Fore.BLUE + "确定删除数据吗？")
                if o.name == "nt":
                    if o.path.exists(datepath):
                        o.remove(datepath)
                    if o.path.exists(dbpath):
                        cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were)) #保存数据
                        cursor.close() #关闭游标
                        conn.commit() #提交事务
                        conn.close() #关闭数据库
                        savedate = False
                        o.remove(dbpath)
                else:
                    if o.path.exists(dbpath):
                        o.remove(dbpath)
                    if o.path.exists(f".XJZY-{version}.json"):
                        o.remove(f".XJZY-{version}.json")
                    savedate = False
                prco("删除完成！在你退出游戏前，你所做的更改都不会被保存！", 4)
                t.sleep(1.5)
                clear()
            elif opendebug == 0:
                pass
        else:
            input("在这里,每个人都会拥有自己的一只小鸡和一小块庄园,这里就是你的庄园。")
            input("那边分别是AA、BB、CC和DD的庄园,我们可以去那边偷些饲料；当然我们也要小心被偷吃......")
            input("沿这条路去到镇中心的商店,你可以在那里将饲料换成金币,你也可以拿金币买玉米种子,加速卡,甚至是隐身药剂。")
            input("对了,这些给你(5个金币,10个饲料)好了,我不打扰了,希望我再回来的时候,你能干出自己的一番天地!")
            input("(老人离开了这里······)")
            t.sleep(1)
            clear()
            if neco == False:
                prco("获得成就[" + Fore.LIGHTGREEN_EX + "初来乍到" + Fore.RESET + "]")
                neco = True
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
            conn = sqlite3.connect(dbpath) #创建数据库文件
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
        clear()
        prco(f"版本：{version}")
        prco("通知：开始动画和更多的成就！")
        conn = sqlite3.connect(dbpath) #选择数据库文件
        cursor = conn.cursor()
        cursor.execute("select * from xjzy") #执行SQL语句
        xjzydbresult = cursor.fetchone() #查找全部的数据
        if o.path.exists(datepath):
            date = rjf()
            # date
            json_Gold = date["date"]["Gold"]
            json_Stealth_potions = date["date"]["Stealth_potions"]
            json_How_much_feed_the_chicks_ate_in_total = date["date"]["How_much_feed_the_chicks_ate_in_total"]
            json_Accelerator_card = date["date"]["Accelerator_card"]
            json_How_much_corn_is_there_in_total = date["date"]["How_much_corn_is_there_in_total"]
            json_How_many_corn_seeds_there_were = date["date"]["How_many_corn_seeds_there_were"]

            # accomplishment
            # 普通
            neco = date["accomplishment"]["neco"]
            frsc = date["accomplishment"]["frsc"]
            figo = date["accomplishment"]["figo"]
            deal = date["accomplishment"]["deal"]
            coon = date["accomplishment"]["coon"]
            cnsc = date["accomplishment"]["cnsc"]
            stol = date["accomplishment"]["stol"]
            cost = date["accomplishment"]["cost"]
            # 高级
            aoag = date["accomplishment"]["aoag"]
            prof = date["accomplishment"]["prof"]
            pope = date["accomplishment"]["pope"]
            pogo = date["accomplishment"]["pogo"]
            pref = date["accomplishment"]["pref"]
            # 挑战
            soha = date["accomplishment"]["soha"]
            moex = date["accomplishment"]["moex"]
            golu = date["accomplishment"]["golu"]
            balu = date["accomplishment"]["balu"]
            eate = date["accomplishment"]["eate"]
            mmod = date["accomplishment"]["mmod"]
            ripe = date["accomplishment"]["ripe"]

            # accomplishment_date
            Number_of_thefts = date["accomplishment_date"]["Number_of_thefts"]
            Number_of_transactions = date["accomplishment_date"]["Number_of_transactions"]

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
                    prco("获得成就[" + Fore.LIGHTGREEN_EX + "真的是小偷！" + Fore.RESET + "]")
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
        if figo == False and Gold > 5:
            prco("获得成就[" + Fore.LIGHTGREEN_EX + "第一桶金" + Fore.RESET + "]")
            figo = True
            t.sleep(1)


        if What_to_do == "你好":
            if pope == False:
                prco("你好，有什么事吗？")
                t.sleep(0.5)
                prco("获得成就[" + Fore.LIGHTGREEN_EX + "礼貌问候" + Fore.RESET + "]")
                pope = True
                t.sleep(0.5)
            else:
                prco("你好，有什么事吗？")
                t.sleep(1)

        if neco and frsc and figo and deal and coon and cnsc and stol and cost and aoag == False:
            prco("获得成就[" + Fore.LIGHTYELLOW_EX + "我会玩了" + Fore.RESET + "]")
            aoag = True
            t.sleep(1)

        if Number_of_thefts >= 50 and prof == False:
            prco("获得成就[" + Fore.LIGHTYELLOW_EX + "专业小偷" + Fore.RESET + "]")
            prof = True
            t.sleep(1)

        if Number_of_transactions >= 50 and pref == False:
            prco("获得成就[" + Fore.LIGHTYELLOW_EX + "老顾客,有优惠吗?" + Fore.RESET + "]")
            pref = True
            t.sleep(1)

        if pogo == False and Gold >= 50:
            prco("获得成就[" + Fore.LIGHTYELLOW_EX + "真的是一桶金" + Fore.RESET + "]")
            pogo = True
            t.sleep(1)

        if Number_of_thefts >= 100 and moex == False:
            prco("获得成就[" + Fore.LIGHTMAGENTA_EX + "小偷院长" + Fore.RESET + "]")
            moex = True
            t.sleep(1)

        if golu == False and Number_of_not_bullied >= 10:
            prco("获得成就[" + Fore.LIGHTMAGENTA_EX + "欧皇圣体" + Fore.RESET + "]")
            golu = True
            t.sleep(1)

        if balu == False and Number_of_been_bullied >= 10:
            prco("获得成就[" + Fore.LIGHTMAGENTA_EX + "天生非酋体质" + Fore.RESET + "]")
            balu = True
            t.sleep(1)

        if ripe == False and Gold >= 500:
            prco("获得成就[" + Fore.LIGHTMAGENTA_EX + "大富翁" + Fore.RESET + "]")
            ripe = True
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
                            # 普通
                            "neco":neco,
                            "frsc":frsc,
                            "figo":figo,
                            "deal":deal,
                            "coon":coon,
                            "cnsc":cnsc,
                            # 高级
                            "aoag":aoag,
                            "stol":stol,
                            "cost":cost,
                            "prof":prof,
                            "pope":pope,
                            "pogo":pogo,
                            "pref":pref,
                            # 挑战
                            "soha":soha, 
                            "moex":moex,
                            "golu":golu,
                            "balu":balu,
                            "eate":eate,
                            "mmod":mmod,
                            "ripe":ripe,
                        },
                        "accomplishment_date":{
                            "Number_of_thefts":Number_of_thefts,
                            "Number_of_transactions":Number_of_transactions,
                        }
                    }
            wjf(wdate)

            # ↓保存数据
            cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were))
            conn.commit() #提交事务

        Whether_or_not_to_steal_it = r.choice(Stealing_probability)
        if Whether_or_not_to_steal_it == "T" and How_much_feed_the_chicks_ate_in_total >= 20:
            Number_of_stolen += 1
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
            if stol == False:
                prco("获得成就[" + Fore.LIGHTYELLOW_EX + "黑吃黑？" + Fore.RESET + "]")
                stol = True
                t.sleep(1)
            elif eate == False and Number_of_stolen >= 10:
                prco("获得成就[" + Fore.LIGHTMAGENTA_EX + "黑吃黑,我是被吃的" + Fore.RESET + "]")
                eate = True
                t.sleep(1)
            else:
                t.sleep(1)
        else:
            Number_of_stolen = 0
        prco("\n" + "─"*o.get_terminal_size().columns, 3)
        prco(menu, 2) #输出菜单

        What_to_do = input(Fore.BLUE + "你要干什么呢？")
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

                Number_of_thefts += 1

            if Whether_to_use_an_accelerator_card == "1" and Whether_to_use_stealth_potions == "1":
                Accelerator_card -= 1
                Stealth_potions -= 1
                prco("你使用了1张加速卡和1瓶隐身药剂，小鸡进食速度大大加快并且还隐身了", 4)
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
                if frsc == False:
                    prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                    frsc = True
                    t.sleep(1)
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

                if coon == False:
                    prco("获得成就[" + Fore.LIGHTGREEN_EX + "撸起袖子加油吃" + Fore.RESET + "]")
                    coon = True

                if cnsc == False:
                    prco("获得成就[" + Fore.LIGHTGREEN_EX + "看,看不清楚" + Fore.RESET + "]")
                    cnsc = True
            if Whether_to_use_an_accelerator_card == "2" and Whether_to_use_stealth_potions == "2":
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
                    if frsc == False:
                        prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                        frsc = True
                        t.sleep(1)
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
                    Number_of_not_bullied += 1
                    Number_of_been_bullied = 0
                    How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                    prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)
                else:
                    Number_of_not_bullied = 0
                    Number_of_been_bullied += 1
                    if How_many_grams_were_eaten >= 10:
                        How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                        How_much_feed_the_chicks_ate_in_total -= 10
                        Already_treated = "T"
                        plead = "F"
                    else:
                        Already_treated = "F"
                    if How_much_feed_the_chicks_ate_in_total >= 10:
                        if Already_treated == "F":
                            How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                            How_much_feed_the_chicks_ate_in_total -= 10
                        plead = "F"
                    if How_much_feed_the_chicks_ate_in_total < 10 and How_many_grams_were_eaten < 10:
                        How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                        if How_much_feed_the_chicks_ate_in_total >= 10:
                            How_much_feed_the_chicks_ate_in_total -= 10
                            plead = "F"
                    if plead == "T":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)
                        if frsc == False:
                            prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                            frsc = True
                            t.sleep(1)
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
                        if frsc == False:
                            prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                            frsc = True
                            t.sleep(1)
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
                    if cost == False:
                        prco("获得成就[" + Fore.LIGHTYELLOW_EX + "什么都是有代价的" + Fore.RESET + "]")
                        cost = True
            if Whether_to_use_an_accelerator_card == "1" and Whether_to_use_stealth_potions == "2":
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
                        Number_of_not_bullied += 1
                        Number_of_been_bullied = 0
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)
                        if frsc == False:
                            prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                            frsc = True
                            t.sleep(1)
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
                        Number_of_not_bullied = 0
                        Number_of_been_bullied += 1
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
                                How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                                How_much_feed_the_chicks_ate_in_total -= 10
                            plead = "F"
                        if How_much_feed_the_chicks_ate_in_total < 10 and How_many_grams_were_eaten < 10:
                            How_much_feed_the_chicks_ate_in_total += How_many_grams_were_eaten
                            if How_much_feed_the_chicks_ate_in_total >= 10:
                                How_much_feed_the_chicks_ate_in_total -= 10
                                plead = "F"
                            plead = "T"
                        if plead == "T":
                            for i in range(100):
                                print_progress_bar(i + 1, 100, prefix='偷吃中:', length=25)
                                t.sleep(How_many_minutes_were_eaten/1000)
                            if frsc == False:
                                prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                                frsc = True
                                t.sleep(1)
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
                            if frsc == False:
                                prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                                frsc = True
                                t.sleep(1)
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

                        if cost == False:
                            prco("获得成就[" + Fore.LIGHTYELLOW_EX + "什么都是有代价的" + Fore.RESET + "]")
                            cost = True

                    if coon == False:
                        prco("获得成就[" + Fore.LIGHTGREEN_EX + "撸起袖子加油吃" + Fore.RESET + "]")
                        coon = True
                else:
                    prco("你还没有加速卡哦！快去商店购买吧！", 5)
            if (
                Whether_to_use_an_accelerator_card == "2"
                and Whether_to_use_stealth_potions == "1"
            ):
                prco("你使用了1瓶隐身药剂，小鸡隐身了",4)
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
                if frsc == False:
                    prco("获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                    frsc = True
                    t.sleep(1)
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

                if cnsc == False:
                    prco("获得成就[" + Fore.LIGHTGREEN_EX + "看,看不清楚" + Fore.RESET + "]")
                    cnsc = True

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
            clear()

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
                        if deal == False:
                            prco("获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                            deal = True
                            t.sleep(1)
                        Number_of_transactions += 1
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
                            if deal == False:
                                prco("获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                deal = True
                                t.sleep(1)
                            Number_of_transactions += 1
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
                            prco("你获得了" + str(How_many_corn_seeds_to_buy) + "个玉米种子", 4)
                            if deal == False:
                                prco("获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                deal = True
                                t.sleep(1)
                            Number_of_transactions += 1
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
                        if deal == False:
                            prco("获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                            deal = True
                            t.sleep(1)
                        Number_of_transactions += 1
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
                        if deal == False:
                            prco("获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                            deal = True
                            t.sleep(1)
                        Number_of_transactions += 1

            elif Why == "0":
                clear() #退出

        elif What_to_do == "4":
            prco("饲料 = " + str(How_much_feed_the_chicks_ate_in_total), 5)
            prco("加速卡 = " + str(Accelerator_card), 5)
            prco("金币 = " + str(Gold), 5)
            prco("隐身药剂 = " + str(Stealth_potions), 5)
            prco("玉米 = " + str(How_much_corn_is_there_in_total), 5)
            prco("玉米种子 = " + str(How_many_corn_seeds_there_were), 5)
            t.sleep(2)

        elif What_to_do == "5":
            # 普通
            if neco:
                neco_name = "[" + Fore.LIGHTGREEN_EX + "初来乍到" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                neco_name = "[????????]"

            if frsc:
                frsc_name = "[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                frsc_name = "[????????]"

            if figo:
                figo_name = "[" + Fore.LIGHTGREEN_EX + "第一桶金" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                figo_name = "[????????]"

            if deal:
                deal_name = "[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                deal_name = "[??????]"

            if coon:
                coon_name = "[" + Fore.LIGHTGREEN_EX + "撸起袖子加油吃" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                coon_name = "[??????????????]"

            if cnsc:
                cnsc_name = "[" + Fore.LIGHTGREEN_EX + "看，看不清楚" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                cnsc_name = "[????????????]"
            # 高级
            if aoag:
                aoag_name = "[" + Fore.LIGHTYELLOW_EX + "我会玩了" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                aoag_name = "[????????]"

            if cost:
                cost_name = "[" + Fore.LIGHTYELLOW_EX + "什么都是有代价的" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                cost_name = "[????????????????]"

            if stol:
                stol_name = "[" + Fore.LIGHTYELLOW_EX + "黑吃黑？" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                stol_name = "[????????]"

            if prof:
                prof_name = "[" + Fore.LIGHTYELLOW_EX + "专业小偷" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                prof_name = "[????????]"

            if pope:
                pope_name = "[" + Fore.LIGHTYELLOW_EX + "礼貌问候" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                pope_name = "[????????]"

            if pogo:
                pogo_name = "[" + Fore.LIGHTYELLOW_EX + "真的是一桶金" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                pogo_name = "[????????????]"

            if pref:
                pref_name = "[" + Fore.LIGHTYELLOW_EX + "老顾客，有优惠吗？" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                pref_name = "[??????????????????]"
            # 挑战
            if soha:
                soha_name = "[" + Fore.LIGHTMAGENTA_EX + "来点更难的？" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                soha_name = "[????????????]"
            if moex:
                moex_name = "[" + Fore.LIGHTMAGENTA_EX + "小偷院长" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                moex_name = "[????????]"

            if golu:
                golu_name = "[" + Fore.LIGHTMAGENTA_EX + "欧皇圣体" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                golu_name = "[????????]"

            if balu:
                balu_name = "[" + Fore.LIGHTMAGENTA_EX + "天生非酋体质" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                balu_name = "[????????????]"

            if eate:
                eate_name = "[" + Fore.LIGHTMAGENTA_EX + "黑吃黑，我是被吃的" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                eate_name = "[??????????????????]"

            if mmod:
                mmod_name = "[" + Fore.LIGHTMAGENTA_EX + "真的是小偷！" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                mmod_name = "[??????????]"

            if ripe:
                ripe_name = "[" + Fore.LIGHTMAGENTA_EX + "大富翁" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                ripe_name = "[??????]"
            accomplishment = f"""
{neco_name}─────{frsc_name}─┬───{coon_name}─────{cnsc_name}──╮
                          ╰───{deal_name}─────{figo_name}──────────────╯

                                                    ╔═════{pogo_name}══════╗
{aoag_name}═════{cost_name}═════{stol_name}════╬═════{prof_name}══════════╣
                                                    ╚═════{pref_name}╝

                  ┏━━━━━{golu_name}━━━━━{balu_name}━━━━━{eate_name}━━━━━┓
{soha_name}━━━━╋━━━━━{moex_name}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                  ┗━━━━━{ripe_name}━━━━━{mmod_name}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                             """
            prco(accomplishment, 3)
        elif What_to_do == "6":
            prco(about)
            t.sleep(1)
        elif What_to_do == "db": #调试模式
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
                if o.name == "nt":
                    if o.path.exists(datepath):
                        o.remove(datepath)

                    if o.path.exists(dbpath):
                        cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were)) #保存数据
                        cursor.close() #关闭游标
                        conn.commit() #提交事务
                        conn.close() #关闭数据库
                        savedate = False
                        o.remove(dbpath)
                else:
                    if o.path.exists(dbpath):
                        o.remove(dbpath)
                    if o.path.exists(f".XJZY-{version}.json"):
                        o.remove(f".XJZY-{version}.json")
                    savedate = False
                prco("删除完成！请重启游戏。", 4)
        elif What_to_do == "0":
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
                                # 普通
                                "neco":neco,
                                "frsc":frsc,
                                "figo":figo,
                                "deal":deal,
                                "coon":coon,
                                "cnsc":cnsc,
                                # 高级
                                "aoag":aoag,
                                "stol":stol,
                                "cost":cost,
                                "prof":prof,
                                "pope":pope,
                                "pogo":pogo,
                                "pref":pref,
                                # 挑战
                                "soha":soha,
                                "moex":moex,
                                "golu":golu,
                                "balu":balu,
                                "eate":eate,
                                "mmod":mmod,
                                "ripe":ripe,
                            },
                            "accomplishment_date":{
                                "Number_of_thefts":Number_of_thefts,
                                "Number_of_transactions":Number_of_transactions,
                            }
                        }
                wjf(wdate)
                cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were)) #保存数据
                cursor.close() #关闭游标
                conn.commit() #提交事务
                conn.close() #关闭数据库

            logo("end")
            t.sleep(2)

            clear()
            break #退出循环，结束程序
        else:
            clear()

if __name__ == "__main__":
    XJZY() #调用主函数