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
 ·2.4：BUG修复（当前）

 ·状态：更新中······
 ·XJZY 1x只更新到1.6版本
 ·XJZY 2x增加了数据保存、彩色字体功能，目前正在更新

 ·开发：小白、调试：小陈
 ·邮箱：小白：3589326704@qq.com
 ·网址：https://gitee.com/xiaobai-it_1/XJZY
 ·联系：
      Bilibili：小白：白猫猫猫猫猫猫猫儿、小陈：橘猫猫猫猫猫猫猫儿
"""


def XJZY():
    import os as o  # ←导入系统模块
    import random as r  # ←导入随机数模块
    import re as e  # ←导入格式化字符模块
    import time as t  # ←导入时间模块
    from colorama import init, Fore  # ←导入颜色模块
    from prco import prco  # ←导入我写的颜色函数
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
 ·2.4：BUG修复（当前）
            
 ·状态：更新中······
 ·XJZY 1x只更新到1.6版本
 ·XJZY 2x增加了数据保存、彩色字体功能，目前正在更新
            
 ·开发：小白、调试：小陈
 ·邮箱：小白：3589326704@qq.com
 ·网址：https://gitee.com/xiaobai-it_1/XJZY
 ·联系：
      Bilibili：小白：白猫猫猫猫猫猫猫儿、小陈：橘猫猫猫猫猫猫猫儿
             """

    print_list = ["1、去偷吃", "2、种玉米", "3、去商店", "4、查看资源", "5、信息", "6、退出"]
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
    if not o.path.exists("XJZY.db"):
        #初始化
        conn = sqlite3.connect("XJZY.db") #创建数据库文件
        cursor = conn.cursor() #创建游标
        cursor.execute("create table xjzy (id int(1) primary key, Gold float, Stealth_potions int,How_much_feed_the_chicks_ate_in_total int, Accelerator_card int,How_much_corn_is_there_in_total int,How_many_corn_seeds_there_were int)") #数据库结构
        cursor.execute("insert into xjzy (id, Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were) values (1, 0, 0, 0, 0, 0, 0)") #给数据库赋值
        Gold = 0
        Stealth_potions = 0
        How_much_feed_the_chicks_ate_in_total = 0
        Accelerator_card = 0
        How_much_corn_is_there_in_total = 0
        How_many_corn_seeds_there_were = 0
        #新手引导
        if input("欢迎来到小鸡庄园") != "n": #跳过
            t.sleep(1)
            input("这里就是我们的庄园；当然以后啊就是你的了。看，那些分别是AA、BB、CC、DD的庄园")
            input("我们可以去那里偷一点饲料回来；当然我们也要小心被偷吃")
            input("看到那个大房子了吗？那个就是商店，你可以去那里做一些卖买")
            input("好了，我就不打扰了，再见！")
            input("(老人离开了这里······)")
            t.sleep(1)
    else:
        prco("版本：2.4")
        prco("通知：全面优化了“小鸡庄园”")
        conn = sqlite3.connect("XJZY.db") #选择数据库文件
        cursor = conn.cursor()
        cursor.execute("select * from xjzy") #执行SQL语句
        xjzydbresult = cursor.fetchone() #查找全部的数据
        if xjzydbresult != None: #数据库为空
            # xjzydbresult[0]是id字段
            Gold = xjzydbresult[1]
            Stealth_potions = xjzydbresult[2]
            How_much_feed_the_chicks_ate_in_total = xjzydbresult[3]
            Accelerator_card = xjzydbresult[4]
            How_much_corn_is_there_in_total = xjzydbresult[5]
            How_many_corn_seeds_there_were = xjzydbresult[6]
        else:
            Gold = 0
            Stealth_potions = 0
            How_much_feed_the_chicks_ate_in_total = 0
            Accelerator_card = 0
            How_much_corn_is_there_in_total = 0
            How_many_corn_seeds_there_were = 0
    # ↓死循环
    while True:
        # ↓保存数据
        cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were))
        conn.commit() #提交事务
        t.sleep(0.5)
        prco("=" * 45 + "小鸡庄园" + "=" * 45) #分割线
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
            prco("\n")
            prco("=" * 45 + "小鸡庄园" + "=" * 45)
        for print_variable in print_list: #输出菜单
            prco(print_variable, 2)
            # ↓等待0.5秒
            t.sleep(0.5)
            # ↑“t”：time模块
        What_to_do = input(Fore.BLUE + "你要干什么呢？")
        if What_to_do == "1":
            if Accelerator_card > 0:
                prco("1、要", 2)
                t.sleep(0.5)
                prco("2、不要", 2)
                t.sleep(0.5)
                Whether_to_use_an_accelerator_card = input(Fore.BLUE + "你要用加速卡吗？")
            else:
                Whether_to_use_an_accelerator_card = "2"
            if Stealth_potions > 0:
                prco("1、要", 2)
                # ↓“t”：time模块
                t.sleep(0.5)
                prco("2、不要", 2)
                # ↓“t”：time模块
                t.sleep(0.5)
                Whether_to_use_stealth_potions = input(Fore.BLUE + "你要用隐身药剂吗？")
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
                    t.sleep(0.5)
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
                t.sleep(0.5)
                Whether_to_be_beaten_or_not = ["T", "T", "F", "F", "F"]
                Whether_to_be_beaten_or_not = r.choice(Whether_to_be_beaten_or_not)
                if Whether_to_be_beaten_or_not == "F":
                    prco(
                        "你的小鸡在" +
                        str(Manor_Lord_1) +
                        "的庄园偷吃了" +
                        str(How_many_minutes_were_eaten) +
                        "分钟，吃掉了" +
                        str(How_many_grams_were_eaten) +
                        "克饲料，就被" +
                        str(Manor_Lord_1) +
                        "赶了回来，幸运的是：你的小鸡没被" +
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
                        if plead != "F":
                            plead = "T"
                    if plead == "T":
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
                    # ↓声明列表“庄园主1”
                    Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
                    # ↓在列表“庄园主1”随机选一个元素（我们可以把列表的名字看作一个班级，元素看作班级里的成员）并将这个元素保存到“庄园主1”
                    Manor_Lord_1 = r.choice(Manor_Lord_1)
                    #        ↑“r”：random模块
                    How_many_minutes_were_eaten = r.randint(15, 30)
                    #             ↑“r”：random模块
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
                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_1) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_1) +
                            "赶了回来，幸运的是：你的小鸡没被" +
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
                Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
                Manor_Lord_1 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 5
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 10
                else:
                    How_many_grams_were_eaten = 15
                t.sleep(0.5)
                # ↑“t”：time模块
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
                prco("你还没有玉米的种子呢！快去购买吧！")
            else:
                prco("你有" + str(How_many_corn_seeds_there_were) + "个种子", 5)
                try:
                    How_much_to_plant = int(input(Fore.BLUE + "你要种多少玉米？"))
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
                        How_much_corn_is_there_in_total += How_much_to_plant
                        prco("种植成功", 4)
                    elif How_much_to_plant == 0:
                        prco("你去地里逛了一圈，什么都没干")
        elif What_to_do == "3":
            prco("1、买加速卡", 2)
            prco("2、卖饲料", 2)
            prco("3、买种子", 2)
            prco("4、卖玉米", 2)
            prco("5、卖隐身药剂", 2)
            Why = input(Fore.BLUE + "你要做什么买卖？")
            if Why == "1":
                prco("1张加速卡=1个金币", 5)
                prco("你现在一共有" + str(Gold) + "个金币，和" + str(Accelerator_card) + "张加速卡", 5)
                try:
                    How_many_acceleration_cards_to_buy = int(input(Fore.YELLOW + "你要买多少加速卡："))
                except ValueError:
                    prco("老板把你赶了出去", 1)
                else:
                    if int(How_many_acceleration_cards_to_buy) > int(Gold):
                        if Gold == 0:
                            prco("你现在没有金币哦！", 5)
                        else:
                            prco("你的金币还不够哦！你现在只有" + str(Gold) + "个金币", 1)
                    elif int(How_many_acceleration_cards_to_buy) <= int(Gold) and How_many_acceleration_cards_to_buy != 0:
                        Accelerator_card += int(How_many_acceleration_cards_to_buy)
                        Gold -= int(How_many_acceleration_cards_to_buy)
                        prco("购买成功", 4)
                        prco("你获得了" + str(How_many_acceleration_cards_to_buy) + "个加速卡", 5)
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
                    if How_much_feed_the_chicks_ate_in_total >= How_much_feed_to_buy:
                        Gold += int(How_much_feed_to_buy) / 5
                        How_much_feed_the_chicks_ate_in_total -= int(
                            How_much_feed_to_buy
                        )
                        prco("你卖了" + str(How_much_feed_to_buy) + "克饲料", 4)
                    else:
                        prco("你还没有那么多饲料！", 1)
                    if How_much_feed_to_buy == 0:
                        prco("你去商店逛了一圈，什么都没卖")
            elif Why == "3":
                prco("你有" + str(Gold) + "个金币", 5)
                prco("1个玉米种子=5个金币", 5)
                try:
                    How_many_corn_seeds_to_buy = int(input(Fore.BLUE + "你要买多少玉米种子？"))
                except ValueError:
                    prco("老板把你赶了出去", 1)
                else:
                    if (How_many_corn_seeds_to_buy * 5) > Gold:
                        prco("你的金币还不够哦！", 1)
                    elif (How_many_corn_seeds_to_buy * 5) <= Gold:
                        Gold -= How_many_corn_seeds_to_buy * 5
                        How_many_corn_seeds_there_were += How_many_corn_seeds_to_buy
                        prco("购买成功！", 4)
                        prco("你获得了" + str(How_many_corn_seeds_to_buy) + "个玉米种子", 4)
                    if How_many_corn_seeds_to_buy == 0:
                        prco("你去商店逛了一圈，什么都没买")
            elif Why == "4":
                prco("你有" + str(How_much_corn_is_there_in_total) + "个玉米", 5)
                prco("1个玉米=10个金币", 5)
                try:
                    How_much_corn = int(input(Fore.BLUE + "你要卖多少玉米？"))
                except ValueError:
                    prco("客人不知道你要干嘛，你什么都没卖出去", 1)
                else:
                    if How_much_corn == 0:
                        pass
                    elif How_much_corn_is_there_in_total < How_much_corn:
                        prco("你还没有那么多玉米哦！", 1)
                    elif How_much_corn_is_there_in_total >= How_much_corn:
                        Gold += How_much_corn * 10
                        How_much_corn_is_there_in_total -= How_much_corn
                        prco("成功卖出", 4)
                    if How_much_corn == 0:
                        prco("你去商店逛了一圈，什么都没卖")
            elif Why == "5":
                prco("你有" + str(Gold) + "个金币", 5)
                prco("1瓶隐身药剂=15个金币", 5)
                try:
                    How_much_stealth_potion_to_buy = int(input(Fore.BLUE + "你要买多少隐身药剂？"))
                except ValueError:
                    prco("老板把你赶了出去", 1)
                else:
                    if (How_much_stealth_potion_to_buy * 15) > Gold:
                        prco("你的金币还不够哦！", 1)
                    elif (How_much_stealth_potion_to_buy * 15) <= Gold:
                        Gold -= How_much_stealth_potion_to_buy * 15
                        Stealth_potions += How_much_stealth_potion_to_buy
                        prco("购买成功！", 4)
                        prco("你获得了" + str(How_much_stealth_potion_to_buy) + "个隐身药剂", 5)
                    if How_much_stealth_potion_to_buy == 0:
                        prco("你去商店逛了一圈，什么都没买", 5)
        elif What_to_do == "4":
            t.sleep(0.5)
            prco("饲料 = " + str(How_much_feed_the_chicks_ate_in_total), 5)
            t.sleep(0.5)
            prco("加速卡 = " + str(Accelerator_card), 5)
            t.sleep(0.5)
            prco("金币 = " + str(Gold), 5)
            t.sleep(0.5)
            prco("隐身药剂 = " + str(Stealth_potions), 5)
            t.sleep(0.5)
            prco("玉米 = " + str(How_much_corn_is_there_in_total), 5)
            t.sleep(0.5)
            prco("玉米种子 = " + str(How_many_corn_seeds_there_were), 5)
        elif What_to_do == "5":
            prco(about)
        elif What_to_do == "6":
            cursor.execute("update xjzy set Gold = ?, Stealth_potions = ?, How_much_feed_the_chicks_ate_in_total = ?, Accelerator_card = ?, How_much_corn_is_there_in_total = ?, How_many_corn_seeds_there_were = ? where id = 1", (Gold, Stealth_potions, How_much_feed_the_chicks_ate_in_total, Accelerator_card, How_much_corn_is_there_in_total, How_many_corn_seeds_there_were)) #保存数据
            cursor.close() #关闭游标
            conn.commit() #提交事务
            conn.close() #关闭数据库
            prco("拜拜\n")
            t.sleep(0.5)
            break #退出循环，结束程序


if __name__ == "__main__":
    XJZY()
