# -*- coding: utf-8 -*-
"""
                        小鸡庄园是一款文字游戏，由“XJZY开发组”开发和测试
                                    版权所有 (C) 2025 小白

                            本程序是自由软件：您可以重新分发或修改它
它根据 GNU 通用公共许可证的条款发布Free Software Foundation，许可证的第 3 版，或（由您选择）任何更高版本。

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
 ·2.9：玩法升级+数据保存功能4+代码整理+BUG修复（当前）
 
 ·XJZY 1x只更新到1.6版本
 ·XJZY 2x增加了数据保存、彩色字体功能，目前正在更新

 ·开发：白猫
 ·调试：橘猫、old唐（电脑不见了，可能是被马桶冲走了）

 ·1.0~1.4、2.0、2.0.1已被删除 QAQ

 ·网址：https://gitee.com/PSWG/XJZY
 ·备用网址：https://gitcode.com/bxl24563/XJZY
 ·联系：
      微信：橘猫：橘猫（真的就叫橘猫）
      QQ：白猫：3589326704    橘猫:3956670241
      邮箱：白猫：3589326704@qq.com    橘猫：18978996240@163.com
      Bilibili：白猫：白猫猫猫猫猫猫猫儿    橘猫：橘猫猫猫猫猫猫猫儿    old唐：白水Whusacr
"""
# 打包代码：pyinstaller --paths <colorama目录> -F <小鸡庄园文件名>.py
# 打包代码（白猫专用）：pyinstaller --paths D:\code_storehouse\Python3.11.5\Lib\site-packages\colorama -F XJZY.py -i D:\code\Python\XJZY-V2\XJZY-2.9(Test)\ico\1.ico
from colorama import init, Fore  # ←导入颜色模块
from pickle import dump, load
from re import findall  # ←导入正则表达式匹配库中的findall函数


golds = 0
key = b"\xae\xf8\xe7|\x15\xd3\x6a1AO\xe3`\t\xf0\xb5\xa8" # ←密钥
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

thefts_time = 0 # 偷吃的次数
transactions_time = 0 # 交易的次数
stolen_time = 0 # 被偷吃的次数
bullied_time = 0 # 被打的次数
not_bullied_time = 0 # 没被打的次数

def prco(text, color=3):
    """
    PRint COlor
    颜色模块
    """
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

def print_progress_bar(iteration, total, prefix="",
                       suffix="", decimals=1, length=100,
                       fill="="):
    """
    进度条（感谢国外佚名大佬提供）
    """
    init() #初始化colorama

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = (Fore.LIGHTGREEN_EX + fill + Fore.RESET) * filledLength + (Fore.LIGHTWHITE_EX + fill + Fore.RESET) * (length - filledLength)

    print(f"\r{prefix} [{bar}] {percent}% {suffix}", end="\r") # 效果类似：描述 [=========================] 100.0%

    if iteration == total:
        print("", end="\n\b")

def write_data(version, data_pack):
    with open(f"XJZY-{version}.pkl", "wb") as f:  
        dump(data_pack, f)

def read_data(version):
    with open(f"XJZY-{version}.pkl", "rb") as f:
        data_pack = load(f)
    return data_pack

def clear():
    """清屏"""
    import os

    if os.name == "nt": # 不同系统使用不同命令
        os.system("cls") # Windows
    else:
        os.system("clear") # Unix、Linux、MacOS

def logo(version, status="start"):
    """XJZY Logo!"""
    import os

    init()
    VERSION_LEN = len(version) # ←版本名长度（为了居中显示）
    width = os.get_terminal_size().columns # 获取终端的长度
    height = os.get_terminal_size().lines # 获取终端的宽度

    clear()
    # 开始logo的尺寸
    startlogo_width = 26 # logo的最大长度
    startlogo_height = 6 # logo的最大宽度

    # 开始logo
    startlogo = {
    "1":"   _  __    _________  __",
    "2":"  | |/ /   / /__  /\ \/ /",
    "3":"  |   /_  / /  / /  \  /",
    "4":" /   / /_/ /  / /__ / /",
    "5":"/_/|_\____/  /____//_/",
    "6":f"{(int((startlogo_width-VERSION_LEN-3)/2))*' '}{version}{(int((startlogo_width-VERSION_LEN-3)/2))*' '}" # 版本号居中（也许有点乱）
    }

    # 结束logo的尺寸
    endlogo_width = 42 # logo的最大长度
    endlogo_height = 6 # logo的最大宽度

    # 结束logo
    endlogo = {
    "1":"   ______                ______",
    "2":"  / ____/___  ____  ____/ / __ )__  _____",
    "3":" / / __/ __ \/ __ \/ __  / __  / / / / _ \\", # 因为“\”会被Python识别成转义字符，所以这里用了两个“\”
    "4":"/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/",
    "5":"\____/\____/\____/\__,_/_____/\__, /\___/",
    "6":"                             /____/"
    }
    if status == "start": # 开始动画

        line = 1

        startlogo_x = int((width - startlogo_width) / 2) # 计算出logo的准确位置，并把不能整除的转换为整数
        startlogo_y = int((height - startlogo_height) / 2)

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

                if line < startlogo_height:
                    line += 1 #继续下一部分logo
                else:
                    break # 完成

        for a in range(startlogo_y):# 下面的空行
            print()
    elif status == "end": # 结束动画
        # 清除颜色
        prco(Fore.RESET)

        line = 1

        endlogo_x = int((width - endlogo_width) / 2) # 计算出logo的准确位置，并把不能整除的转换为整数
        endlogo_y = int((height - endlogo_height) / 2)

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
    del a
    del b
    del c
    del d

def showmenu(status="initialmenu"):
    import os
    try:
        initialmenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{((os.get_terminal_size().columns-10)/2)*" "}小鸡庄园{((os.get_terminal_size().columns-10)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 偷吃{(os.get_terminal_size().columns-8)*" "}│
│2 巡逻{(os.get_terminal_size().columns-8)*" "}│
│3 种玉米{(os.get_terminal_size().columns-10)*" "}│
│4 镇商店{(os.get_terminal_size().columns-10)*" "}│
│5 仓库{(os.get_terminal_size().columns-8)*" "}│
│6 成就墙{(os.get_terminal_size().columns-10)*" "}│
│7 升级{(os.get_terminal_size().columns-8)*" "}│
│8 更多{(os.get_terminal_size().columns-8)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 退出{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    except TypeError: # 如果屏幕（终端）宽度很刁钻，左边会多出来一个空格
        initialmenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{int((os.get_terminal_size().columns-10)/2)*" "}小鸡庄园{int((os.get_terminal_size().columns-9)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 偷吃{(os.get_terminal_size().columns-8)*" "}│
│2 巡逻{(os.get_terminal_size().columns-8)*" "}│
│3 种玉米{(os.get_terminal_size().columns-10)*" "}│
│4 镇商店{(os.get_terminal_size().columns-10)*" "}│
│5 仓库{(os.get_terminal_size().columns-8)*" "}│
│6 成就墙{(os.get_terminal_size().columns-10)*" "}│
│7 升级{(os.get_terminal_size().columns-8)*" "}│
│8 更多{(os.get_terminal_size().columns-8)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 退出{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    try:
        shopmenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{((os.get_terminal_size().columns-8)/2)*" "}商店{((os.get_terminal_size().columns-8)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 卖饲料{(os.get_terminal_size().columns-10)*" "}│
│2 买加速卡{(os.get_terminal_size().columns-12)*" "}│
│3 买隐身药剂{(os.get_terminal_size().columns-14)*" "}│
│4 加工玉米饲料{(os.get_terminal_size().columns-16)*" "}│
│5 买种子{(os.get_terminal_size().columns-10)*" "}│
│6 卖玉米{(os.get_terminal_size().columns-10)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 返回{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    except TypeError:
        shopmenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{int((os.get_terminal_size().columns-6)/2)*" "}商店{int((os.get_terminal_size().columns-5)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 卖饲料{(os.get_terminal_size().columns-10)*" "}│
│2 买加速卡{(os.get_terminal_size().columns-12)*" "}│
│3 买隐身药剂{(os.get_terminal_size().columns-14)*" "}│
│4 加工玉米饲料{(os.get_terminal_size().columns-16)*" "}│
│5 买种子{(os.get_terminal_size().columns-10)*" "}│
│6 卖玉米{(os.get_terminal_size().columns-10)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 返回{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    try:
        moremenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{((os.get_terminal_size().columns-8)/2)*" "}更多{((os.get_terminal_size().columns-8)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 关于{(os.get_terminal_size().columns-8)*" "}│
│2 Wiki{(os.get_terminal_size().columns-8)*" "}│
│3 源代码{(os.get_terminal_size().columns-10)*" "}│
│4 GPLv3许可证{(os.get_terminal_size().columns-15)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 返回{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    except TypeError:
        moremenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{int((os.get_terminal_size().columns-6)/2)*" "}更多{int((os.get_terminal_size().columns-5)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 关于{(os.get_terminal_size().columns-8)*" "}│
│2 Wiki{(os.get_terminal_size().columns-8)*" "}│
│3 源代码{(os.get_terminal_size().columns-10)*" "}│
│4 GPLv3许可证{(os.get_terminal_size().columns-15)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 返回{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    try:
        debugmenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{((os.get_terminal_size().columns-8)/2)*" "}Debug{((os.get_terminal_size().columns-8)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 开启数据保存{(os.get_terminal_size().columns-16)*" "}│
│2 关闭数据保存{(os.get_terminal_size().columns-16)*" "}│
│3 清除数据{(os.get_terminal_size().columns-12)*" "}│
│4 删除数据{(os.get_terminal_size().columns-12)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 返回{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    except TypeError:
        debugmenu = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{int((os.get_terminal_size().columns-7)/2)*" "}Debug{int((os.get_terminal_size().columns-6)/2)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│1 开启数据保存{(os.get_terminal_size().columns-16)*" "}│
│2 关闭数据保存{(os.get_terminal_size().columns-16)*" "}│
│3 清除数据{(os.get_terminal_size().columns-12)*" "}│
│4 删除数据{(os.get_terminal_size().columns-12)*" "}│
├{(os.get_terminal_size().columns-2)*"─"}┤
│0 返回{(os.get_terminal_size().columns-8)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    try:
        selectivemenu1 = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{((os.get_terminal_size().columns-18)/3)*" "}1 确定{((os.get_terminal_size().columns-18)/3)*" "}2 取消{int((os.get_terminal_size().columns-5)/3)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    except Exception as e:
        selectivemenu1 = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{int((os.get_terminal_size().columns-16)/3)*" "}1 确定{int((os.get_terminal_size().columns-18)/3)*" "}2 取消{int((os.get_terminal_size().columns-5)/3)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    try:
        selectivemenu2 = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{((os.get_terminal_size().columns-16)/3)*" "}1 要{((os.get_terminal_size().columns-16)/3)*" "}2 不要{int((os.get_terminal_size().columns-5)/3)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """
    except Exception as e:
        selectivemenu2 = f"""
╭{(os.get_terminal_size().columns-2)*"─"}╮
│{int((os.get_terminal_size().columns-14)/3)*" "}1 要{int((os.get_terminal_size().columns-16)/3)*" "}2 不要{int((os.get_terminal_size().columns-5)/3)*" "}│
╰{(os.get_terminal_size().columns-2)*"─"}╯
        """

    if status == "initialmenu":
        prco(initialmenu, 2)
    elif status == "shopmenu":
        prco(shopmenu, 2)
    elif status == "moremenu":
        prco(moremenu, 2)
    elif status == "debugmenu":
        prco(debugmenu, 2)
    elif status == "selectivemenu1":
        prco(selectivemenu1, 2)
    elif status == "selectivemenu2":
        prco(selectivemenu2, 2)

def check_achievements():
    init()

    global golds
    global neco
    global frsc
    global figo
    global deal
    global coon
    global cnsc
    global stol
    global cost
    global aoag
    global prof
    global pope
    global pogo
    global pref
    global soha
    global moex
    global golu
    global balu
    global eate
    global mmod
    global ripe

    global thefts_time
    global transactions_time
    global stolen_time
    global bullied_time
    global not_bullied_time

    achievements = []
    # 这些都是数据到达某个点时触发的成就
    if neco and frsc and figo and deal and coon and cnsc and stol and cost and aoag is False:
        achievements.append(Fore.LIGHTYELLOW_EX + "我会玩了" + Fore.RESET)
        aoag = True

    if stol and cost and aoag and prof and pope and pogo and pref and soha is False:
        achievements.append(Fore.LIGHTYELLOW_EX + "我会玩了" + Fore.RESET)
        soha = True

    if thefts_time >= 50 and not prof:
        achievements.append(Fore.LIGHTYELLOW_EX + "专业小偷" + Fore.RESET)
        prof = True

    if transactions_time >= 50 and not pref:
        achievements.append(Fore.LIGHTYELLOW_EX + "老顾客,有优惠吗?" + Fore.RESET)
        pref = True

    if thefts_time >= 100 and not moex:
        achievements.append(Fore.LIGHTMAGENTA_EX + "小偷院长" + Fore.RESET)
        moex = True

    if not golu and not_bullied_time >= 10:
        achievements.append(Fore.LIGHTMAGENTA_EX + "欧皇圣体" + Fore.RESET)
        golu = True

    if not balu and bullied_time >= 10:
        achievements.append(Fore.LIGHTMAGENTA_EX + "天生非酋体质" + Fore.RESET)
        balu = True

    if not ripe and golds >= 500:
        achievements.append(Fore.LIGHTMAGENTA_EX + "大富翁" + Fore.RESET)
        ripe = True

    return achievements

def XJZY(version, announcement): #主函数。参数一是版本号，参数二是公告
    import os as o  # ←导入系统模块
    import random as r  # ←导入随机数模块
    import time as t  # ←导入时间模块

    init() #←初始化colorama
    
    # 改变作用域
    global golds
    global neco
    global frsc
    global figo
    global deal
    global coon
    global cnsc
    global stol
    global cost
    global aoag
    global prof
    global pope
    global pogo
    global pref
    global soha
    global moex
    global golu
    global balu
    global eate
    global mmod
    global ripe

    global thefts_time
    global transactions_time
    global stolen_time
    global bullied_time
    global not_bullied_time

    # ↓声明不保存到数据库的变量，从而预防UnboundLocalError错误
    copyright = Fore.LIGHTRED_EX + f"""
{o.get_terminal_size().columns * "─"}
这是 GNU 通用公共许可证（GNU GPL）的非正式简体中文翻译
它并未被自由软件基金会发行，也不是使用 GNU GPL 软件的发布法律声明——只有 GNU GPL 的原始英文版才有法律意义
不过，我们希望该翻译能够帮助简体中文用户更好地理解 GNU GPL。
{o.get_terminal_size().columns * "─"}""" + Fore.RESET + f"""


{int((o.get_terminal_size().columns-4)/2) * " "}【引言】
　　GNU通用公共许可协议是一份面向软件及其他类型作品的，自由的版权共产协议。
　　就多数软件而言，许可协议被设计用于剥夺你分享和修改软件的自由。相反，GNU通用公共许可协议力图保障你分享和修改某程序全部版本的权利--确保自由软件对其用户来说是自由的。我们自由软件基金会将GNU通用公共许可协议用于我们的大多数软件，并为一些其他作品的作者效仿。你也可以将本协议用于你的程序。
　　所谓自由软件，强调自由，而非免费。本GNU通用公共许可协议设计用于确保你享有分发自由软件的自由（你可以为此服务收费），确保你可以在需要的时候获得这些软件的源码，确保你可以修改这些软件或者在新的自由软件中复用其中某些片段，并且确保你在这方面享有知情权。
　　为保障你的权益，我们需要作一些限定：禁止任何人否认你的上述权利，或者要求你放弃它们。因此，当你分发或修改这些软件时，你有一定的责任--尊重他人的自由。如果你分发这种程序的副本，无论收费还是免费，你必须给予与你同等的权利。你还要确保他们也能收到源码并了解他们的权利。
　　采用GNU通用公共许可协议的开发者通过两步保障你的权益：其一，申明软件的版权；其二，通过本协议使你可以合法地复制、分发和修改该软件。
　　为了保护每一位作者和开发者，GNU通用公共许可协议指明一点：自由软件并没有品质担保。为用户和作者双方着想，GNU通用公共许可协议要求修改版必须有标记，以免其问题被错误地归到先前版本的作者身上。
　　某些设备设计成拒绝用户安装运行修改过的软件，但厂商不受限。这和我们保护用户享有修改软件的自由的宗旨存在根本性矛盾。该滥用协议的模式出现于个人用品领域，这恰是最不可接受的。因此，我们设计了这版GNU通用公共许可协议来禁止这类产品。如果此类问题在其他领域涌现，我们时刻准备着在将来的版本中把规定扩展到相应领域，以保护用户的自由。
　　最后，每个程序都持续受到软件专利的威胁。政府不应该允许专利限制通用计算机软件的开发和应用，在做不到这点时，我们希望避免专利应用有效地使自由软件私有化的危险。就此，GNU通用公共许可协议保证专利不能使程序非自由化。

　　下文是关于复制、分发和修改的严谨描述和实施条件。

{int((o.get_terminal_size().columns-30)/2) * " "}【关于复制、分发和修改的术语和条件】
〇、定义

　　"本协议"指GNU通用公共许可协议第三版。
　　"版权"也指适用于诸如半导体掩模的其他类型作品的类似法律。
　　"本程序"指任何在本协议保护下的有版权的作品。每个许可获得者称作"你"。"许可获得者"和"接收者"可以是个人或组织。
　　"修改"一个作品指需要版权许可的复制及对作品全面的或部分的改编行为，有别于制作副本。所产生的作品称作前作的"修改版"，或"基于"前作的作品。
　　"受保护作品"指程序或其派生作品。
　　"传播"作品指那些未经许可就会在适用版权法律下构成直接或间接侵权的行为，不包括在计算机上运行和私下的修改。传播包括复制、分发（无论修改与否）、向公众公开，以及在某些国家的其他行为。
　　"转发"作品指让他方能够制作或者接收副本的行为。仅仅通过计算机网络和用户交互，没有传输副本，则不算转发。
　　一个显示"适当的法律声明"的交互式用户界面应包括一个便捷而醒目的可视化特性：(1)显示适当的版权声明；(2)告知用户没有品质担保（提供了品质担保的情况除外），许可获得者可以在本协议约束下转发该作品，及查看本协议副本的途径。如果该界面提供一个命令列表，如菜单，其表项应符合上述规范。

一、源码

　　作品的源码指其可修改的首选形式，目标码指所有其他形式。
　　"标准接口"指标准化组织定义的官方标准中的接口，或针为某种编程语言设定的接口中为开发者广泛使用的接口。
　　可执行作品中的"系统库"不是指整个程序，而是涵盖此等内容：(a)以通常形式和主部件打包到一起却并非后者一部分，且(b)仅为和主部件一起使作品可用或实现某些已有公开实现源码的接口。"主部件"在这里指可执行作品运行依赖的操作系统（如果存在）的必要部件（内核、窗口系统等），生成该作品的编译器，或运行所需的目标码解释器。
　　目标码形式的作品中"相应的源码"指所有修改作品及生成、安装、运行（对可执行作品而言）目标码所需的源码，包括控制上述行为的脚本。可是，其中不包括系统库、通用工具、未修改直接用于支持上述行为却不是该作品一部分的通常可得的自由软件。例如，相应的源码包含配合作品源文件的接口定义，以及共享库和作品专门依赖的动态链接子程序的源码。这里的依赖体现为频密的数据交换或者该子程序和作品其他部分的控制流切换。
　　相应的源码不必包含那些用户可以通过源码其他部分自动生成的内容。
　　源码形式作品的相应源码即其本身。

二、基本许可

　　本协议的一切授权都是对本程序的版权而言的，并且在所述条件都满足时不可撤销。本协议明确批准你不受限制地运行本程序的未修改版本。受保护作品的运行输出，仅当其内容构成一个受保护作品时，才会为本协议所约束。如版权法所赋予，本协议承认你正当使用或与之等价的权利。
　　只要你获得的许可仍有效，你可以制作、运行和传播那些你并不转发的受保护作品。只要你遵守本协议中关于转发你不占有版权的材料的条款，你可以向他人转发，仅仅以求对方为你做定制或向你提供运行这些作品的工具。那些为你制作或运行这些受保护作品的人，应该在你的指引和控制下，谨代表你工作，即禁止他们在双方关系之外制作任何你提供的受版权保护材料的副本。
　　仅当满足后文所述条件时，其他各种情况下的转发才是允许的。不允许再授权行为，而第十条的存在使再授权变得没有必要。

三、保护用户的合法权益免受反破解法限制

　　在任何满足1996年12月20日通过的WIPO版权条约第11章要求的法律，或类似的禁止或限制技术手段破解的法律下，受保护作品不应该视为有效技术手段的一部分。
　　当你转发一个受保护作品时，你将失去任何通过法律途径限制技术手段破解的权力，乃至于通过行使本协议所予权利实现的破解。你即已表明无心通过限制用户操作或修改受保护作品来确保你或第三方关于禁止技术手段破解的法定权利。

四、转发完整副本

　　你可以通过任何媒介发布你接收到的本程序的完整源码副本，但要做到：为每一个副本醒目而恰当地发布版权；完整地保留关于本协议及按第七条加入的非许可性条款；完整地保留免责声明；给接收者附上一份本协议的副本。
　　你可以免费或收费转发，也可以选择提供技术支持或品质担保以换取收入。

五、转发修改过的源码版本

　　你可以以源码形式转发基于本程序的作品或修改的内容，除满足第四条外还需要满足以下几点要求：
　　a)该作品必须带有醒目的修改声明及相应的日期。
　　b)该作品必须带有醒目的声明，指出其在本协议及任何符合第七条的附加条件下发布。这个要求修正了第四条关于"完整保留"的内容。
　　c)你必须按照本协议将该作品整体向想要获得许可的人授权，本协议及符合第七条的附加条款就此适用于整个作品，即其每一部分，不管如何建包。本协议不允许以其他形式授权该作品，但如果你收到别的许可则另当别论。
　　d)如果该作品有交互式用户界面，则其必须显示适当的法律声明。然而，当本程序有交互式用户界面却不显示适当的法律声明时，你的作品也不必。
一个在存储或分发媒介上的受保护作品和其他分离的单体作品的联合作品，在既不是该受保护作品的自然扩展，也不以构筑更大的程序为目的，并且自身及其产生的版权并非用于限制单体作品给予联合作品用户的访问及其他合法权利时，称为"聚合体"。在聚合作品中包含受保护作品并不会使本协议影响聚合作品的其他部分。

六、以非源码形式转发

　　你可以如第四条和第五条所述那样以目标码形式转发受保护作品，同时在本协议规范下以如下方式之一转发机器可读的对应源码：
　　a)目标码通过实体产品（涵盖某种实体分发媒介）转发时，通过常用于软件交换的耐用型实体媒介随同转发相应的源码。
　　b)目标码通过实体产品（涵盖某种实体分发媒介）转发时，伴以具有至少三年且与售后服务等长有效期的书面承诺，给予目标码的持有者：(1)包含产品全部软件的相应源码的常用于软件交换的耐用型实体媒介，且收费不超过其合理的转发成本；或者(2)通过网络免费获得相应源码的途径。
　　c)单独转发目标码时，伴以提供源码的书面承诺。本选项仅在你收到目标码及b项形式的承诺的情况下可选。
　　d)通过在指定地点提供目标码获取服务（无论是否收费）的形式转发目标码时，在同一地点以同样的方式提供对等的源码获取服务，并不得额外收费。你不以要求接收者在复制目标码的同时复制源码。如果提供目标码复制的地点为网络服务器，相应的源码可以提供在另一个支持相同复制功能的服务器上（由你或者第三方运营），不过你要在目标码处指出相应源码的确切路径。不管你用什么源码服务器，你有义务要确保持续可用以满足这些要求。
　　e)通过点对点传输转发目标码时，告知其他节点目标码和源码在何处以d项形式向大众免费提供。
　　"面向用户的产品"指(1)"消费品"，即个人、家庭或日常用途的个人有形财产；或者(2)面向社会团体设计或销售，却落入居家之物。在判断一款产品是否消费品时，争议案例的判断将向利于扩大保护靠拢。就特定用户接收到特定产品而言，"正常使用"指对此类产品的典型或一般使用，不管该用户的身份，该用户对该产品的实际用法，以及该产品的预期用法。无论产品是否实质上具有商业上的，工业上的，及非面向消费者的用法，它都视为消费品，除非以上用法代表了它唯一的重要使用模式。
　　"安装信息"对面向用户的产品而言，指基于修改过的源码安装运行该产品中的受保护作品的修改版所需的方法、流程、认证码及其他信息。这些信息必须足以保证修改过的目标码不会仅仅因为被修改过而不能继续工作。
　　如果你根据本条在，或随，或针对一款面向用户的产品，以目标码形式转发某作品，且转发体现于该产品的所有权和使用权永久或者在一定时期内转让予接收者的过程（无论其有何特点），根据本条进行的源码转发必须伴有安装信息。不过，如果你和第三方都没有保留在该产品上安装修改后的目标码的能力（如作品安装在ROM上），这项要求不成立。 　　要求提供安装信息并不要求为修改或安装的作品，以及其载体产品继续提供技术支持、品质担保和升级。当修改本身对网络运行有实质上的负面影响，或违背了网络通信协议和规则时，可以拒绝其联网。
　　根据本条发布的源码及安装信息，必须以公共的文件格式（并且存在可用的空开源码的处理工具）存在，同时不得对解压、阅读和复制设置任何密码。

七、附加条款

　　"附加许可"用于补充本协议，以允许一些例外情况。合乎适用法律的对整个程序适用的附加许可，应该被视为本协议的内容。如果附加许可作用于程序的某部分，则该部分受此附加许可约束，而其他部分不受其影响。
　　当你转发本程序时，你可以选择性删除副本或其部分的附加条款。（附加条款可以写明在某些情况下要求你修改时删除该条款。）在你拥有或可授予恰当版权许可的受保护作品中，你可以在你添加的材料上附加许可。
　　尽管已存在本协议的其他条款，对你添加到受保护作品的材料，你可以（如果你获得该材料版权持有人的授权）以如下条款补充本协议：
　　a)表示不提供品质担保或有超出十五、十六条的责任。
　　b)要求在此材料中或在适当的法律声明中保留特定的合理法律声明或创作印记。
　　c)禁止误传材料的起源，或要求合理标示修改以别于原版。
　　d)限制以宣传为目的使用该材料的作者或授权人的名号。
　　e)降低约束以便赋予在商标法下使用商品名、商品标识及服务标识。
　　f)要求任何转发该材料（或其修改版）并对接收者提供契约性责任许诺的人，保证这种许诺不会给作者或授权人带来连带责任。
　　此外的非许可性附加条款都被视作第十条所说的"进一步的限制"。如果你接收到的程序或其部分，声称受本协议约束，却补充了这种进一步的限制条款，你可以去掉它们。如果某许可协议包含进一步的限制条款，但允许通过本协议再授权或转发，你可以通过本协议再授权或转发加入了受前协议管理的材料，不过要同时移除上述条款。
　　如果你根据本条向受保护作品添加了调控，你必须在相关的源文件中加入对应的声明，或者指出哪里可以找到它们。
　　附加条款，不管是许可性的还是非许可性的，可以以独立的书面协议出现，也可以声明为例外情况，两种做法都可以实现上述要求。

八、终止授权

　　除非在本协议明确授权下，你不得传播或修改受保护作品。其他任何传播或修改受保护作品的企图都是无效的，并将自动中止你通过本协议获得的权利（包括第十一条第3段中提到的专利授权）。
　　然而，当你不再违反本协议时，你从特定版权持有人处获得的授权恢复：(1)暂时恢复，直到版权持有人明确终止；(2)永久恢复，如果版权持有人没能在60天内以合理的方式指出你的侵权行为。
　　再者，如果你第一次收到了特定版权持有人关于你违反本协议（对任意作品）的通告，且在收到通告后30天内改正，那你可以继续享此有授权。
　　当你享有的权利如本条所述被中止时，已经从你那根据本协议获得授权的他方的权利不会因此中止。在你的权利恢复之前，你没有资格凭第十条获得同一材料的授权。

九、持有副本无需接受协议

　　你不必为接收或运行本程序而接受本协议。类似的，仅仅因点对点传输接收到副本引发的对受保护作品的辅助性传播，并不要求接受本协议。但是，除本协议外没有什么可以授权你传播或修改任何受保护作品。如果你不接受本协议，这些行为就侵犯了版权。因此，一旦修改和传播一个受保护作品，就表明你接受本协议。

十、对下游接收者的自动授权

　　每当你转发一个受保护作品，其接收者自动获得来自初始授权人的授权，依照本协议可以运行、修改和传播此作。你没有要求第三方遵守该协议的义务。
　　"实体事务"指转移一个组织的控制权或全部资产、或拆分或合并组织的事务。如果实体事务导致一个受保护作品的传播，则事务中各收到作品副本方，都有获得前利益相关者享有或可以如前段所述提供的对该作品的任何授权，以及从前利益相关者处获得并拥有相应的源码的权利，如果前利益相关者享有或可以通过合理的努力获得此源码。
　　你不可以对本协议所授权利的行使施以进一步的限制。例如，你不可以索要授权费或版税，或就行使本协议所授权利征收其他费用；你也不能发起诉讼（包括交互诉讼和反诉），宣称制作、使用、零售、批发、引进本程序或其部分的行为侵犯了任何专利。

十一、专利

　　"贡献人"指通过本协议对本程序或其派生作品进行使用认证的版权持有人。授权作品成为贡献人的"贡献者版"。
　　贡献人的"实质专利权限"指其拥有或掌控的，无论是已获得的还是将获得的全部专利权限中，可能被通过某种本协议允许的方式制作、使用或销售其贡献者版作品的行为侵犯的部分，不包括仅有修改其贡献者版作品才构成侵犯的部分。"掌控"所指包括享有和本协议相一致的专利再授权的权利。
　　每位贡献人皆其就实质专利权限，授予你一份全球有效的免版税的非独占专利许可，以制作、使用、零售、批发、引进，及运行、修改、传播其贡献者版的内容。
　　在以下三段中，"专利许可"指通过任何方式明确表达的不行使专利权（如对使用专利的明确许可和不起诉专利侵权的契约）的协议或承诺。对某方"授予"专利许可，指这种不对其行使专利权的协议或承诺。
　　如果你转发的受保护作品已知依赖于某专利，而其相应的源码并不是任何人都能根据本协议从网上或其他地方免费获得，那你必须(1)以上述方式提供相应的源码；或者(2)放弃从该程序的专利许可中获得利益；或者(3)以某种和本协议相一致的方式将专利许可扩展到下游接收者。"已知依赖于"指你实际上知道若没有专利许可，你在某国家转发受保护作品的行为，或者接收者在某国家使用受保护作品的行为，会侵犯一项或多项该国认定的专利，而这些专利你有理由相信它们的有效性。
　　如果根据一项事务或安排，抑或与之相关，你转发某受保护作品，或通过促成其转手以实现传播，并且该作品的接收方授予专利许可，以使指可以使用、传播、修改或转发该作品的特定副本，则此等专利许可将自动延伸及每一个收到该作品或其派生作品的人。
　　如果某专利在其涵盖范围内，不包含本协议专门赋予的一项或多项权利，禁止行使它们或以不行使它们为前提，则该专利是"歧视性"的。如果你和软件发布行业的第三方有合作，合作要求你就转发受保护作品的情况向其付费，并授予作品接收方歧视性专利，而且该专利(a)与你转发的副本（或在此基础上制作的副本）有关，或针对包含该受保护作品的产品或联合作品，你不得转发本程序，除非参加此项合作或取得该专利早于2007年3月28日。
　　本协议的任何部分不应被解释成在排斥或限制任何暗含的授权，或者其他在适用法律下对抗侵权的措施。

十二、不得牺牲他人的自由

　　即便你面临与本协议条款冲突的条件（来自于法庭要求、协议或其他），那也不能成为你违背本协议的理由。倘若你不能在转发受保护作品时同时满足本协议和其他文件的要求，你就不能转发本程序。例如，当你同意了某些要求你就再转发问题向你的转发对象收取版税的条款时，唯一能同时满足它和本协议要求的做法便是不转发本程序。

十三、和GNU Affero通用公共许可协议一起使用

　　尽管已存在本协议的一些条款，你可以将任何受保护作品与以GNU Affero通用公共许可协议管理的作品关联或组合成一个联合作品，并转发。本协议对其中的受保护作品部分仍然有效，但GNU Affero通用公共许可协议第十三条的关于网络交互的特别要求适用于整个联合作品。

十四、本协议的修订版

　　自由软件联盟可能会不定时发布GNU通用公共许可协议的修订版或新版。新版将秉承当前版本的精神，但对问题或事项的描述细节不尽相同。
　　每一版都会有不同的版本号，如果本程序指定其使用的GNU通用公共许可协议的版本"或任何更新的版本"，你可以选择遵守该版本或者任何更新的版本的条款。如果本程序没有指定协议版本，你可以选用自由软件联盟发布的任意版本的GNU通用公共许可协议。
　　如果本程序指定代理来决定将来那个GNU通用公共许可协议版本适用，则该代理的公开声明将指导你选择协议版本。
　　新的版本可能会给予你额外或不同的许可。但是，任何作者或版权持有人的义务，不会因为你选择新的版本而增加。

十五、不提供品质担保

　　本程序在适用法律范围内不提供品质担保。除非另作书面声明，版权持有人及其他程序提供者"概"不提供任何显式或隐式的品质担保，品质担保所指包括而不仅限于有经济价值和适合特定用途的保证。全部风险，如程序的质量和性能问题，皆由你承担。若程序出现缺陷，你将承担所有必要的修复和更正服务的费用。

十六、责任范围

　　除非适用法律或书面协议要求，任何版权持有人或本程序按本协议可能存在的第三方修改和再发布者，都不对你的损失负有责任，包括由于使用或者不能使用本程序造成的任何一般的、特殊的、偶发的或重大的损失（包括而不仅限于数据丢失、数据失真、你或第三方的后续损失、其他程序无法与本程序协同运作），即使那些人声称会对此负责

十七、第十五条和第十六条的解释

　　如果上述免责声明和责任范围声明不为地方法律所支持，上诉法庭应采用与之最接近的关于放弃本程序相关民事责任的地方法律，除非本程序附带收费的品质担保或责任许诺。

{int((o.get_terminal_size().columns-32)/2) * " "}【附录：如何将上述条款应用到你的新程序】

　　如果你开发了一个新程序，并希望它能最大限度地为公众所使用，最好的办法是将其作为自由软件，以使每个人都能在本协议约束下对其再发布及修改。
　　为此，请在附上以下声明。最安全的做法是将其附在每份源码的开头，以便于最有效地传递免责信息。同时，每个文件至少包含一处"版权"声明和一个协议全文的链接。

　　<用一行来标明程序名及其作用>
　　版权所有（C）<年份> <作者姓名>
　　本程序为自由软件，在自由软件联盟发布的GNU通用公共许可协议的约束下，你可以对其进行再发布及修改。协议版本为第三版或（随你）更新的版本。
　　我们希望发布的这款程序有用，但不保证，甚至不保证它有经济价值和适合特定用途。详情参见GNU通用公共许可协议。
　　你理当已收到一份GNU通用公共许可协议的副本，如果没有，请查阅<http://www.gnu.org/licenses/>

　　同时提供你的电子邮件地址或传统的邮件联系方式。

　　如果该程序是交互式的，让它在交互模式下输出类似下面的一段声明：

　　<程序名> 第69版，版权所有（C）<年份> <作者姓名>
　　本程序从未提供品质担保，输入'show w'可查看详情。这是款自由软件，欢迎你在满足一定条件后对其再发布，输入'show c'可查看详情。

　　例子中的命令'show w'和'show c'应用于显示GNU通用公共许可协议相应的部分。当然你也可以因地制宜地选用别的方式，对图形界面程序可以用"关于"菜单。

　　如果你之上存在雇主（你是码农）或校方，你还应当让他们在必要时为此程序签署放弃版权声明。详情参见<http://www.gnu.org/licenses/>。

　　本GNU通用公共许可协议不允许把你的程序并入私有程序。如果你的程序是某种库，且你想允许它被私有程序链接而使之更有用，请使用GNU较宽松通用公共许可协议。决定前请先查阅<http://www.gnu.org/philosophy/why-not-lgpl.html>。
                 """
    about = f"""
                                当前版本：{version}

                                    开发者名单
                                       白猫
                                       橘猫
                                      old唐

                                       更多
                           https://gitee.com/PSWG/XJZY
                         https://gitcode.com/bxl24563/XJZY

                    小鸡庄园是一款文字游戏，由“XJZY开发组”开发和测试
                               版权所有 (C) 2025 小白

                        本程序是自由软件：您可以重新分发和/或修改它
它根据 GNU 通用公共许可证的条款发布Free Software Foundation，许可证的第 3 版，或（由您选择）任何更高版本。
            """

    What_to_do = ""
    Whether_to_use_an_accelerator_cards = ""
    Manor_Lord_1 = ["AA", "BB", "CC", "DD"]
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
    Whether_to_upgrade = ""
    Get_speed = {
    0:1, 1:1.1, 2:1.2, 3:1.3, 4:1.4, 5:1.5,
    6:1.6, 7:1.7, 8:1.8, 9:1.9, 10:2,
    11:2.1, 12:2.2, 13:2.3, 14:2.4, 15:2.5,
    16:2.6, 17:2.7, 18:2.8, 19:2.9, 20:3,
    21:3.1, 22:3.2, 23:3.3, 24:3.4, 25:3.5,
    26:3.6, 27:3.7, 28:3.8, 29:3.9, 30:4
    }

    if o.name == "nt":
        datehome = "C:\\Users\\"+o.getlogin()+"\\AppData\\LocalLow\\"+"XJZY"
        datepath = datehome+f"\\XJZY-{version}.json"
    else:
        datepath = f".XJZY-{version}.json"
    savedate = True

    wdate = {}

    logo(version=version)
    t.sleep(1)
    clear()

    if not o.path.exists(f"XJZY-{version}.pkl"):
        #新手引导
        if findall(r"^\d{1,}\.\d{1,}$", version) == []: #判断是不是正式版
            prco("注意！你当前游玩的是Beta版，可能有奇奇怪怪的bug!", 1)
            t.sleep(1)
        input("(风里有一股淡淡的海水味，你来到小鸡镇码头边······)")
        name = input("老人：你好，怎么称呼：")
        input(f"你：我叫{name}。")
        input(f"老人：你好啊{name}，欢迎你来到小鸡镇。")
        input("老人：在这里，每个人都会拥有自己的一只小鸡和一小块庄园，这里就是你的庄园。")
        input("老人：那边分别是AA、BB、CC和DD的庄园,我们可以去那边偷些饲料；当然我们也要小心被偷吃······")
        input("老人：沿这条路去到镇中心的商店，你可以在那里将饲料换成金币，你也可以拿金币买各种各样的东西。")
        input("老人：对了，这些给你(5个金币，10个饲料)好了，希望我再回来的时候，你能打造出一片最大的庄园!")
        input("(老人离开了这里······)")
        t.sleep(1)
        clear()
        prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "初来乍到" + Fore.RESET + "]")
        neco = True
        #初始化
        data_pack = {
            "golds":5,
            "stealth_potions":0,
            "feeds":10,
            "corn_feeds":0,
            "accelerator_cards":0,
            "corns":0,
            "corn_needs":0,
            "chick_level":0,
            "neco":True,
            "frsc":False,
            "figo":False,
            "deal":False,
            "coon":False,
            "cnsc":False,
            "aoag":False,
            "stol":False,
            "cost":False,
            "prof":False,
            "pope":False,
            "pogo":False,
            "pref":False,
            "soha":False,
            "moex":False,
            "golu":False,
            "balu":False,
            "eate":False,
            "mmod":False,
            "ripe":False,
            "thefts_time":0,
            "transactions_time":0
        }
        write_data(version, data_pack)

        golds = 5
        stealth_potions = 0
        feeds = 10
        corn_feeds = 0
        accelerator_cards = 0
        corns = 0
        corn_needs = 0
        chick_level = 0
        eating_speed = 1

        t.sleep(1)
    else:
        clear()
        prco(f"版本：{version}")
        prco(f"公告：{announcement}")
        data_pack = read_data(version)
        if data_pack != None: #数据不为空
            try:
                golds = data_pack["golds"]
                stealth_potions = data_pack["stealth_potions"]
                feeds = data_pack["feeds"]
                corn_feeds = data_pack["corn_feeds"]
                accelerator_cards = data_pack["accelerator_cards"]
                corns = data_pack["corns"]
                corn_needs = data_pack["corn_needs"]
                chick_level = data_pack["chick_level"]
                neco = data_pack["neco"]
                frsc = data_pack["frsc"]
                figo = data_pack["figo"]
                deal = data_pack["deal"]
                coon = data_pack["coon"]
                cnsc = data_pack["cnsc"]
                stol = data_pack["stol"]
                cost = data_pack["cost"]
                aoag = data_pack["aoag"]
                prof = data_pack["prof"]
                pope = data_pack["pope"]
                pogo = data_pack["pogo"]
                pref = data_pack["pref"]
                soha = data_pack["soha"]
                moex = data_pack["moex"]
                golu = data_pack["golu"]
                balu = data_pack["balu"]
                eate = data_pack["eate"]
                mmod = data_pack["mmod"]
                ripe = data_pack["ripe"]
                thefts_time = data_pack["thefts_time"]
                transactions_time = data_pack["transactions_time"]
            except TypeError:
                prco("不要再偷鸡了，这样不会有好下场的-.-",1)
                t.sleep(1)
                if not mmod:
                    prco("获得成就[" + Fore.LIGHTMAGENTA_EX + "真的是小偷！" + Fore.RESET + "]")
                    mmod = True
                    t.sleep(1)
                golds = 5
                stealth_potions = 0
                feeds = 10
                corn_feeds = 0
                accelerator_cards = 0
                corns = 0
                corn_needs = 0
                chick_level = 0
                eating_speed = 1

                neco = True
                frsc = False
                figo = False
                deal = False
                coon = False
                cnsc = False
                aoag = False
                stol = False
                cost = False
                prof = False
                pope = False
                pogo = False
                pref = False
                soha = False
                moex = False
                golu = False
                balu = False
                eate = False
                mmod = True
                ripe = False

                thefts_time = 0
                transactions_time = 0
                stolen_time = 0
                bullied_time = 0
                not_bullied_time = 0
        else:
            golds = 5
            stealth_potions = 0
            feeds = 10
            corn_feeds = 0
            accelerator_cards = 0
            corns = 0
            corn_needs = 0
            chick_level = 0
            eating_speed = 1

            neco = True
            frsc = False
            figo = False
            deal = False
            coon = False
            cnsc = False
            aoag = False
            stol = False
            cost = False
            prof = False
            pope = False
            pogo = False
            pref = False
            soha = False
            moex = False
            golu = False
            balu = False
            eate = False
            mmod = False
            ripe = False

            thefts_time = 0
            transactions_time = 0
            stolen_time = 0
            bullied_time = 0
            not_bullied_time = 0

    # ↓死循环
    while True:
        eating_speed = Get_speed[chick_level]
        Whether_or_not_to_steal_it = r.choice(Stealing_probability)
        # 判断是否获得成就
        achievements = check_achievements()
        for achievement in achievements:
            prco("\a获得成就[" + achievement + "]")
            t.sleep(1)

        if savedate:
            data_pack = {
                "golds":golds,
                "stealth_potions":stealth_potions,
                "feeds":feeds,
                "corn_feeds":corn_feeds,
                "accelerator_cards":accelerator_cards,
                "corns":corns,
                "corn_needs":corn_needs,
                "chick_level":chick_level,
                "neco":neco,
                "frsc":frsc,
                "figo":figo,
                "deal":deal,
                "coon":coon,
                "cnsc":cnsc,
                "aoag":aoag,
                "stol":stol,
                "cost":cost,
                "prof":prof,
                "pope":pope,
                "pogo":pogo,
                "pref":pref,
                "soha":soha,
                "moex":moex,
                "golu":golu,
                "balu":balu,
                "eate":eate,
                "mmod":mmod,
                "ripe":ripe,
                "thefts_time":thefts_time,
                "transactions_time":transactions_time
            }
            write_data(version, data_pack)

        if Whether_or_not_to_steal_it == "T" and feeds >= 20:
            stolen_time += 1
            Manor_Lord_2 = r.choice(Manor_Lord_1)
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
                str(Manor_Lord_2) +
                "的小鸡在你的的庄园偷吃了" +
                str(How_many_minutes_were_eaten) +
                "分钟，吃掉了" +
                str(How_many_grams_were_eaten) +
                "克饲料"
            , 1)
            feeds -= How_many_grams_were_eaten
            if not stol:
                prco("\a获得成就[" + Fore.LIGHTYELLOW_EX + "黑吃黑？" + Fore.RESET + "]")
                stol = True
                t.sleep(1)
            elif not eate and stolen_time >= 10:
                prco("\a获得成就[" + Fore.LIGHTMAGENTA_EX + "黑吃黑,我是被吃的" + Fore.RESET + "]")
                eate = True
                t.sleep(1)
            else:
                t.sleep(1)
        else:
            stolen_time = 0
        prco("\n" + "─"*o.get_terminal_size().columns, 3)

        showmenu()

        What_to_do = input(Fore.BLUE + "你要干什么呢？" + Fore.RESET)

        if What_to_do == "1":
            if accelerator_cards > 0:
                showmenu("selectivemenu2")
                t.sleep(0.5)
                Whether_to_use_an_accelerator_cards = input(Fore.BLUE + "你要给小鸡使用加速卡吗？" + Fore.RESET)
            else:
                Whether_to_use_an_accelerator_cards = "2"

            if stealth_potions > 0:
                showmenu("selectivemenu2")
                t.sleep(0.5)
                Whether_to_use_stealth_potions = input(Fore.BLUE + "你要给小鸡使用隐身药剂吗？" + Fore.RESET)
            else:
                Whether_to_use_stealth_potions = "2"

                thefts_time += 1

            if Whether_to_use_an_accelerator_cards == "1" and Whether_to_use_stealth_potions == "1":
                accelerator_cards -= 1
                stealth_potions -= 1
                prco("你使用了1张加速卡和1瓶隐身药剂，小鸡进食速度大大加快并且还隐身了", 4)
                Manor_Lord_2 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 10 * eating_speed
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 15 * eating_speed
                else:
                    How_many_grams_were_eaten = 20 * eating_speed
                for i in range(100):
                    print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                    t.sleep(How_many_minutes_were_eaten/1000)
                if not frsc:
                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                    frsc = True
                    t.sleep(1)
                prco(
                    "你的小鸡在" +
                    str(Manor_Lord_2) +
                    "的庄园偷吃了" +
                    str(How_many_minutes_were_eaten) +
                    "分钟，吃掉了" +
                    str(How_many_grams_were_eaten) +
                    "克饲料，就被" +
                    str(Manor_Lord_2) +
                    "赶了回来，因为你使用了隐身药剂，所以你的小鸡没被" +
                    str(Manor_Lord_2) +
                    "打到"
                , 4)
                feeds += How_many_grams_were_eaten
                prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)

                if not coon:
                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "撸起袖子加油吃" + Fore.RESET + "]")
                    coon = True

                if not cnsc:
                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "看,看不清楚" + Fore.RESET + "]")
                    cnsc = True

            if Whether_to_use_an_accelerator_cards == "2" and Whether_to_use_stealth_potions == "2":
                Manor_Lord_2 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 5 * eating_speed
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 10 * eating_speed
                else:
                    How_many_grams_were_eaten = 15 * eating_speed
                Whether_to_be_beaten_or_not = ["T", "T", "F", "F", "F"]
                Whether_to_be_beaten_or_not = r.choice(Whether_to_be_beaten_or_not)
                if Whether_to_be_beaten_or_not == "F":
                    for i in range(100):
                        print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                        t.sleep(How_many_minutes_were_eaten/1000)
                    if not frsc:
                        prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                        frsc = True
                        t.sleep(1)
                    prco(
                        "你的小鸡在" +
                        str(Manor_Lord_2) +
                        "的庄园偷吃了" +
                        str(How_many_minutes_were_eaten) +
                        "分钟，吃掉了" +
                        str(How_many_grams_were_eaten) +
                        "克饲料，就被" +
                        str(Manor_Lord_2) +
                        "赶了回来，你的小鸡很幸运，没有被" +
                        str(Manor_Lord_2) +
                        "打到"
                    , 4)
                    not_bullied_time += 1
                    bullied_time = 0
                    feeds += How_many_grams_were_eaten
                    prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)
                else:
                    not_bullied_time = 0
                    bullied_time += 1
                    if How_many_grams_were_eaten >= 10:
                        feeds += How_many_grams_were_eaten
                        feeds -= 10
                        Already_treated = "T"
                        plead = "F"
                    else:
                        Already_treated = "F"
                    if feeds >= 10:
                        if Already_treated == "F":
                            feeds += How_many_grams_were_eaten
                            feeds -= 10
                        plead = "F"
                    if feeds < 10 and How_many_grams_were_eaten < 10:
                        feeds += How_many_grams_were_eaten
                        if feeds >= 10:
                            feeds -= 10
                            plead = "F"
                    if plead == "T":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)
                        if not frsc:
                            prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                            frsc = True
                            t.sleep(1)
                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_2) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_2) +
                            "赶了回来，倒霉的是：你的小鸡被" +
                            str(Manor_Lord_2) +
                            "打到了。因为你没有足够的饲料，所以医生免费把你的小鸡治好了"
                        , 4)
                    if plead == "F":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)
                        if not frsc:
                            prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                            frsc = True
                            t.sleep(1)
                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_2) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_2) +
                            "赶了回来，倒霉的是：你的小鸡被" +
                            str(Manor_Lord_2) +
                            "打到了。你给了医生10克饲料，医生把你的小鸡治好了"
                        , 1)
                        prco("饲料-10", 1)
                    if not cost:
                        prco("\a获得成就[" + Fore.LIGHTYELLOW_EX + "什么都是有代价的" + Fore.RESET + "]")
                        cost = True

            if Whether_to_use_an_accelerator_cards == "1" and Whether_to_use_stealth_potions == "2":
                accelerator_cards -= 1
                prco("你使用了1张加速卡，小鸡撸起袖子开始双手吃饲料，进食速度大大加快", 4)
                Manor_Lord_2 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 10 * eating_speed
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 15 * eating_speed
                else:
                    How_many_grams_were_eaten = 20 * eating_speed
                t.sleep(0.5)
                Whether_to_be_beaten_or_not = ["T", "T", "F", "F", "F"]
                Whether_to_be_beaten_or_not = r.choice(Whether_to_be_beaten_or_not)
                if Whether_to_be_beaten_or_not == "F":
                    not_bullied_time += 1
                    bullied_time = 0
                    for i in range(100):
                        print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                        t.sleep(How_many_minutes_were_eaten/1000)
                    if not frsc:
                        prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                        frsc = True
                        t.sleep(1)
                    prco(
                        "你的小鸡在" +
                        str(Manor_Lord_2) +
                        "的庄园偷吃了" +
                        str(How_many_minutes_were_eaten) +
                        "分钟，吃掉了" +
                        str(How_many_grams_were_eaten) +
                        "克饲料，就被" +
                        str(Manor_Lord_2) +
                        "赶了回来，你的小鸡很幸运，没有被" +
                        str(Manor_Lord_2) +
                        "打到"
                    , 4)
                    feeds += (
                        How_many_grams_were_eaten
                    )
                    prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)
                else:
                    not_bullied_time = 0
                    bullied_time += 1
                    if How_many_grams_were_eaten >= 10:
                        feeds += (
                            How_many_grams_were_eaten
                        )
                        feeds -= 10
                        Already_treated = "T"
                        plead = "F"
                    else:
                        Already_treated = "F"
                    if feeds >= 10:
                        if Already_treated == "F":
                            feeds += How_many_grams_were_eaten
                            feeds -= 10
                        plead = "F"
                    if feeds < 10 and How_many_grams_were_eaten < 10:
                        feeds += How_many_grams_were_eaten
                        if feeds >= 10:
                            feeds -= 10
                            plead = "F"
                        plead = "T"
                    if plead == "T":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)
                        if not frsc:
                            prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                            frsc = True
                            t.sleep(1)
                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_2) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_2) +
                            "赶了回来，倒霉的是：你的小鸡被" +
                            str(Manor_Lord_2) +
                            "打了。因为你没有饲料，所以医生免费把你的小鸡治好了"
                        , 4)
                    if plead == "F":
                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                            t.sleep(How_many_minutes_were_eaten/1000)
                        if not frsc:
                            prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                            frsc = True
                            t.sleep(1)
                        prco(
                            "你的小鸡在" +
                            str(Manor_Lord_2) +
                            "的庄园偷吃了" +
                            str(How_many_minutes_were_eaten) +
                            "分钟，吃掉了" +
                            str(How_many_grams_were_eaten) +
                            "克饲料，就被" +
                            str(Manor_Lord_2) +
                            "赶了回来，倒霉的是：你的小鸡被" +
                            str(Manor_Lord_2) +
                            "打了。你给了医生10克饲料，医生把你的小鸡治好了"
                        , 1)
                        prco("饲料-10", 1)
                    if not cost:
                        prco("\a获得成就[" + Fore.LIGHTYELLOW_EX + "什么都是有代价的" + Fore.RESET + "]")
                        cost = True

                if not coon:
                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "撸起袖子加油吃" + Fore.RESET + "]")
                    coon = True
            if Whether_to_use_an_accelerator_cards == "2" and Whether_to_use_stealth_potions == "1":
                prco("你使用了1瓶隐身药剂，小鸡隐身了",4)
                Manor_Lord_2 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 5 * eating_speed
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 10 * eating_speed
                else:
                    How_many_grams_were_eaten = 15 * eating_speed

                for i in range(100):
                    print_progress_bar(i + 1, 100, prefix="偷吃中:", length=25)
                    t.sleep(How_many_minutes_were_eaten/1000)
                if not frsc:
                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.RESET + "]")
                    frsc = True
                    t.sleep(1)
                if not cnsc:
                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "看,看不清楚" + Fore.RESET + "]")
                    cnsc = True
                    t.sleep(1)
                prco(
                    "你的小鸡在" +
                    str(Manor_Lord_2) +
                    "的庄园偷吃了" +
                    str(How_many_minutes_were_eaten) +
                    "分钟，吃掉了" +
                    str(How_many_grams_were_eaten) +
                    "克饲料，就被" +
                    str(Manor_Lord_2) +
                    "赶了回来，因为你使用了隐身药剂，所以你的小鸡没被" +
                    str(Manor_Lord_2) +
                    "打到"
                , 4)
                feeds += How_many_grams_were_eaten
                prco("你又多了" + str(How_many_grams_were_eaten) + "克饲料", 4)

        elif What_to_do == "2":
            Whether_or_not_to_steal_it = r.choice(Stealing_probability)
            if Whether_or_not_to_steal_it == "T" and feeds >= 20:
                stolen_time += 1
                Manor_Lord_2 = r.choice(Manor_Lord_1)
                How_many_minutes_were_eaten = r.randint(15, 30)
                if 15 <= How_many_minutes_were_eaten < 20:
                    How_many_grams_were_eaten = 10 * eating_speed
                elif 20 < How_many_minutes_were_eaten < 25:
                    How_many_grams_were_eaten = 15 * eating_speed
                else:
                    How_many_grams_were_eaten = 20 * eating_speed
                prco(
                    str(Manor_Lord_2) +
                    "的小鸡在你的的庄园偷吃了" +
                    str(How_many_minutes_were_eaten) +
                    "分钟，吃掉了" +
                    str(How_many_grams_were_eaten) +
                    "克饲料"
                , 1)
                feeds -= How_many_grams_were_eaten
                if not stol:
                    prco("\a获得成就[" + Fore.LIGHTYELLOW_EX + "黑吃黑？" + Fore.RESET + "]")
                    stol = True
                    t.sleep(0.5)
                elif not eate and stolen_time >= 10:
                    prco("\a获得成就[" + Fore.LIGHTMAGENTA_EX + "黑吃黑,我是被吃的" + Fore.RESET + "]")
                    eate = True
                    t.sleep(0.5)
                t.sleep(0.5)
            else:
                stolen_time = 0
                prco('你的庄园很好，什么都没有发生', 4)
                t.sleep(0.5)

        elif What_to_do == "3":
            if corn_needs == 0:
                prco("你还没有种子呢！快去购买吧！", 1)
                t.sleep(0.5)
            else:
                prco("你有" + str(corn_needs) + "个种子", 5)
                try:
                    How_much_to_plant = int(input(Fore.BLUE + "你要种多少玉米？" + Fore.RESET))
                except ValueError:
                    prco("额，看来你不想种玉米", 1)
                else:
                    if How_much_to_plant > corn_needs != 0:
                        prco("你还没有那么多种子呢！快去买吧！", 5)
                    elif How_much_to_plant > corn_needs == 0:
                        prco("你还没有玉米种子呢！快去买吧！", 5)
                    elif How_much_to_plant <= corn_needs and How_much_to_plant != 0:
                        corn_needs -= How_much_to_plant
                        if How_much_to_plant < 10:
                            Corn_that_grows = r.randint(0, How_much_to_plant)
                        else:
                            Corn_that_grows = r.randint(How_much_to_plant-10, How_much_to_plant)
                        corns += Corn_that_grows

                        for i in range(100):
                            print_progress_bar(i + 1, 100, prefix="播种中:", length=25)
                            t.sleep(How_much_to_plant/1000)
                        if Corn_that_grows > 0:
                            prco("你种了" + str(How_much_to_plant) + "个玉米种子,长出来了" + str(Corn_that_grows) + "个", 4)
                        else:
                            prco("你种了" + str(How_much_to_plant) + "个玉米种子,但一个都没有长出来", 1)
                    elif How_much_to_plant == 0:
                        prco("你去地里逛了一圈，什么都没干")
                        t.sleep(1)
        elif What_to_do == "4":
            clear()

            while True:
                if not figo and golds > 5:
                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "第一桶金" + Fore.RESET + "]")
                    figo = True
                    t.sleep(0.5)

                if not pogo and golds >= 50:
                    prco("\a获得成就[" + Fore.LIGHTYELLOW_EX + "真的是一桶金" + Fore.RESET + "]")
                    pogo = True

                showmenu("shopmenu")
                Why = input(Fore.BLUE + "你要做什么买卖？" + Fore.RESET)
                if Why == "1":
                    prco("5克饲料=1个金币", 5)
                    prco("你有" + str(feeds) + "克饲料", 5)
                    try:
                        How_much_feed_to_buy = int(input(Fore.BLUE + "你要卖多少饲料？" + Fore.RESET))
                    except ValueError:
                        prco("客人不知道你要干嘛，你什么都没卖出去", 1)
                    else:
                        if int(How_much_feed_to_buy) < 0:
                            prco("老板把你赶了出去", 1)
                        elif How_much_feed_to_buy != 0:
                            if How_much_feed_to_buy >= 5:
                                if feeds >= How_much_feed_to_buy:
                                    How_much_feed_to_buy -= How_much_feed_to_buy % 5
                                    feeds -= int(
                                        How_much_feed_to_buy
                                    )
                                    golds += int(How_much_feed_to_buy) / 5
                                    prco("你获得了了" + str(int(How_much_feed_to_buy) / 5) + "个金币", 4)
                                    if not deal:
                                        prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                        deal = True
                                        t.sleep(1)
                                    transactions_time += 1
                                else:
                                    prco("你还没有那么多饲料！", 1)
                            else:
                                prco("你卖得太少了，试着买多一点吧", 1)
                        else:
                            prco("你去商店逛了一圈，什么都没卖", 3)
                elif Why == "2":
                    prco("1张加速卡=1个金币", 5)
                    prco("你现在有" + str(golds) + "个金币", 5)
                    try:
                        How_many_acceleration_cards_to_buy = int(input(Fore.BLUE + "你要买多少加速卡：" + Fore.RESET))
                    except ValueError:
                        prco("老板把你赶了出去", 1)
                    else:
                        if int(How_many_acceleration_cards_to_buy) > int(golds):
                            if golds == 0:
                                prco("你现在没有金币哦！", 1)
                            else:
                                prco("你的金币还不够哦！你现在只有" + str(golds) + "个金币", 1)
                        elif int(How_many_acceleration_cards_to_buy) < 0:
                            prco("老板把你赶了出去", 1)
                        elif int(How_many_acceleration_cards_to_buy) <= int(golds) and How_many_acceleration_cards_to_buy != 0:
                            accelerator_cards += int(How_many_acceleration_cards_to_buy)
                            golds -= int(How_many_acceleration_cards_to_buy)
                            prco("你获得了" + str(How_many_acceleration_cards_to_buy) + "个加速卡", 4)
                            if not deal:
                                prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                deal = True
                                t.sleep(1)
                            transactions_time += 1
                        elif How_many_acceleration_cards_to_buy == 0:
                            prco("你去商店逛了一圈，什么都没买")
                elif Why == "3":
                    prco("你现在有" + str(golds) + "个金币", 5)
                    prco("1瓶隐身药剂=15个金币", 5)
                    try:
                        How_much_stealth_potion_to_buy = int(input(Fore.BLUE + "你要买多少隐身药剂？" + Fore.RESET))
                    except ValueError:
                        prco("老板把你赶了出去", 1)
                    else:
                        if int(How_much_stealth_potion_to_buy) < 0:
                            prco("老板把你赶了出去", 1)
                        elif How_much_stealth_potion_to_buy == 0:
                            prco("你去商店逛了一圈，什么都没买", 3)
                        elif How_much_stealth_potion_to_buy * 15 > golds:
                            prco("你的金币还不够哦！", 1)
                        elif How_much_stealth_potion_to_buy * 15 <= golds:
                            golds -= How_much_stealth_potion_to_buy * 15
                            stealth_potions += How_much_stealth_potion_to_buy
                            prco("你获得了" + str(How_much_stealth_potion_to_buy) + "个隐身药剂", 4)
                            if not deal:
                                prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                deal = True
                                t.sleep(1)
                            transactions_time += 1
                elif Why == "4":
                    prco("加工5克玉米饲料=5个金币和1个玉米", 5)
                    prco("你现在有" + str(golds) + "个金币和" + str(corns) + "个玉米", 5)
                    try:
                        How_many_acceleration_corn_feeds_to_process = int(input(Fore.BLUE + "你要加工多少份玉米饲料：" + Fore.RESET))
                    except ValueError:
                        prco("老板把你赶了出去", 1)
                    else:
                        if int(How_many_acceleration_corn_feeds_to_process < 0):
                            prco("老板把你赶了出去", 1)
                        elif How_many_acceleration_corn_feeds_to_process != 0:
                            if int(golds) < How_many_acceleration_corn_feeds_to_process * 5:
                                if golds == 0:
                                    prco("你现在没有金币哦！", 1)
                                else:
                                    prco("你的金币还不够哦！你现在只有" + str(golds) + "个金币", 1)
                            elif int(corns) < How_many_acceleration_corn_feeds_to_process:
                                if corns == 0:
                                    prco("你现在没有玉米哦！", 1)
                                else:
                                    prco("你的玉米还不够哦！你现在只有" + str(corns) + "个金币", 1)
                            elif How_many_acceleration_corn_feeds_to_process * 5 <= int(golds) and How_many_acceleration_corn_feeds_to_process <= int(corns) and How_many_acceleration_corn_feeds_to_process != 0:
                                corn_feeds += int(How_many_acceleration_corn_feeds_to_process) * 5
                                golds -= How_many_acceleration_corn_feeds_to_process * 5
                                corns -= How_many_acceleration_corn_feeds_to_process
                                prco("你获得了" + str(How_many_acceleration_corn_feeds_to_process * 5) + "克玉米饲料", 4)
                                if not deal:
                                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                    deal = True
                                    t.sleep(1)
                                transactions_time += 1
                        else:
                            prco("你去商店逛了一圈，什么都没买")
                elif Why == "5":
                    prco("你有" + str(golds) + "个金币", 5)
                    prco("1个玉米种子=5个金币", 5)
                    try:
                        How_many_corn_seeds_to_buy = int(input(Fore.BLUE + "你要买多少玉米种子？" + Fore.RESET))
                    except ValueError:
                        prco("老板把你赶了出去", 1)
                    else:
                        if int(How_many_corn_seeds_to_buy) < 0:
                            prco("老板把你赶了出去", 1)
                        elif How_many_corn_seeds_to_buy != 0:
                            if How_many_corn_seeds_to_buy * 5 > golds:
                                prco("你的金币还不够哦！", 1)
                            elif How_many_corn_seeds_to_buy * 5 <= golds:
                                golds -= How_many_corn_seeds_to_buy * 5
                                corn_needs += How_many_corn_seeds_to_buy
                                prco("你获得了" + str(How_many_corn_seeds_to_buy) + "个玉米种子", 4)
                                if not deal:
                                    prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                    deal = True
                                    t.sleep(1)
                                transactions_time += 1
                        else:
                            prco("你去商店逛了一圈，什么都没买", 3)
                elif Why == "6":
                    prco("你有" + str(corns) + "个玉米", 5)
                    prco("1个玉米=10个金币", 5)
                    try:
                        How_much_corn = int(input(Fore.BLUE + "你要卖多少玉米？" + Fore.RESET))
                    except ValueError:
                        prco("客人不知道你要干嘛，你什么都没卖出去", 1)
                    else:
                        if int(How_much_corn) < 0:
                            prco("老板把你赶了出去", 1)
                        elif How_much_corn == 0:
                            prco("你去商店逛了一圈，什么都没卖", 3)
                        elif corns < How_much_corn:
                            prco("你还没有那么多玉米哦！", 1)
                        elif corns >= How_much_corn:
                            golds += How_much_corn * 10
                            corns -= How_much_corn
                            prco("你获得了" + str(How_much_corn * 10) + "个金币", 4)
                            if not deal:
                                prco("\a获得成就[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.RESET + "]")
                                deal = True
                                t.sleep(1)
                            transactions_time += 1
                elif Why == "0":
                    clear() #退出
                    break

        elif What_to_do == "5":
            prco("金币 = " + str(golds), 5)
            prco("饲料 = " + str(feeds), 5)
            prco("玉米饲料 = " + str(corn_feeds), 5)
            print()
            prco("加速卡 = " + str(accelerator_cards), 5)
            prco("隐身药剂 = " + str(stealth_potions), 5)
            print()
            prco("玉米 = " + str(corns), 5)
            prco("玉米种子 = " + str(corn_needs), 5)
            t.sleep(2)

        elif What_to_do == "6":
            # 普通
            if neco:
                neco_status = "[" + Fore.LIGHTGREEN_EX + "初来乍到" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                neco_status = "[????????]"

            if frsc:
                frsc_status = "[" + Fore.LIGHTGREEN_EX + "白手起家" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                frsc_status = "[????????]"

            if figo:
                figo_status = "[" + Fore.LIGHTGREEN_EX + "第一桶金" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                figo_status = "[????????]"

            if deal:
                deal_status = "[" + Fore.LIGHTGREEN_EX + "成交！" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                deal_status = "[??????]"

            if coon:
                coon_status = "[" + Fore.LIGHTGREEN_EX + "撸起袖子加油吃" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                coon_status = "[??????????????]"

            if cnsc:
                cnsc_status = "[" + Fore.LIGHTGREEN_EX + "看，看不清楚" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                cnsc_status = "[????????????]"
            # 高级
            if aoag:
                aoag_status = "[" + Fore.LIGHTYELLOW_EX + "我会玩了" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                aoag_status = "[????????]"

            if cost:
                cost_status = "[" + Fore.LIGHTYELLOW_EX + "什么都是有代价的" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                cost_status = "[????????????????]"

            if stol:
                stol_status = "[" + Fore.LIGHTYELLOW_EX + "黑吃黑？" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                stol_status = "[????????]"

            if prof:
                prof_status = "[" + Fore.LIGHTYELLOW_EX + "专业小偷" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                prof_status = "[????????]"

            if pope:
                pope_status = "[" + Fore.LIGHTMAGENTA_EX + "礼貌问候" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                pope_status = "[????????]"

            if pogo:
                pogo_status = "[" + Fore.LIGHTYELLOW_EX + "真的是一桶金" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                pogo_status = "[????????????]"

            if pref:
                pref_status = "[" + Fore.LIGHTYELLOW_EX + "老顾客，有优惠吗？" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                pref_status = "[??????????????????]"
            # 挑战
            if soha:
                soha_status = "[" + Fore.LIGHTMAGENTA_EX + "来点更难的？" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                soha_status = "[????????????]"
            if moex:
                moex_status = "[" + Fore.LIGHTMAGENTA_EX + "小偷院长" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                moex_status = "[????????]"

            if golu:
                golu_status = "[" + Fore.LIGHTMAGENTA_EX + "欧皇圣体" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                golu_status = "[????????]"

            if balu:
                balu_status = "[" + Fore.LIGHTMAGENTA_EX + "天生非酋体质" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                balu_status = "[????????????]"

            if eate:
                eate_status = "[" + Fore.LIGHTMAGENTA_EX + "黑吃黑，我是被吃的" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                eate_status = "[??????????????????]"

            if mmod:
                mmod_status = "[" + Fore.LIGHTMAGENTA_EX + "真的是小偷！" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                mmod_status = "[??????????]"

            if ripe:
                ripe_status = "[" + Fore.LIGHTMAGENTA_EX + "大富翁" + Fore.LIGHTWHITE_EX + "]" + Fore.RESET
            else:
                ripe_status = "[??????]"

            accomplishment = f"""
{neco_status}─────{frsc_status}─┬───{coon_status}─────{cnsc_status}
                          ╰───{deal_status}─────{figo_status}

                                                    ╔═════{pogo_status}
{aoag_status}═════{cost_status}═════{stol_status}════╬═════{prof_status}
                                                    ╚═════{pref_status}

                  ┏━━━━━{golu_status}━━━━━{balu_status}━━━━━{eate_status}
{soha_status}━━━━╋━━━━━{moex_status}
                  ┗━━━━━{ripe_status}━━━━━{mmod_status}━━━━━{pope_status}
                                               """
            print(accomplishment)

        elif What_to_do == "7":
            if chick_level == 30:
                prco("小鸡已经升到满级了！", 1)
            else:
                prco("小鸡现在的等级是" + str(chick_level) + "LV\n", 5)
                print(str(chick_level) + "LV ──> " + Fore.LIGHTGREEN_EX + str(chick_level+1) + "LV\n" + Fore.RESET)
                prco("这次升级需要" + str((chick_level+1) * 5) + "克玉米饲料", 5)
                if corn_feeds != 0:
                    prco("你现在有" + str(corn_feeds) + "克玉米饲料", 5)
                    showmenu("selectivemenu1")
                    Whether_to_upgrade = input(Fore.BLUE + "确定要升级吗？" + Fore.RESET)
                    if Whether_to_upgrade == "1":
                        if corn_feeds >= chick_level * 5:
                            for i in range(100):
                                print_progress_bar(i + 1, 100, prefix="升级中:", length=25)
                                t.sleep((chick_level+1)/100)
                            corn_feeds -= (chick_level+1) * 5
                            chick_level += 1
                            prco("小鸡升级到了" + str(chick_level) + "LV，偷吃的速度变增加了" + str(round(round(Get_speed[chick_level-1], 3)*100)) + "%", 4)
                        elif corn_feeds < chick_level * 5:
                            prco("你的玉米饲料还不够哦！快去加工吧！", 1)
                else:
                    prco("你还没有玉米饲料哦！快去加工吧！", 1)

        elif What_to_do == "8":
            showmenu("moremenu")
            moreoptions = input(Fore.BLUE + "请选择：" + Fore.RESET)
            if moreoptions == "1":
                prco(about, 3)
            elif moreoptions == "2":
                if o.name == "nt":
                    o.system("start https://ejkdn.github.io/XJZY-Wiki/")
                    prco("已打开浏览器", 4)
                else:
                    prco("把这个链接复制到浏览器打开：https://ejkdn.github.io/XJZY-Wiki/")
            elif moreoptions == "3":
                if o.name == "nt":
                    o.system("start https://gitee.com/PSWG/XJZY/")
                    prco("已打开浏览器", 4)
                else:
                    prco("把这个链接复制到浏览器打开：https://gitee.com/PSWG/XJZY/")
            elif moreoptions == "4":
                prco(copyright, 3)

        elif What_to_do == "db": #调试模式
            showmenu("debugmenu")
            opendebug = input(Fore.BLUE + "请选择开启项目：" + Fore.RESET)
            if opendebug == "1":
                savedate = True
                prco("已开启数据保存功能", 4)
                t.sleep(1)

            elif opendebug == "2":
                savedate = False
                prco("已关闭数据保存功能", 4)
                t.sleep(1)

            elif opendebug == "3":
                showmenu("selectivemenu1")
                cleardate = input(Fore.BLUE + "确定要清除数据吗？" + Fore.RESET)
                if cleardate == "1":
                    golds = 5
                    stealth_potions = 0
                    feeds = 10
                    corn_feeds = 0
                    accelerator_cards = 0
                    corns = 0
                    corn_needs = 0
                    chick_level = 0
                    eating_speed = 1

                    # 普通
                    neco = True #[初来乍到]
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

                    thefts_time = 0 # 偷吃的次数
                    transactions_time = 0 # 交易的次数
                    stolen_time = 0 # 被偷吃的次数
                    bullied_time = 0 # 被打的次数
                    not_bullied_time = 0 # 没被打的次数
                    prco("清除完成。", 4)
            elif opendebug == "4":
                showmenu("selectivemenu1")
                deletedate = input(Fore.BLUE + "确定要删除数据吗？" + Fore.RESET)
                if deletedate == "1":
                    data_pack = {
                        "golds":golds,
                        "stealth_potions":stealth_potions,
                        "feeds":feeds,
                        "corn_feeds":corn_feeds,
                        "accelerator_cards":accelerator_cards,
                        "corns":corns,
                        "corn_needs":corn_needs,
                        "chick_level":chick_level,
                        "neco":neco,
                        "frsc":frsc,
                        "figo":figo,
                        "deal":deal,
                        "coon":coon,
                        "cnsc":cnsc,
                        "aoag":aoag,
                        "stol":stol,
                        "cost":cost,
                        "prof":prof,
                        "pope":pope,
                        "pogo":pogo,
                        "pref":pref,
                        "soha":soha,
                        "moex":moex,
                        "golu":golu,
                        "balu":balu,
                        "eate":eate,
                        "mmod":mmod,
                        "ripe":ripe,
                        "thefts_time":thefts_time,
                        "transactions_time":transactions_time
                    }
                    write_data(version, data_pack)
                    savedate = False
                    if o.path.exists(f"XJZY-{version}.pkl"):
                        o.remove(f"XJZY-{version}.pkl")
                        prco("\a删除完成，请重启游戏。", 4)
                    else:
                        prco("找不到数据库文件", 1)

        elif What_to_do == "你好":
            if not pope:
                prco("你好，有什么事吗？")
                t.sleep(0.5)
                prco("\a获得成就[" + Fore.LIGHTMAGENTA_EX + "礼貌问候" + Fore.RESET + "]")
                pope = True
                t.sleep(0.5)
            else:
                prco("\a你好，有什么事吗？")
                t.sleep(1)

        elif What_to_do == "0":
            if savedate:
                # ↓保存数据
                data_pack = {
                    "golds":golds,
                    "stealth_potions":stealth_potions,
                    "feeds":feeds,
                    "corn_feeds":corn_feeds,
                    "accelerator_cards":accelerator_cards,
                    "corns":corns,
                    "corn_needs":corn_needs,
                    "chick_level":chick_level,
                    "neco":neco,
                    "frsc":frsc,
                    "figo":figo,
                    "deal":deal,
                    "coon":coon,
                    "cnsc":cnsc,
                    "aoag":aoag,
                    "stol":stol,
                    "cost":cost,
                    "prof":prof,
                    "pope":pope,
                    "pogo":pogo,
                    "pref":pref,
                    "soha":soha,
                    "moex":moex,
                    "golu":golu,
                    "balu":balu,
                    "eate":eate,
                    "mmod":mmod,
                    "ripe":ripe,
                    "thefts_time":thefts_time,
                    "transactions_time":transactions_time
                }
                write_data(version, data_pack)

            logo(version, "end")
            t.sleep(2)

            clear()
            break #退出循环，结束程序
        else:
            clear()

if __name__ == "__main__":
    XJZY("2.9Beta8", "更优雅的加密和响应式菜单！") #调用主函数
