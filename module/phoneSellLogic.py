# 进销存系统处理逻辑
from module.phoneSellDatas import component
from module.database import database

class system:
    def __init__(self, name:str) -> None:
        # init database here
        table_attribute = {"ID": "INTEGER", "name": "TEXT", "price": "NUMBER", "quantity": "INTEGER", "sales": "INTEGER"}
        self.db = database()
        self.db.create(name=f"{name}", path="./database/phone.db", dict=table_attribute)
        self.name = name
        result = self.__query("", self.name, "ID", {"ID":0}, ">=", "AND")
        self.cpn = component()
        self.id = result[-1][0] if len(result) != 0 else 0
        add = lambda module, name, dict: self.add(module, name, dict)
        remove = lambda module, name, condition: self.remove(module, name, condition)
        update = lambda module, name, dict: self.update(module, name, dict)
        query = lambda module, name, dict: self.query(module, name, dict)
        quit = lambda module: self.quit(module)
        self.callMap = {"add":add, "remove":remove, "update":update, "query":query, "quit":quit}
        
    def getCallMap(self):
        return self.callMap
    
    def getComponent(self):
        return self.cpn
            
    def add(self, module:str, name:str, dict:dict):
        try:
            dict["ID"] = self.id
            dict["name"] = str(dict["name"])
            dict["price"] = float(dict["price"]) if dict["price"] != '' else 0
            dict["quantity"] = int(dict["quantity"])
            dict["sales"] = int(dict["sales"])
        except:
            result_str = "输入数据格式不正确!"
            return result_str
        finally:
            pass

        if dict["name"] == "":
            result_str = "请输入商品名称！"
            return result_str
        result = self.__query(module, name, "*", {"name":dict["name"]}, "=", "AND")
        if len(result) == 0:
            if dict["price"]<0:
                result_str = "输入价格为负数, 请重新设置！"
            else:
                self.id += 1
                self.db.insert(f"{name}", dict)
                result_str = "当前仓库暂时无该商品, 新增商品成功！"
        else:
            result_str = "当前仓库已有该商品, 如需要请更新/删除商品！"
        return result_str
    
    def remove(self, module:str, name:str, condition:dict):
        result = self.__query(module, name, "*", {"name":condition["name"]}, "=", "AND")
        if len(result) == 0:
            result_str = "仓库中没有该商品, 无法删除!"
        else:
            self.db.delete(name=f"{name}", condition=condition, operator="=", logicOp="AND")
            result_str = "成功删除该商品!"
        return result_str
        
    def update(self, module:str, name:str, dict:dict, condition:dict=None):
        try:
            dict["ID"] = int(dict["ID"])
            dict["name"] = str(dict["name"])
            dict["price"] = float(dict["price"]) if dict["price"] != '' else 0
            dict["quantity"] = int(dict["quantity"])
            dict["sales"] = int(dict["sales"])
        except:
            result_str = "输入数据格式不正确!"
            return result_str
        finally:
            pass
        
        dict["name"] = str(dict["name"])
        result = self.__query(module, name, "*", {"name":dict["name"]}, "=", "AND")
        if len(result) == 0:
            if module == "management":
                action = "新增商品"
            else:
                action = "切换到管理商品界面新增商品"
            return f"当前仓库没有该商品， 请{action}!"
        dict["ID"] = int(result[0][0])
        dict["name"] = str(result[0][1])
        condition = {"name":dict["name"]} if condition is None else condition
        if module == "management":
            dict["price"] = float(dict["price"]) if dict["price"] != '' else 0
            if dict["price"]<0:
                result_str = "输入价格不合理, 请重新设置！"
            else:
                dict["quantity"] = int(result[0][3])
                dict["sales"] = int(result[0][4])
                self.db.update(name=f"{name}", dict=dict, condition=condition, operator="=", logicOp="AND")
                result_str = "更新商品成功！"
        elif module == "purchase":
            if int(dict["quantity"])<0:
                result_str = "输入进货量不合理, 请重新设置！"
            else:
                dict["price"] = float(result[0][2])
                dict["quantity"] = int(result[0][3]) + int(dict["quantity"])
                dict["sales"] = int(result[0][4])
                self.db.update(name=f"{name}", dict=dict, condition=condition, operator="=", logicOp="AND")
                result_str = "进货成功！"
        elif module == "sales":
            if int(dict["sales"])<0:
                result_str = "输入销货量不合理, 请重新设置！"
            else:
                dict["price"] = float(result[0][2])
                dict["quantity"] = int(result[0][3])
                res = int(result[0][3]) - int(dict["sales"])
                if res>=0:
                    dict["quantity"] = res
                    dict["sales"] = int(result[0][4]) + int(dict["sales"])
                    self.db.update(name=f"{name}", dict=dict, condition=condition, operator="=", logicOp="AND")
                    result_str = "销货成功！"
                else:
                    result_str = f"当前仓库商品存量为：{int(result[0][3])}, 无法销售{int(dict['sales'])}件商品, 请进货！"
        else:
            result_str = "更新失败！"
        return result_str
        
    def query(self, module:str, name:str, dict:dict):
        # support Fuzzy search
        condition = {}
        for _key, _value in dict.items():
            try:
                if _key == "name" and _value != "":
                    condition[_key] = f"%{_value}%"
                elif _value != "":
                    condition[_key] = int(_value)
            except:
                result_str = "输入数据格式不正确!"
                return result_str
            finally:
                pass
                
        result = self.__query(module, name, "*", condition, " LIKE ", f"{self.cpn.getSearchLogic()}")
        if(len(result) == 0):
            result_str = "当前仓库没有该商品, 如需要请在商品管理界面新增商品！"
        else:
            result_str = ""
            for r in result:
                result_str += f"商品名: {r[1]}, 库存: {r[3]}, 销量: {r[4]}\n"
        return result_str
    
    def quit(self, module:str):
        self.db.close()
        
    def __query(self, module:str, name:str, keys:str, condition:dict, operator:str, logicOp:str):
        self.db.select(name=f"{name}", keys=f"{keys}", condition=condition, operator=operator, logicOp=logicOp)
        return self.db.show()

# test demo
if __name__ == '__main__':
    pass

 