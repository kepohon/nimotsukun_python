'''
    オブジェクト 荷物君
    
    object.py
    
    20234/01/04 by kepohon
'''

class Object:
    _currentX = 0
    _currentY = 0
    
    objectArray = "# oO.pP\n"
    WALL = 0
    BLANK = 1
    BLOCK = 2
    BLOCK_ON_GOAL = 3
    GOAL = 4
    MAN = 5
    MAN_ON_GOAL = 6
    NEW_LINE = 7
    UNKNOWN = 8
    
    def __init__(self, data):
        self._data = data
        self._index = self.search(data)
        pass
    
    def __int__(self):
        return self._index
    
    def __str__(self):
        return self._data
    
    def search(self, character):
        return self.objectArray.index(character)
    
    def character(self, index):
        return self.objectArray[index]
    
    def setXY(self, x, y):
        self._currentX = x
        self._currentY = y
    
    def getXY(self):
        return [self._currentX, self._currentY]
    


# Objectの使い方
if __name__ == "__main__":
    obj = Object()
    print("obj=%d" % (obj))
    print(obj)
    if int(obj) == 5:
        print("MAN")
    index = obj.search('P')
    print(index)
    print(obj.character(index))
    print(obj.character(obj.GOAL))
    
