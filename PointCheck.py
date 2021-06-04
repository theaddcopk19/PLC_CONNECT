#PLC Fx3G : Input X: X000 to X177
#X000 to X007, X010 to X017, X020 to X027... X100 to X107 ... X170 to X177
import time


def X_POINT(POINT:int):
    INPUT_POINT = POINT
    INPUT_POINT_GROUP = int(POINT/10)
    START_RANGE = INPUT_POINT_GROUP*10
    END_RANGE = START_RANGE+8
    POINT_GORUP = [*range(START_RANGE, END_RANGE )]
    ErrorPoint = "Error Input {0}".format(POINT)
    if(INPUT_POINT >= 0 and INPUT_POINT <= 177):
        if(INPUT_POINT > 77 and INPUT_POINT < 100):
            return ErrorPoint
        else:
            if(INPUT_POINT not in POINT_GORUP):
                return ErrorPoint
            else:
                return True
    else:
       return ErrorPoint

#PLC Fx3G : Output Y: Y000 to Y177
#Y000 to Y007, Y010 to Y017, Y020 to Y027 ... Y100 to Y107 ... Y170 to Y177
def Y_POINT(POINT:int):
    return  X_POINT(POINT)

#PLC Fx3G: Auxiliry range(M0-M7679) and Spacial range(M8000-M8511)
def M_POINT(POINT:int):
    INPUT_POINT = POINT
    ErrorPoint = "Error Input {0}".format(POINT)
    INPUT_POINT_CHECK = D_POINT(INPUT_POINT)
    if(INPUT_POINT_CHECK is not True):
        return ErrorPoint
    else:
        if(INPUT_POINT > 7679 and INPUT_POINT <8000):
            return ErrorPoint
        else:
            return True
    
#State range(S0-S4095)
def S_POINT(POINT:int):
    INPUT_POINT = POINT
    ErrorPoint = "Error Input {0}".format(POINT)
    if(INPUT_POINT < 0 or INPUT_POINT > 4095):
        return ErrorPoint
    else:
        return True

#Timer range(T0-T319)
def T_POINT(POINT:int):
    INPUT_POINT = POINT
    ErrorPoint = "Error Input {0}".format(POINT)
    if(INPUT_POINT < 0 or INPUT_POINT > 319 ):
        return ErrorPoint
    else:
        return True

#Counter range(C0-C255)
def C_POINT(POINT:int):
    INPUT_POINT = POINT
    ErrorPoint = "Error Input {0}".format(POINT)
    if(INPUT_POINT < 0 or INPUT_POINT > 255):
        return ErrorPoint
    else:
        return True

#Data Register range(D0-D7999) and For Special range (D8000-D8511)
def D_POINT(POINT:int):
    INPUT_POINT = POINT
    ErrorPoint = "Error Input {0}".format(POINT)
    if(INPUT_POINT < 0 or INPUT_POINT > 8511):
        return  ErrorPoint
    else:
        return True

#Extension Register range(R0-R23999)
def R_POINT(POINT:int):
    INPUT_POINT = POINT
    ErrorPoint = "Error Input {0}".format(POINT)
    if(INPUT_POINT < 0 or INPUT_POINT > 23999):
        return ErrorPoint
    else:
        return True



