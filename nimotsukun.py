'''
    荷物君
    
    nimotsu.py
    
    20234/01/04 by kepohon
'''

import sys
import msvcrt
import os

from stage import Stage
from state import State
from object import Object

class Nimotsukun:
    DIRECTION_RIGHT = 0
    DIRECTION_UP = 1
    DIRECTION_DOWN = 2
    DIRECTION_LEFT = 3
    _direction = None
    
    def __init__(self, stageFileName):
        self._stageFileName = stageFileName
        self._stage = Stage(stageFileName)
        self._state = State(self._stage.data(), self._stage.width(), self._stage.height())
    
    def displayState(self, switch):
        self._state.displayState(self._stage.width(), self._stage.height(), switch)
    
    def update(self, direction):
        if direction == None:       # 移動でなければ更新なし
            return
        
        playerNextPosition = [0, 0]
        playerNextNextPosition = [0, 0]
        playerCurrentPosition = self._state.searchPlayer()
        #playerNextPosition[0] = playerCurrentPosition[0]
        #playerNextPosition[1] = playerCurrentPosition[1]
        
        directionX = 0
        directionY = 0
        print("direction = %d" % direction)
        if direction == self.DIRECTION_RIGHT:
            directionX = 1
        elif direction == self.DIRECTION_UP:
            directionY = -1
        elif direction == self.DIRECTION_DOWN:
            directionY = 1
        elif direction == self.DIRECTION_LEFT:
            directionX = -1
        playerNextPosition[0] = playerCurrentPosition[0] + directionX
        playerNextPosition[1] = playerCurrentPosition[1] + directionY
        playerNextNextPosition[0] = playerNextPosition[0] + directionX
        playerNextNextPosition[1] = playerNextPosition[1] + directionY
        
        print("player current position %d, %d" % (playerCurrentPosition[0], playerCurrentPosition[1]))
        print("player next position %d, %d" % (playerNextPosition[0], playerNextPosition[1]))
        
        currentObject = self._state.get(playerCurrentPosition[0], playerCurrentPosition[1])
        nextObject = self._state.get(playerNextPosition[0], playerNextPosition[1])
        nextNextObject = self._state.get(playerNextNextPosition[0], playerNextNextPosition[1])
        print("currentObject = [%s]" % str(currentObject))
        print("nextObject = [%s]" % str(nextObject))
        
        if str(nextObject) == "#":
            return
        if str(currentObject) == "p" and str(nextObject) == " ":
            print("move enable")
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object(" "))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("p"))
            return
        if str(currentObject) == "p" and str(nextObject) == ".":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object(" "))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("P"))
            return
        if str(currentObject) == "p" and str(nextObject) == "o" and str(nextNextObject) == " ":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object(" "))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("p"))
            self._state.set(playerNextNextPosition[0], playerNextNextPosition[1], Object("o"))
        if str(currentObject) == "p" and str(nextObject) == "o" and str(nextNextObject) == ".":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object(" "))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("p"))
            self._state.set(playerNextNextPosition[0], playerNextNextPosition[1], Object("O"))
        if str(currentObject) == "p" and str(nextObject) == "O" and str(nextNextObject) == ".":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object(" "))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("P"))
            self._state.set(playerNextNextPosition[0], playerNextNextPosition[1], Object("O"))
        if str(currentObject) == "p" and str(nextObject) == "O" and str(nextNextObject) == " ":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object(" "))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("P"))
            self._state.set(playerNextNextPosition[0], playerNextNextPosition[1], Object("o"))
            
        if str(currentObject) == "P" and str(nextObject) == " ":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object("."))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("p"))
            return
        if str(currentObject) == "P" and str(nextObject) == "o" and str(nextNextObject) == " ":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object("."))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("p"))
            self._state.set(playerNextNextPosition[0], playerNextNextPosition[1], Object("o"))
        if str(currentObject) == "P" and str(nextObject) == "O" and str(nextNextObject) == " ":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object("."))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("P"))
            self._state.set(playerNextNextPosition[0], playerNextNextPosition[1], Object("o"))
        if str(currentObject) == "P" and str(nextObject) == "O" and str(nextNextObject) == ".":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object(" "))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("P"))
            self._state.set(playerNextNextPosition[0], playerNextNextPosition[1], Object(" "))
        if str(currentObject) == "P" and str(nextObject) == ".":
            self._state.set(playerCurrentPosition[0], playerCurrentPosition[1], Object("."))
            self._state.set(playerNextPosition[0], playerNextPosition[1], Object("P"))
        pass
    
    def output(self):
        os.system('cls')        # コンソールクリア
        self._state.displayState(self._stage.width(), self._stage.height(), True)
    
    def play(self):
        while True:
            if self._state.isGameClear():
                print("Game Clear ＼(^o^)／")
                break
            
            # キー入力
            self._direction = None
            if msvcrt.kbhit() == 0:
                continue
            keyCode = msvcrt.getch()
            if keyCode == b"\xe0":
                keyCode2 = msvcrt.getch()
                if keyCode2 == b'M':        # RIGHT Key
                    self._direction = self.DIRECTION_RIGHT
                    print("RIGHT")
                elif keyCode2 == b'H':      # UP Key
                    self._direction = self.DIRECTION_UP
                    print("UP")
                elif keyCode2 == b'P':      # DOWN Key
                    self._direction = self.DIRECTION_DOWN
                    print("DOWN")
                elif keyCode2 == b'K':      # LEFT Key
                    self._direction = self.DIRECTION_LEFT
                    print("LEFT")
                else:
                    self._direction = None
                    
            if keyCode == b"\x1b":
                break
            
            
            # 更新処理
            self.update(self._direction)
            
            # 表示処理
            self.output()
            print("player position = ", end="")
            print(self._state.searchPlayer())


if __name__ == "__main__":
    print("荷物君")
    
    args = sys.argv
    
    stageFileName = None
    if len(args) == 2:
        stageFileName = args[1]
        print("ステージファイルあり：%s" % stageFileName)
    
    nimotsukun = Nimotsukun(stageFileName)
    
    nimotsukun.output()
    
    nimotsukun.play()

