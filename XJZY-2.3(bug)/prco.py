def prco(text, color=3):
    """
    1、red.\n
    2、cyan.\n
    3、white.\n
    4、green.\n
    5、yellow.\n
    """
    from colorama import init, Fore
    init()

    if color == 1:
        print(Fore.RED + text + Fore.RESET) #red:坏、失败、错误
    elif color == 2:
        print(Fore.CYAN + text + Fore.RESET) #cyan:菜单
    elif color == 3:
        print(Fore.WHITE + text + Fore.RESET) #white:普通
    elif color == 4:
        print(Fore.GREEN + text + Fore.RESET) #green:好、成功
    elif color == 5:
        print(Fore.YELLOW + text + Fore.RESET) #yellow:提示、旁白
    elif color == 6:
        print(Fore.BLUE + text + Fore.RESET) #blue:选择