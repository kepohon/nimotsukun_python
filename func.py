# -*- coding: utf-8 -*-
'''
    func.py
    
    関数を引数として渡す（クラスメソッドの引数）
    
    2024/01/09 by kepohon
'''

class Func:
    def __init__(self,func=None):
        if func is None:
            self._func = self.defaultFunction    # デフォルト関数を渡す
        else:
            self._func = func           # 引数で指定された関数を渡す
    
    def defaultFunction(self):
        print("defaultFunction")
    
    def run(self):
        self._func()
    

def aFunc():
    print("aFunc")


# 使用例
if __name__ == "__main__":
    f2 = Func()
    f2.run()
    f = Func(aFunc)
    f.run()

