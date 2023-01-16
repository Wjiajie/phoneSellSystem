# 界面布局

import PySimpleGUI as sg
from module.phoneSellDatas import component
from module.phoneSellLogic import system

class layout:
    def __init__(self, name:str) -> None:
        self.NAME_SIZE = 15
        self.logic = system(name)
        self.datas = self.logic.getComponent()
        self.name = name
        self.stack = list()
        self.module = "defalut"
        sg.theme('SystemDefault')
    def createWindow(self, module="defalut"):
        if module == "defalut":
            self.stack.clear()
            subLayout = [
                        [self.__name('信息'), sg.Text('请选择使用以下任意一种功能')],
                        [self.__name('功能选择'), sg.Combo(self.datas.getMenu(), default_value="菜单", s=(15,20), enable_events=True, readonly=True, k='default')],
            ]
            layout = [
                    [sg.T('欢迎使用手机进销存系统', font='_ 14', justification='c', expand_x=True)],
                    [subLayout],
                    [self.__name('输出窗口'), sg.Output(s=(50,10))],
                    ]
            self.module = "defalut"
            self.window = sg.Window('手机进销售存系统', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, 
                                    alpha_channel=0.95)
        else:
            if module == "management":
                button1 =  [[self.__name('新增'), sg.Button(button_text='新增商品', enable_events=True, k='add')]]
                button2 =  [[self.__name('更新'), sg.Button(button_text='更新商品', enable_events=True, k='update')]]
                button3 =  [[self.__name('删除'), sg.Button(button_text='删除商品', enable_events=True, k='remove')]]
                button4 =  [[self.__name('模块切换'), sg.Combo(["主页面", "退出系统"], default_value="菜单", s=(15,20), enable_events=True, readonly=True, k='default')]]
                
                subLayout1 = [
                        [self.__name(''), sg.Text('新增商品', font='_ 14', justification='c', expand_x=True)],
                        [self.__name('商品名'), sg.Input(s=10)], 
                        [self.__name('价格'), sg.Input(s=10)]
                        ]  
                subLayout2 = [
                        [self.__name(''), sg.Text('更新商品', font='_ 14', justification='c', expand_x=True)],
                        [self.__name('商品名'), sg.Input(s=10)], 
                        [self.__name('价格'), sg.Input(s=10)]
                        ]  
                subLayout3 = [
                        [self.__name(''), sg.Text('删除商品', font='_ 14', justification='c', expand_x=True)],
                        [self.__name('商品名'), sg.Input(s=10)]
                        ]   
                layout = [
                        [sg.T('商品管理', font='_ 14', justification='c', expand_x=True)],
                        [sg.Col(subLayout1, p=0), sg.Col(subLayout2, p=0), sg.Col(subLayout3, p=0)],
                        [sg.Col(button1, p=0), sg.Col(button2, p=10), sg.Col(button3, p=0)],
                        [button4],
                        [self.__name('输出窗口'), sg.Output(s=(50,10))],
                        ]
                self.module = "management"
                self.window = sg.Window('商品管理模块', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)
            elif module == "purchase":
                button1 =  [[self.__name('进货'), sg.Button(button_text='确认进货', enable_events=True, k='update')]]
                button2 =  [[self.__name('模块切换'), sg.Combo(["主页面", "管理商品", "退出系统"], default_value="菜单", s=(15,20), enable_events=True, readonly=True, k='default')]]
                subLayout1 = [
                        [self.__name('进货'), sg.Text('进货')],
                        [self.__name('商品名'), sg.Input(s=10)], 
                        [self.__name('进货数量'), sg.Input(s=10)], 
                        ] 
                subLayout2 = [
                        ]  
                layout = [
                        [sg.T('商品进货', font='_ 14', justification='c', expand_x=True)],
                        [sg.Col(subLayout1, p=0), sg.Col(subLayout2, p=0)],
                        [sg.Col(button1, p=0), sg.Col(button2, p=0)],
                        [self.__name('输出窗口'), sg.Output(s=(50,10))],
                        ]
                self.module = "purchase"
                self.window = sg.Window('进货模块', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)
            elif module == "sales":
                button1 =  [[self.__name('销货'), sg.Button(button_text='确认销货', enable_events=True, k='update')]]
                button2 =  [[self.__name('模块切换'), sg.Combo(["主页面", "管理商品", "进货", "退出系统"], default_value="菜单", s=(15,20), enable_events=True, readonly=True, k='default')]]
                subLayout1 = [
                        [self.__name('销货'), sg.Text('销货')],
                        [self.__name('商品名'), sg.Input(s=10)], 
                        [self.__name('销货数量'), sg.Input(s=10)], 
                        ] 
                subLayout2 = [
                        ]  
                layout = [
                        [sg.T('商品销售', font='_ 14', justification='c', expand_x=True)],
                        [sg.Col(subLayout1, p=0), sg.Col(subLayout2, p=0)],
                        [sg.Col(button1, p=0), sg.Col(button2, p=0)],
                        [self.__name('输出窗口'), sg.Output(s=(50,10))],
                        ]
                self.module = "sales"
                self.window = sg.Window('销货模块', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)
            elif module == "query":
                button1 =  [[self.__name('查询'), sg.Button(button_text='确认查询', enable_events=True, k='query')]]
                button2 =  [[self.__name('模块切换'), sg.Combo(["主页面", "管理商品", "退出系统"], default_value="菜单", s=(15,20), enable_events=True, readonly=True, k='default')]]
                button3 =  [[self.__name('搜索方法选择'), sg.Combo(["AND", "OR"], default_value="OR", size=(5, 2), s=(15,16), enable_events=True, readonly=True, k='search_logic')]]
                subLayout1 = [
                        [self.__name('查询'), sg.Text('查询')],
                        [self.__name('ID'), sg.Input(s=10)], 
                        [self.__name('商品名'), sg.Input(s=10)], 
                        [self.__name('商品数量'), sg.Input(s=10)], 
                        ] 
                subLayout2 = [
                        ]  
                layout = [
                        [sg.T('商品查询', font='_ 14', justification='c', expand_x=True)],
                        [sg.Col(subLayout1, p=0), sg.Col(subLayout2, p=0)],
                        [sg.Col(button1, p=0), sg.Col(button2, p=0)],
                        [button3],
                        [self.__name('输出窗口'), sg.Output(s=(50,10))],
                        ]
                self.module = "query"
                self.window = sg.Window('销货模块', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)
            elif module == "quit":
                self.module = "quit"
                self.window.close()
                self.window = None
        
    def run(self):
        while True:
            if self.window == None:
                break
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                if(len(self.stack)==0):
                    break
                self.stack.pop()
                if(len(self.stack)==0):
                    break
                module = self.stack[-1]
                self.__updateWindows(module)
            if event == 'default':
                moduleFuncs = self.datas.getModueFunction(values[event])
                self.__updateWindows(moduleFuncs["name"])
            if event == 'add':
                dict = {"ID": -1, "name": values[0], "price": values[1], "quantity": 0, "sales": 0}
                callMap = self.logic.getCallMap()
                result_str = callMap[event](self.module, self.name, dict)
                print(f"{result_str}")
            if event == 'update':
                callMap = self.logic.getCallMap()
                if self.module == "management":
                    dict = {"ID": -1, "name": values[2], "price": values[3], "quantity": 0, "sales": 0}
                elif self.module == "purchase":
                    dict = {"ID": -1, "name": values[0], "price": 0, "quantity": values[1], "sales": 0}
                elif self.module == "sales":
                    dict = {"ID": -1, "name": values[0], "price": 0, "quantity": 0, "sales": values[1]}
                result_str = callMap[event](self.module, self.name, dict)
                print(f"{result_str}")
            if event == "remove":
                callMap = self.logic.getCallMap()
                if self.module == "management":
                    dict = {"name": values[4]}
                result_str = callMap[event](self.module, self.name, dict)
                print(f"{result_str}")
            if event == "query":
                callMap = self.logic.getCallMap()
                dict = {"ID": values[0], "name": values[1], "quantity": values[2]}
                result_str = callMap[event](self.module, self.name, dict)
                print(f"{result_str}")
            if event == "search_logic":
                self.datas.setSearchLogic(str(values[event]))
        if self.window is not None:
            self.window.close()
            self.window = None
       
    def __name(self, name):
        dots = self.NAME_SIZE-len(name)-10
        return sg.Text(name + ' ' + ' '*dots, size=(self.NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')
    
    def __updateWindows(self, module:str):
        if(len(self.stack) == 0):
            self.stack.append("defalut")
        self.window.close()
        self.createWindow(module)
        if(len(self.stack) == 0 or module != self.stack[-1]):
            self.stack.append(module)    

# test demo
if __name__ == '__main__':
    pass