def prco(text, color=3):
    from colorama import init, Fore
    init()

    if color == 1:
        print(Fore.RED + text + Fore.RESET) #red:坏、失败、错误
    elif color == 2:
        print(Fore.CYAN + text + Fore.RESET) #blue:菜单
    elif color == 3:
        print(Fore.WHITE + text + Fore.RESET) #white:普通
    elif color == 4:
        print(Fore.GREEN + text + Fore.RESET) #green:好、成功
    elif color == 5:
        print(Fore.YELLOW + text + Fore.RESET) #yellow:提示、旁白
    pass

# prco("hello color!")
# prco("你好，颜色！")