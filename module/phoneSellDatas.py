# 进销存系统数据定义和管理

class component(object):
    def __init__(self) -> None:
        self.moduleTable = {
            "主页面":{"name":"defalut", "function": []},
            "管理商品":{"name":"management", "function": ["add", "remove", "update"]},
             "进货":{"name":"purchase", "function": ["update"]},
             "销货":{"name":"sales", "function": ["update"]},
             "查询":{"name":"query", "function": ["query"]},
             "退出系统":{"name":"quit", "function": ["quit"]}}
      
        self.menu = list(self.moduleTable.keys()) 
        print("self.menu: ", self.menu)
        self.searchLogic = "OR"
    def getMenu(self):
        return self.menu

    def getModueFunction(self, module:str):
        return self.moduleTable[module]
    
    def setSearchLogic(self, logic:str):
        self.searchLogic = logic
    
    def getSearchLogic(self):
        return self.searchLogic
    
# test demo
if __name__ == '__main__':
    pass