#!/usr/bin/python3
import random

#读取数据
encodings = ['utf-8', 'gbk']
for enc in encodings:
    try:
        nmls = open('usrfiles/nmls', 'r', encoding=enc)
        mnls_main = nmls.readlines()
        break  # 读取成功，跳出循环
    except FileNotFoundError:
        input("wrong:数据库文件不存在!!!\n请按回车键退出程序")
        exit()
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            input("wrong:不支持此编码的数据库文本!!!\n请使用GBK或UTF-8\n并按回车键退出运行")
            exit()
nmls.close()

#将数据初步分割
temp_list = []
for i in mnls_main:
    temp_list.append(i.split(','))

#定义三个乘员组
male_name = []
female_name = []
all_name = []

#判断是否有性别列是否正常
have_sex = True
for i in temp_list:
    if len(i) < 3 or \
        "男" in i[2] and "女" in i[2] or\
        "女" not in i[2] and "男" not in i[2]:
        print('error:数据库中性别标识或性别列位置不正确,将无法使用模式2!!')
        have_sex = False
        break

if have_sex:
    #对数据分类
    for i in temp_list:
        if "男" in i[2] and "女" not in i[2]:
            male_name.append(i[1])
        elif "女" in i[2] and "男" not in i[2]:
            female_name.append(i[1])
    all_name = male_name + female_name
    if not all_name:
        print("wrong:数据库为空!!!")
        input('请按回车键退出运行')
        exit()
    elif not male_name:
        print("error:无男性数据!!")
    elif not female_name:
        print("error:无女性数据!!")
else:
    del male_name,female_name
    for i in temp_list:
        all_name.append(i[1])
    if not all_name:
        print("wrong:数据库为空!!!")
        input('请按回车键退出运行')
        exit()

#提取编号
num_list = []
for i in temp_list:
    num_list.append(i[0])

#删除初步分类临时表
del temp_list

while True:
    #选择模式
    mode = input('1.单人抽取模式\n2.性别选择模式\n3.多人抽取模式\n4.单编号抽取模式\n5.多编号抽取模式\n请输入您选择的模式编号或输入"exit"退出运行:')
    #主逻辑
    if mode == "1":
        while True:
            mode_input = input('请按回车键抽取姓名\n或输入"exit"退出运行"quit"重新选择模式')
            if mode_input == "exit":
                exit()
            elif mode_input == "quit":
                break
            print()
            print(random.choice(all_name))
            print()
    elif mode == "2":
        while True:
            if not have_sex:
                print("error:无性别数据无法使用此模式!!")
                break
            sex_choice = input('默认为全部,male为仅男性,female为仅女性\n请选择抽取范围或\n输入"exit"退出运行"quit"重新选择模式:')
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
                    print("error:无男性数据!!")
            elif sex_choice == "female":
                if female_name:
                    print(random.choice(female_name))
                    print()
                else:
                    print("error:无女性数据!!")
            else:
                print(random.choice(all_name))
                print()
    elif mode == "3":
        while True:
            num = input('请选择抽取人数或\n输入"exit"退出运行"quit"重新选择模式:')
            if num == "exit":
                exit()
            elif num == "quit":
                break
            try:
                num = int(num)
            except ValueError:
                print('error:请输入整数!!')
                continue
            print()
            if num <= 0:
                print("error:请输入正整数!!\n")
            elif num <= len(all_name):
                random.shuffle(all_name)
                for i in all_name[:num]:
                    print(i,end=" ")
                print("\n")
            else:
                print(f"error:人数不足,仅{len(all_name)}人,无法抽取!!")
                print('\n')
    elif mode == "4":
        while True:
            mode_input = input('请按回车键抽取编号\n或输入"exit"退出运行"quit"重新选择模式')
            if mode_input == "exit":
                exit()
            elif mode_input == "quit":
                break
            print()
            print(random.choice(num_list))
            print()
    elif mode == "5":
        while True:
            num = input('请选择抽取编号数量或\n输入"exit"退出运行"quit"重新选择模式:')
            if num == "exit":
                exit()
            elif num == "quit":
                break
            try:
                num = int(num)
            except ValueError:
                print('error:请输入整数!!')
                continue
            print()
            if num <= 0:
                print("error:请输入正整数!!\n")
            elif num <= len(num_list):
                random.shuffle(num_list)
                for i in num_list[:num]:
                    print(i,end=" ")
                print("\n")
            else:
                print(f"error:编号数量不足,仅{len(num_list)}个,无法抽取!!")
                print('\n')
    elif mode == "exit":
        exit()
    else:
        print('error:未识别的模式编号!!\n请重新选择')