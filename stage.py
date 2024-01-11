'''
    ステージ処理 荷物君
    
    stage.py
    
    20234/01/04 by kepohon
'''

class Stage:
    
    # デフォルトのステージデータ
    defaultStageData = "##########\n"\
                "#        #\n"\
                "# ..   p #\n"\
                "# oo     #\n"\
                "#        #\n"\
                "##########\n"
    widthNumber = 10
    heightNumber = 6
    
    def __init__(self, stageFileName):
        self._stageFileName = stageFileName
        if stageFileName != None:
            self.readStageFile(stageFileName)
        else:
            self.stageData = self.defaultStageData
        self.analyzeStageData()
    
    def readStageFile(self, stageFileName):
        f = open(stageFileName, 'r')
        self.stageData = f.read()
        f.close()    
    
    def analyzeStageData(self):
        width = 0
        height = 0
        for data in self.stageData:
            if data == '\n':
                height += 1
                self._width = width
                width = 0
            else:
                width += 1
        self._height = height
    
    def data(self):
        return self.stageData
    
    def displayStage(self):
        print(self.stageData)
    
    def width(self):
        return self._width
    
    def height(self):
        return self._height
        

