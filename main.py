#!/usr/bin/python3
import json

#导入模块化模式函数
from models import *

#定义判断是否为整数的函数
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

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
        print_wrong('配置文件不存在')
        input("请按回车键退出程序")
        exit()
    except PermissionError:
        print_wrong('无读取配置文件权限不足')
        input("请检查文件权限并按回车键退出程序")
        exit()
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            print_wrong('不支持此编码的配置文件')
            input("请使用GBK或UTF-8\n并按回车键退出运行")
            exit()

#读取数据
for enc in encodings:
    try:
        with open(f"nmls/{filename}", 'r', encoding=enc) as nmls:
            mnls_main = nmls.readlines()
        break  # 读取成功，跳出循环
    except FileNotFoundError:
        print_wrong('数据库文件不存在')
        input("请按回车键退出程序")
        exit()
    except PermissionError:
        print_wrong('无读取数据库文件权限不足')
        input("请检查文件权限并按回车键退出程序")
        exit()
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            print_wrong('不支持此编码的数据库文本')
            input("请使用GBK或UTF-8\n并按回车键退出运行")
            exit()

#将数据初步分割
tmp_list = []
for i in mnls_main:
    tmp_list.append(i.split(','))

#判断是否有性别列是否正确，并将数据分类

only_one_sex = False
if settings['IncludeSex']:
    #定义乘员组
    male_name = []
    female_name = []
    male_number = []
    female_number = []
    #对数据分类
    for i in tmp_list[settings['RowStart']:settings['RowEnd']]:
        if len(i) <= settings['SexColumn'] or \
        "男" in i[settings['SexColumn']] == "女" in i[settings['SexColumn']]:
            print_wrong("数据库性别设置不正确")
            input("请检查数据库性别列并按回车键退出运行")
            exit()
    for i in tmp_list[settings['RowStart']:settings['RowEnd']]:
        if "男" in i[settings['SexColumn']] and "女" not in i[settings['SexColumn']]:
            male_name.append(i[settings['NameColumn']])
            male_number.append(i[settings['NumberColumn']])
        elif "女" in i[settings['SexColumn']] and "男" not in i[settings['SexColumn']]:
            female_name.append(i[settings['NameColumn']])
            female_number.append(i[settings['NumberColumn']])
    if not male_name + female_name:
        print_wrong("数据库为空")
        input('请按回车键退出运行')
        exit()
    elif not male_name:
        print_error("无男性数据")
        only_one_sex = True
    elif not female_name:
        print_error("无女性数据")
        only_one_sex = True
else:
    num_list = []
    name_list = []
    for i in tmp_list:
        num_list.append(i[settings['NumberColumn']])
    for i in tmp_list:
        name_list.append(i[settings['NameColumn']])

#判断是否有权重列是否正确
if settings['IncludeWeight']:
    for i in tmp_list[settings['RowStart']:settings['RowEnd']]:
        if len(i) <= settings['WeightColumn'] and is_integer(i[settings['WeightColumn']]):
            print_wrong("数据库权重列设置不正确")
            input("请检查数据库权重列并按回车键退出运行")
            exit()

#提取权重
weight_list = []
if settings['IncludeWeight']:
    for i in tmp_list[settings['RowStart']:settings['RowEnd']]:
        weight_list.append(i[settings["WeightColumn"]])

#删除初步分类临时表
del tmp_list

#模式列表
modelist = ['单人姓名抽取',
            '多人姓名抽取',
            '单人编号抽取',
            '多编号抽取模式',
            '单人性别选择姓名抽取',
            'about']

#定义主逻辑
while True:
    for i in range(len(modelist)):
        print(f"{i+1}.{modelist[i]}模式")
    #选择模式
    mode = input("请输入您选择的模式编号或输入\"exit\"退出运行:")
    #主逻辑
    if mode == "1":
        if settings['IncludeSex']:
            single_name_pick(male_name + female_name)
        else:
            single_name_pick(name_list)
    elif mode == "2":
        if settings['IncludeSex']:
            multiple_name_pick(male_name + female_name)
        else:
            multiple_name_pick(name_list)
    elif mode == "3":
        if settings['IncludeSex']:
            single_number_pick(male_number + female_number)
        else:
            single_number_pick(num_list)
    elif mode == "4":
        if settings['IncludeSex']:
            multiple_number_pick(male_number + female_number)
        else:
            multiple_number_pick(num_list)
    elif mode == "5":
        if only_one_sex:
            print_wrong("仅单性别数据无法使用此模式")
        else:
            single_gender_select_name_pick(male_name,female_name)
    elif mode == "6":
        print()
        print("版本信息:")
        print(f"    version:{VERSION_INFO['version']}")
        print(f"    update_date:{VERSION_INFO['update_date']}")
        print(f"    update_info:")
        for update_info in VERSION_INFO['update_info']:
            print(f"        {update_info}")
        print(f"    {VERSION_INFO['other']}")
        input("按回车键继续使用...")
    elif mode == "exit":
        exit()
    else:
        print_error('未识别的模式编号')
        print('请重新选择模式')