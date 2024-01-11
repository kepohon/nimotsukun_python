# -*- coding: utf-8 -*-
import msvcrt

class Key:
    keyHited = 0
    lastKey = 0
    
    def __init__(self):
        pass
    
    def kbhit(self):
        return msvcrt.kbhit()
    
    def getch(self):
        return msvcrt.getch()
    

# 使用例
if __name__ == "__main__":
    
    key = Key()
    print('hit any key!("q" or "ESC":exit)')
    
    while True:
        if key.kbhit() != 0:
            continue
        keyCode = key.getch()
        if keyCode == b"\xe0":
            keyCode2 = key.getch()
            if keyCode2 == b'M':
                print("RIGHT")
            elif keyCode2 == b'H':
                print("UP")
            elif keyCode2 == b'P':
                print("DOWN")
            elif keyCode2 == b'K':
                print("LEFT")
            continue
        if keyCode == b"\x1b":
            break
        if keyCode == b"\r":
            print('RETURN')
            continue
        if keyCode == b"\x08":
            print('BACK SPACE')
            continue
        if keyCode == b"q":
            break
    
