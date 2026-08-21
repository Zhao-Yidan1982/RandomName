import random

#定义错误提示函数
def print_warning(message):
    print(f"Warning:{message}!!\n")
def print_error(message):
    print(f"Error:{message}!!!\n")

#定义判断是否为整数的函数
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#定义身份信息class
class PeopleInfo:
    def __init__(self, \
                _number:(int|None) = None,\
                _name:(str|None) = None, \
                _sex:(bool|None) = None, \
                _weight:(int|None) = None):
        
        self.number = _number
        self.name = _name
        self.sex = _sex
        self.weight = _weight

#定义1.单人姓名抽取函数
def single_name_pick(all_info:list[PeopleInfo])-> None:
    #信息提取
    name_list:list = []
    for info in all_info:
        name_list.append(info.name)
    #功能逻辑
    while True:
        mode_input = input('请按回车键抽取姓名\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            exit()
        elif mode_input == "quit":
            break
        print()
        print(random.choice(name_list))
        print()

#定义2.多人姓名抽取函数
def multiple_name_pick(all_info:list[PeopleInfo])-> None:
    #信息提取
    name_list:list = []
    for info in all_info:
        name_list.append(info.name)

    #功能逻辑
    while True:
        mode_input = input('请按回车键抽取姓名\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            exit()
        elif mode_input == "quit":
            break
        print()
        print(random.choice(name_list))
        print()
        num = 0
        if mode_input == "":
            num = 1
        else:
            try:
                num = int(mode_input)
            except ValueError:
                print_warning('请输入整数')
                continue
        print()
        if num <= 0:
            print_warning("请输入正整数")
        elif num <= len(name_list):
            random.shuffle(name_list)
            for i in name_list[:num]:
                print(i,end=" ")
            print("\n")
        else:
            print_warning(f"姓名数量不足,仅{len(name_list)}个,无法抽取")
            print('\n')

#定义3.单人编号抽取函数
def single_number_pick(all_info:list[PeopleInfo])-> None:
    #信息提取
    num_list:list = []
    for info in all_info:
        num_list.append(info.number)

    #功能逻辑
    while True:
        mode_input = input('请按回车键抽取编号\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            exit()
        elif mode_input == "quit":
            break
        print()
        print(random.choice(num_list))
        print()

#定义4.多编号抽取函数
def multiple_number_pick(all_info:list[PeopleInfo])-> None:
    #信息提取
    num_list:list = []
    for info in all_info:
        num_list.append(info.number)
    
    #功能逻辑
    while True:
        mode_input = input('请按回车键抽取编号\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            exit()
        elif mode_input == "quit":
            break
        print()
        print(random.choice(num_list))
        print()
        num = 0
        if mode_input == "":
            num = 1
        else:
            try:
                num = int(num)
            except ValueError:
                print_warning('请输入整数')
                continue
        print()
        if num <= 0:
            print_warning("请输入正整数")
        elif num <= len(num_list):
            random.shuffle(num_list)
            for i in num_list[:num]:
                print(i,end=" ")
            print("\n")
        else:
            print_warning(f"编号数量不足,仅{len(num_list)}个,无法抽取")
            print('\n')

#定义5.单人性别选择姓名抽取函数
def single_gender_select_name_pick(all_info:list[PeopleInfo])-> None:
    #信息提取
    male_name_list:list = []
    female_name_list:list = []
    for info in all_info:
        if info.sex:
            male_name_list.append(info.number)
        else:
            female_name_list.append(info.name)
        
    #功能逻辑
    while True:
        sex_choice = input('默认为全部,a为仅男性,b为仅女性\n请选择抽取范围或\n输入"exit"退出运行,"quit"重新选择模式:')
        print()
        if sex_choice == "exit":
            exit()
        elif sex_choice == "quit":
            break
        elif sex_choice == "a":
            if male_name_list != []:
                print(random.choice(male_name_list))
                print()
            else:
                print_warning("无男性数据")
        elif sex_choice == "b":
            if female_name_list != []:
                print(random.choice(female_name_list))
                print()
            else:
                print_warning("无女性数据")
        else:
            print(random.choice(male_name_list + female_name_list))
            print()

def multiple_gender_select_name_pick():
    ...
def single_gender_select_number_pick():
    ...
def multiple_gender_select_number_pick():
    ...
def single_weighted_name_pick():
    ...
def multiple_weighted_name_pick():
    ...
def single_weighted_number_pick():
    ...
def multiple_weighted_number_pick():
    ...
def single_weighted_gender_select_name_pick():
    ...
def multiple_weighted_gender_select_name_pick():
    ...
def single_weighted_gender_select_number_pick():
    ...
def multiple_weighted_gender_select_number_pick():
    ...
def single_dynamic_weighted_name_pick():
    ...
def multiple_dynamic_weighted_name_pick():
    ...
def single_dynamic_weighted_number_pick():
    ...
def multiple_dynamic_weighted_number_pick():
    ...
def single_dynamic_weighted_gender_select_name_pick():
    ...
def multiple_dynamic_weighted_gender_select_name_pick():
    ...
def single_dynamic_weighted_gender_select_number_pick():
    ...
def multiple_dynamic_weighted_gender_select_number_pick():
    ...