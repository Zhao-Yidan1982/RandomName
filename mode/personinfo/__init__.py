#定义身份信息class
class PersonInfo:
    def __init__(self, \
                _number:(int|None) = None,\
                _name:(str|None) = None, \
                _sex:(bool|None) = None, \
                _weight:(int|None) = None):
        
        self.number = _number
        self.name = _name
        self.sex = _sex
        self.weight = _weight
    def __str__(self)-> str:
        if self.sex:
            sex:str = '男'
        else:
            sex:str = '女' 
        return f'number:{self.number} name:{self.name} sex:{sex} weight:{self.weight}'
