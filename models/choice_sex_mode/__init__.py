import random

#定义性别选择模式函数
def choice_sex_mode(male_name:list, female_name:list,include_sex:bool):
    #定义错误提示函数
    def print_error(message):
        print(f"error:{message}!!\n")
    def print_wrong(message):
        print(f"wrong:{message}!!!\n")
    
    #定义性别选择模式函数逻辑
    while True:
        if not include_sex:
            print_wrong("无性别数据无法使用此模式")
            break
        sex_choice = input('默认为全部,male为仅男性,female为仅女性\n请选择抽取范围或\n输入"exit"退出运行,"quit"重新选择模式:')
        print()
        if sex_choice == "exit":
            exit()
        elif sex_choice == "quit":
            break
        elif sex_choice == "male":
            if male_name:
                print(random.choice(male_name))
                print()
            else:
                print_error("无男性数据")
        elif sex_choice == "female":
            if female_name:
                print(random.choice(female_name))
                print()
            else:
                print_error("无女性数据")
        else:
            print(random.choice(male_name + female_name))
            print()
    
    
    
    
    