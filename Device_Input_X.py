#Input X000 to X177
from PointCheck import X_POINT

class Device_Input_X():
    def __init__(self):
        self.INPUT_X = []

    def SET(self, INPUT:int):
        INPUT_CHECK = X_POINT(INPUT)
        if(INPUT_CHECK is True):
            self.INPUT_X.append(INPUT)
        else:
            self.INPUT_X.append(INPUT_CHECK) 
        
    def GET(self):
        return self.INPUT_X

    def ERROR_CHECK(self):
        INPUT_length = len(self.INPUT_X)
        for i in range(INPUT_length):
            INPUT_int = self.INPUT_X[i]
            if(type(INPUT_int) is int):
                ERROR = False 
                continue
            else:
                ERROR = True
                break 
        return ERROR 