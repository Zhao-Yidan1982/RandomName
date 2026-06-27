#!/usr/bin/python3
import configparser

#定义错误提示函数
def print_error(message):
    print(f"error:{message}!!\n")

def print_wrong(message):
    print(f"wrong:{message}!!!\n")

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

#选择档案名
filename = input("请输入要读取的数据库文件名(默认为default): ")
if filename == '':
    filename = "default"

#定义程序设置类
class ProgramSettings:
    def __init__(self):
        self.IncludeNumber = True
        self.NumberColumn = 0
        self.IncludeName = True
        self.NameColumn = 1
        self.IncludeSex = True
        self.SexCColumn = 2
        self.IncludeHeavy = True
        self.HeavyColumn = 3
        self.DynamicHeavy = False

#读取配置文件
settings = ProgramSettings()
config = configparser.ConfigParser()
config.read('config/setting.ini')
settings.IncludeNumber = config.getboolean('DEFAULT', 'IncludeNumber', fallback=settings.IncludeNumber)
settings.NumberColumn = config.getint('DEFAULT', 'NumberColumn', fallback=settings.NumberColumn)
settings.IncludeName = config.getboolean('DEFAULT', 'IncludeName', fallback=settings.IncludeName)
settings.NameColumn = config.getint('DEFAULT', 'NameColumn', fallback=settings.NameColumn)
settings.IncludeSex = config.getboolean('DEFAULT', 'IncludeSex', fallback=settings.IncludeSex)
settings.SexCColumn = config.getint('DEFAULT', 'SexColumn', fallback=settings.SexCColumn)
settings.IncludeHeavy = config.getboolean('DEFAULT', 'IncludeHeavy', fallback=settings.IncludeHeavy)
settings.HeavyColumn = config.getint('DEFAULT', 'HeavyColumn', fallback=settings.HeavyColumn)
settings.DynamicHeavy = config.getboolean('DEFAULT', 'DynamicHeavy', fallback=settings.DynamicHeavy)

#读取数据
encodings = ['utf-8', 'gbk']
for enc in encodings:
    try:
        nmls = open(f"nmls/{filename}", 'r', encoding=enc)
        mnls_main = nmls.readlines()
        break  # 读取成功，跳出循环
    except FileNotFoundError:
        print_wrong('数据库文件不存在')
        input("请按回车键退出程序")
        exit()
    except PermissionError:
        print_wrong('数据库文件权限不足')
        input("请检查文件权限并按回车键退出程序")
        exit()
    except UnicodeDecodeError:
        if enc == encodings[-1]:  # 已经是最后一种编码
            print_wrong('不支持此编码的数据库文本')
            input("请使用GBK或UTF-8\n并按回车键退出运行")
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
include_sex = True
for i in temp_list:
    if len(i) < 3 or \
    "男" in i[2] == "女" in i[2]:
        print_error("数据库中性别标识或性别列位置不正确,将无法使用模式2,请检查数据库")
        include_sex = False
        break

if include_sex:
    #对数据分类
    for i in temp_list:
        if "男" in i[2] and "女" not in i[2]:
            male_name.append(i[1])
        elif "女" in i[2] and "男" not in i[2]:
            female_name.append(i[1])
    all_name = male_name + female_name
    if not all_name:
        print_wrong("数据库为空")
        input('请按回车键退出运行')
        exit()
    elif not male_name:
        print_error("无男性数据")
    elif not female_name:
        print_error("无女性数据")
else:
    del male_name,female_name
    for i in temp_list:
        all_name.append(i[1])
    if not all_name:
        print_wrong("数据库为空")
        input('请按回车键退出运行')
        exit()

#提取编号
num_list = []
for i in temp_list:
    num_list.append(i[0])

#删除初步分类临时表
del temp_list

#导入模块化模式函数
from models.single_name_extract_mode import single_name_extract_mode
from models.choice_sex_mode import choice_sex_mode
from models.multi_name_extract_mode import multi_name_extract_mode
from models.single_number_extract_mode import single_number_extract_mode
from models.multi_number_extract_mode import multi_number_extract_mode

#定义主逻辑
while True:
    #选择模式
    mode = input('1.单人抽取模式\n2.性别选择模式\n3.多人抽取模式\n4.单编号抽取模式\n5.多编号抽取模式\n6.about\n请输入您选择的模式编号或输入"exit"退出运行:')
    #主逻辑
    if mode == "1":
        single_name_extract_mode(all_name)
    elif mode == "2":
        choice_sex_mode(all_name,male_name,female_name,include_sex)
    elif mode == "3":
        multi_name_extract_mode(all_name)
    elif mode == "4":
        single_number_extract_mode(num_list)
    elif mode == "5":
        multi_number_extract_mode(num_list)
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