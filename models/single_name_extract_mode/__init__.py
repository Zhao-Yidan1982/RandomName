import random

#定义单姓名抽取模式函数
def single_name_extract_mode(all_name:list):
    while True:
        mode_input = input('请按回车键抽取姓名\n或输入"exit"退出运行"quit"重新选择模式')
        if mode_input == "exit":
            exit()
        elif mode_input == "quit":
            break
        print()
        print(random.choice(all_name))
        print()