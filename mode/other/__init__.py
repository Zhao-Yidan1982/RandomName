#定义判断是否为整数的函数
def is_integer(s:str):
    assert type(s) == type(""), "应输入字符串" 
    try:
        int(s)
        return True
    except ValueError|TypeError:
        return False
