#!/usr/bin/python3

import json

#导入模块化模式函数
from models import *

#版本信息
VERSION_INFO = {
    "version": "1.1.0",
    "update_date": "2026-6-27",
    "update_info": [
        "【改进】优化了报错逻辑",
        "【改进】重构了部分代码结构",
        "【改进】修复了部分bug",
        "【功能】添加了多数据库读取功能",
        "【功能】添加了Linux源代码运行脚本"
        ],
    "other": "work in progress"
}

def about():
    print()
    print("版本信息:")
    print(f"    version:{VERSION_INFO['version']}")
    print(f"    update_date:{VERSION_INFO['update_date']}")
    print(f"    update_info:")
    for update_info in VERSION_INFO['update_info']:
        print(f"        {update_info}")
    print(f"    {VERSION_INFO['other']}")
    input("按回车键继续使用...")

#选择档案
filename = input("请输入要读取的数据库及其设置的名称(默认为default): ")
if filename == '':
    filename = "default"

#支持编码
encodings = ['utf-8', 'gbk']

#读取配置文件
for enc in encodings:
    try:
        with open(f"config/{filename}.json", "r", encoding="utf-8") as f:
            settings = json.load(f)
    except FileNotFoundError:
        print_error('配置文件不存在')
        input("请按回车键退出程序")
        exit()
    except PermissionError:
        print_error('无读取配置文件权限不足')
        input("请检查文件权限并按回车键退出程序")
        exit()
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            print_error('不支持此编码的配置文件')
            input("请使用GBK或UTF-8\n并按回车键退出运行")
            exit()

#读取数据
for enc in encodings:
    try:
        with open(f"nmls/{filename}", 'r', encoding=enc) as nmls:
            mnls_main = nmls.readlines()
        break  # 读取成功，跳出循环
    except FileNotFoundError:
        print_error('数据库文件不存在')
        input("请按回车键退出程序")
        exit()
    except PermissionError:
        print_error('无读取数据库文件权限不足')
        input("请检查文件权限并按回车键退出程序")
        exit()
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            print_error('不支持此编码的数据库文本')
            input("请使用GBK或UTF-8\n并按回车键退出运行")
            exit()


#删除行末换行符
for i in range(len(mnls_main)):
    mnls_main[i] = mnls_main[i][:-1]

#将数据初步分割
tmp_list = []
for i in mnls_main:
    tmp_list.append(i.split(','))

#分离数据
people_data:list = []
try:
    for people in tmp_list[settings["RowStart"]:settings["RowEnd"]]:
        number:int|None = int(people[settings["NumberColumn"]]) if settings["IncludeNumber"] else None
        name:str|None = str(people[settings["NameColumn"]]) if settings["IncludeName"] else None
        sex:bool|None = None
        if settings["IncludeSex"]:
            if "男" in people[settings["NameColumn"]] == "女" in people[settings["NameColumn"]]:
                print_error("性别数据不合法")
            if "男" in people[settings["NameColumn"]]:
                sex = True
            else:
                sex = False
        weight:int|None = int(people[settings["WeightColumn"]]) if settings["IncludeWeight"] else None

        people_data.append(PeopleInfo(number, name, sex, weight))
except IndexError:
    print_error('数据列不存在')
except ValueError:
    print_error('数据内容不合法')

mode_dict:dict = {
    '单人姓名抽取':single_name_pick,
    '多人姓名抽取':multiple_name_pick,
    '单人编号抽取':single_number_pick,
    '多人编号抽取':multiple_number_pick,
    '单人性别选择姓名抽取' :single_gender_select_name_pick,
    '多人性别选择姓名抽取' :multiple_gender_select_name_pick,
    '单人性别选择编号抽取' :single_gender_select_number_pick,
    '多人性别选择编号抽取' :multiple_gender_select_number_pick,
    '单人权重姓名抽取' :single_weighted_name_pick,
    '多人权重姓名抽取' :multiple_weighted_name_pick,
    '单人权重编号抽取' :single_weighted_number_pick,
    '多人权重编号抽取' :multiple_weighted_number_pick,
    '单人权重性别选择姓名抽取' :single_weighted_gender_select_name_pick,
    '多人权重性别选择姓名抽取' :multiple_weighted_gender_select_name_pick,
    '单人权重性别选择编号抽取' :single_weighted_gender_select_number_pick,
    '多人权重性别选择编号抽取' :multiple_weighted_gender_select_number_pick,
    '单人动态权重姓名抽取' :single_dynamic_weighted_name_pick,
    '多人动态权重姓名抽取' :multiple_dynamic_weighted_name_pick,
    '单人动态权重编号抽取' :single_dynamic_weighted_number_pick,
    '多人动态权重编号抽取' :multiple_dynamic_weighted_number_pick,
    '单人动态权重性别选择姓名抽取' :single_dynamic_weighted_gender_select_name_pick,
    '多人动态权重性别选择姓名抽取' :multiple_dynamic_weighted_gender_select_name_pick,
    '单人动态权重性别选择编号抽取' :single_dynamic_weighted_gender_select_number_pick,
    '多人动态权重性别选择编号抽取' :multiple_dynamic_weighted_gender_select_number_pick
}

#模式列表
mode_list = [
    '单人姓名抽取',
    '多人姓名抽取',
    '单人编号抽取',
    '多编号抽取模式',
    '单人性别选择姓名抽取'
]

#定义主逻辑
while True:
    for i in range(len(mode_list)):
        print(f"{i+1}.{mode_list[i]}模式")
    #选择模式
    mode = input("请输入您选择的模式编号或输入\"about\"或输入\"exit\"退出运行:")
    #主逻辑
    if mode == "about":
        about()
    elif mode == "exit":
        exit()
    else:
        if is_integer(mode) and mode_list[int(mode)] in list(mode_dict.keys()):
            mode_dict[mode_list[int(mode) - 1]](people_data)
        else:
            print_warning('未识别的模式编号')
            print('请重新选择模式')
