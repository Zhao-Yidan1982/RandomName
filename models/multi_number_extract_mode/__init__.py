import random

#定义多编号抽取模式函数
def multi_number_extract_mode(num_list:list):
    #定义错误提示函数
    def print_error(message):
        print(f"error:{message}!!\n")
    def print_wrong(message):
        print(f"wrong:{message}!!!\n")
    
    #定义多编号抽取模式函数逻辑
    while True:
        mode_input = input('请按回车键抽取编号\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            exit()
        elif mode_input == "quit":
            break
        print()
        print(random.choice(num_list))
        print()
        try:
            num = int(num)
        except ValueError:
            print_error('请输入整数')
            continue
        print()
        if num <= 0:
            print_error("请输入正整数")
        elif num <= len(num_list):
            random.shuffle(num_list)
            for i in num_list[:num]:
                print(i,end=" ")
            print("\n")
        else:
            print_error(f"编号数量不足,仅{len(num_list)}个,无法抽取")
            print('\n')