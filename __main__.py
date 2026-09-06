#!/usr/bin/python3

import json
import sys

from mode import *
from mode.wrong import *
from mode.personinfo import PersonInfo

#版本信息
VERSION_INFO = {
    "version": "1.2.0",
    "update_date": "2026-8-22",
    "update_info": [
        "【修复】增加空数据库和行范围配置检查",
        "【修复】增加动态权重的非负数和总和校验",
        "【修复】修复配置文件JSON格式和缺少字段时的错误提示",
        "【改进】完善未实现模式的敬请期待提示",
        "【功能】添加macOS启动脚本"
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
            break
    except FileNotFoundError:
        print_error(printmessage='配置文件不存在',exit_num=file_not_found_exit)
    except PermissionError:
        print_error(printmessage='无读取配置文件权限不足',exit_num=permission_exit)
    except json.JSONDecodeError:
        print_error(printmessage='配置文件不是合法的JSON格式',exit_num=json_decode_exit)
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            print_error('不支持此编码的配置文件',"请使用GBK或UTF-8\n并按回车键退出运行")

required_settings = [
    "IncludeNumber", "NumberColumn", "IncludeName", "NameColumn",
    "IncludeSex", "SexColumn", "IncludeWeight", "WeightColumn",
    "RowStart", "RowEnd"
]
if not isinstance(settings, dict):
    print_error('配置文件内容必须是JSON对象',"请检查配置文件格式并按回车键退出程序",json_decode_exit)
missing_settings = [key for key in required_settings if key not in settings]
if missing_settings:
    print_error(f'配置文件缺少字段: {", ".join(missing_settings)}', "请补充配置字段并按回车键退出程序",json_decode_exit)

#读取数据
for enc in encodings:
    try:
        with open(f"nmls/{filename}", 'r', encoding=enc) as nmls:
            mnls_main = nmls.readlines()
        break  # 读取成功，跳出循环
    except FileNotFoundError:
        print_error('数据库文件不存在',"请按回车键退出程序",file_not_found_exit)
    except PermissionError:
        print_error('无读取数据库文件权限不足',"请检查文件权限并按回车键退出程序",permission_exit)
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            print_error('不支持此编码的数据库文本',"请使用GBK或UTF-8\n并按回车键退出运行",unicode_decode_exit)


#删除行末换行符
for i in range(len(mnls_main)):
    mnls_main[i] = mnls_main[i].rstrip('\r\n')

#将数据初步分割
tmp_list = []
for i in mnls_main:
    tmp_list.append(i.split(','))

if settings["RowStart"] > settings["RowEnd"]:
    print_error('数据起始行不能大于结束行')

#分离数据
people_data:list = []
try:
    for people in tmp_list[settings["RowStart"]:settings["RowEnd"] + 1]:
        number:int|None = int(people[settings["NumberColumn"]]) if settings["IncludeNumber"] else None
        name:str|None = str(people[settings["NameColumn"]]) if settings["IncludeName"] else None
        sex:bool|None = None
        if settings["IncludeSex"]:
            if ("男" in people[settings["SexColumn"]]) == ("女" in people[settings["SexColumn"]]):
                print_error("性别数据不合法")
            if "男" in people[settings["SexColumn"]]:
                sex = True
            elif "女" in people[settings["SexColumn"]]:
                sex = False
        weight:int|None = int(people[settings["WeightColumn"]]) if settings["IncludeWeight"] else None

        people_data.append(PersonInfo(number, name, sex, weight))
except IndexError:
    print_error(printmessage='数据列不存在',exit_num=index_exit)
except ValueError:
    print_error(printmessage='数据内容不合法',exit_num=value_exit)

if not people_data:
    print_error('数据库中没有可读取的数据')

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
    '多人编号抽取',
    '单人性别选择姓名抽取',
    '单人动态权重姓名抽取'
]

#定义主逻辑
while True:
    for i in range(len(mode_list)):
        print(f"{i+1}.{mode_list[i]}模式")
    #选择模式
    mode = input("请输入您选择的模式编号或输入\"about\"查看版本信息\"exit\"退出运行:")
    #主逻辑
    if mode == "about":
        about()
    elif mode == "exit":
        sys.exit(normal_exit)
    else:
        if (is_integer(mode)
            and 1 <= int(mode) <= len(mode_list)
            and mode_list[int(mode) - 1] in mode_dict):
            mode_dict[mode_list[int(mode) - 1]](people_data)
        else:
            print_warning('未识别的模式编号')
            print('请重新选择模式')

