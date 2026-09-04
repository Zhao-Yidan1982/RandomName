import random
import math
from mode.wrong import *
from mode.personinfo import PersonInfo
from mode.other import is_integer

#定义1.单人姓名抽取函数
def single_name_pick(all_info:list[PersonInfo])-> None:
    #信息提取
    no_data = False
    if all_info[0].name is None:
        print_warning(no_name)
        no_data = True
    if no_data:
        return
    
    name_list:list = []
    for info in all_info:
        name_list.append(info.name)
    #功能逻辑
    while True:
        mode_input = input('请按回车键抽取姓名\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            sys.exit(normal_exit)
        elif mode_input == "quit":
            break
        print()
        print(random.choice(name_list))
        print()

#定义2.多人姓名抽取函数
def multiple_name_pick(all_info:list[PersonInfo])-> None:
    #信息提取
    no_data = False
    if all_info[0].name is None:
        print_warning(no_name)
        no_data = True
    if no_data:
        return

    name_list:list = []
    for info in all_info:
        name_list.append(info.name)

    #功能逻辑
    while True:
        mode_input = input('请输入抽取姓名个数\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            sys.exit(normal_exit)
        elif mode_input == "quit":
            break

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
            print(*name_list[:num])
        else:
            print_warning(f"姓名数量不足,仅{len(name_list)}个,无法抽取")
            print('\n')

#定义3.单人编号抽取函数
def single_number_pick(all_info:list[PersonInfo])-> None:
    #信息提取
    no_data = False
    if all_info[0].number is None:
        print_warning(no_number)
        no_data = True
    if no_data:
        return

    num_list:list = []
    for info in all_info:
        num_list.append(info.number)

    #功能逻辑
    while True:
        mode_input = input('请按回车键抽取编号\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            sys.exit(normal_exit)
        elif mode_input == "quit":
            break
        print()
        print(random.choice(num_list))
        print()

#定义4.多编号抽取函数
def multiple_number_pick(all_info:list[PersonInfo])-> None:
    #信息提取
    no_data = False
    if all_info[0].number is None:
        print_warning(no_number)
        no_data = True
    if no_data:
        return
    
    num_list:list = []
    for info in all_info:
        num_list.append(info.number)
    
    #功能逻辑
    while True:
        mode_input = input('请输入抽取编号数量\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            sys.exit(normal_exit)
        elif mode_input == "quit":
            break

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
        elif num <= len(num_list):
            random.shuffle(num_list)
            for i in num_list[:num]:
                print(i,end=" ")
            print("\n")
        else:
            print_warning(f"编号数量不足,仅{len(num_list)}个,无法抽取")
            print('\n')

#定义5.单人性别选择姓名抽取函数
def single_gender_select_name_pick(all_info:list[PersonInfo])-> None:
    #信息提取
    no_data = False
    if all_info[0].name is None:
        print_warning(no_name)
        no_data = True
    if all_info[0].sex is None:
        print_warning(no_sex)
        no_data = True
    if no_data:
        return

    male_name_list:list = []
    female_name_list:list = []
    for info in all_info:
        if info.sex:
            male_name_list.append(info.name)
        else:
            female_name_list.append(info.name)
        
    #功能逻辑
    while True:
        sex_choice = input('输入"a"抽取男性,"b"抽取女性\n输入其他内容抽取全部，输入"exit"退出运行,"quit"重新选择模式:')
        print()
        if sex_choice == "exit":
            sys.exit(normal_exit)
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

#定义6.多人性别选择姓名抽取函数
def multiple_gender_select_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义7.单人性别选择编号抽取函数
def single_gender_select_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义8.多人性别选择编号抽取函数
def multiple_gender_select_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义9.单人权重姓名抽取函数
def single_weighted_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"
    
#定义10.多人权重姓名抽取函数
def multiple_weighted_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义11.单人权重编号抽取函数
def single_weighted_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义12.多人权重编号抽取函数
def multiple_weighted_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义13.单人权重性别选择姓名抽取函数
def single_weighted_gender_select_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义14.多人权重性别选择姓名抽取函数
def multiple_weighted_gender_select_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义15.单人权重性别选择编号抽取函数
def single_weighted_gender_select_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义16.多人权重性别选择编号抽取函数
def multiple_weighted_gender_select_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义17.单人动态权重姓名抽取函数
def single_dynamic_weighted_name_pick(all_info:list[PersonInfo])-> None:
    #信息提取
    no_data:bool = False 
    if all_info[0].name is None:
        print_warning(no_name)
        no_data = True
    if all_info[0].weight is None:
        print_warning(no_weight)
        no_data = True
    if no_data:
        return
    
    name_list:list = []
    weight_list:list = []
    for info in all_info:
        name_list.append(info.name)
        weight_list.append(info.weight)

    if any(weight < 0 for weight in weight_list) or sum(weight_list) <= 0:
        print_warning('权重必须为非负数且总和大于零')
        return
    
        #功能逻辑
    while True:
        _:bool = False
        for i in weight_list:
            if i <= 100:
                _:bool = True
        if _:
            for i in range(len(all_info)):
                weight_list[i] = 1000 * weight_list[i]

        mode_input = input('请按回车键抽取姓名\n或输入"exit"退出运行,"quit"重新选择模式')
        if mode_input == "exit":
            sys.exit(normal_exit)
        elif mode_input == "quit":
            break
        else:
            rand_val = random.choices(range(len(all_info)), weights=weight_list, k=1)[0]
            print()
            print(name_list[rand_val])
            weight_list[rand_val] = int(math.sqrt(weight_list[rand_val]))
            print()

#定义18.多人动态权重姓名抽取函数
def multiple_dynamic_weighted_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义19.单人动态权重编号抽取函数
def single_dynamic_weighted_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义20.多人动态权重编号抽取函数
def multiple_dynamic_weighted_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义21.单人动态权重性别选择姓名抽取函数
def single_dynamic_weighted_gender_select_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义22.多人动态权重性别选择姓名抽取函数
def multiple_dynamic_weighted_gender_select_name_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义23.单人动态权重性别选择编号抽取函数
def single_dynamic_weighted_gender_select_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"

#定义24.多人动态权重性别选择编号抽取函数
def multiple_dynamic_weighted_gender_select_number_pick(all_info:list[PersonInfo])-> None:
    assert False, "模式未完成，敬请期待"
