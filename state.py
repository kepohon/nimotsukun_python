'''
    ステージの状態 荷物君
    
    state.py
    
    20234/01/04 by kepohon
'''

from object import Object

class State:
    _stageData = None
    _playerPosition = [0, 0]
    
    def __init__(self, stageData, width, height):
        self._width = width
        self._height = height
        self._stateData = [0] * (width * height)    # 状態データ配列の動的確保
        self.loadStage(stageData, width, height)
        self.searchPlayer()
    
    def loadStage(self, stageData, width, height):
        index = 0
        x = 0
        y = 0
        for data in stageData:
            if data != '\n':
                obj = Object(data)
                obj.setXY(x, y)
                x += 1
                self._stateData[index] = obj
                index += 1
            else:
                y += 1
                x = 0
    
    def displayState(self, width, height, switch):
        counter = 0
        for stateData in self._stateData:
            if switch == True:
                print(str(stateData), end="")
            else:
                print(int(stateData), end="")
            counter += 1
            if counter >= width:
                print("")
                counter = 0
    
    def searchPlayer(self):
        x = 0
        y = 0
        index = 0
        position = [0, 0]
        for data in self._stateData:
            if str(data) == 'p' or str(data) == 'P':
                x = index % self._width
                y = int(index / self._width)
                #position = data.getXY()
                break
            index += 1
        #self._playerPosition = position
        position[0] = x
        position[1] = y
        return position
    
    def get(self, x, y):
        if x >= self._width or y >= self._height:
            return None
        if x < 0 or y < 0:
            return None
        index = y * self._width + x
        return self._stateData[index]
    
    def set(self, x, y, obj):
        self._stateData[y*self._width+x] = obj
    
    def width(self):
        return self._width
    
    def height(self):
        return self._height
    
    def isGameClear(self):
        for obj in self._stateData:
            if str(obj) == "." or str(obj) == "P":
                return False
        return True

