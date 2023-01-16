# 数据库处理逻辑

import sqlite3

class database(object):
    def __init__(self) -> None:
        pass

    def create(self, name:str, path:str, dict:dict):
        self.connect = sqlite3.connect(path)
        self.cursor = self.connect.cursor()
        sql = f"CREATE TABLE {name} ({self.__attributeStr(dict, ' ', False)});"
        # print("create sql: ", sql)

        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except:
            print("this table already exists")
        finally:
            pass
        
    def insert(self, name:str, dict:dict):
        sql = f"INSERT INTO {name} VALUES({self.__attributeStr(dict, '', True)})"
        # print("insert sql: ", sql)
        self.__execute(sql)
        
    def update(self, name:str, dict:dict, condition:dict, operator:str, logicOp:str):
        sql = f"UPDATE {name} SET {self.__attributeStr(dict, ' = ', False)} {self.__conditionStr(condition, operator, logicOp)}"
        # print("update sql: ", sql)
        self.__execute(sql)

    def delete(self, name:str, condition:dict, operator:str, logicOp:str):
        sql = f"DELETE FROM {name} {self.__conditionStr(condition, operator, logicOp)}"
        # print("delete sql: ", sql)
        self.__execute(sql)
    
    # keys should use "key1, key2..." as input, if select all keys, keys can use "*" as input
    def select(self, name:str, keys:str, condition:dict, operator:str, logicOp:str):
        sql = f"SELECT {keys} FROM {name} {self.__conditionStr(condition, operator, logicOp)}"
        # print("select sql: ", sql)
        self.__execute(sql)
        
    def show(self):
        result = self.cursor.fetchall()
        # print("database result: ", result)
        return result
    
    def close(self):
        self.cursor.close()
        self.connect.close()
        
    def __execute(self, sql:str):
        self.cursor.execute(sql)
        self.connect.commit()
    
    def __attributeStr(self, dict:dict, Spacer:str, inoreKey:bool):
        dict_str = ""
        if inoreKey:
            for key, value in dict.items():
                if isinstance(value, str):
                    dict_str += f"\'{value}\',"
                else:
                    dict_str += f"{value},"
        else:
            for key, value in dict.items():
                if isinstance(value, str):
                    dict_str += f"{key}{Spacer}\'{value}\',"
                else:
                    dict_str += f"{key}{Spacer}{value},"
        dict_str = dict_str[:-1]
        return dict_str
        
    def __conditionStr(self, condition:dict, operator:str, logicOp:str):
        condition_str = "WHERE "
        for key, value in condition.items():
            if isinstance(value, str):
                condition_str += f" {key} {operator} \'{value}\' {logicOp}"
            else:
                condition_str += f" {key} {operator} {value} {logicOp}"

        condition_str = condition_str[:-1 * len(logicOp)]
        return condition_str

# test demo
if __name__ == '__main__':
    pass
