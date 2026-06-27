import random

#定义单编号抽取模式函数
def single_number_extract_mode(num_list:list):
    while True:
        mode_input = input('请按回车键抽取编号\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            exit()
        elif mode_input == "quit":
            break
        print()
        print(random.choice(num_list))
        print()