import sys

#定义数据缺失字符串
no_name:str = '无姓名数据无法使用该模式'
no_sex:str = '无性别数据无法使用该模式'
no_number:str = '无编号数据无法使用该模式'
no_weight:str = '无权重数据无法使用该模式'

#定义退出值
normal_exit = 0
file_not_found_exit = 1
permission_exit = 2
unicode_decode_exit = 3
json_decode_exit = 4
index_exit = 5
value_exit = 6


#定义错误提示函数
def print_warning(message:str):
    print(f"Warning:{message}!!\n")

def print_error(printmessage:str, inputmessage:str = "请按return键退出", exit_num:int = normal_exit):
    print(f"Error:{printmessage}!!!\n")
    input(inputmessage)
    sys.exit(exit_num)