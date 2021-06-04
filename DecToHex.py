def DEC_TO_HEC(DEC_INPUT:int):
    DEC_HEX = hex(DEC_INPUT).upper()
    DEC_HEX = DEC_HEX[2:]
    if(len(DEC_HEX) <4):
        DEC_HEX = "{0}{1}".format("0"*(4-len(DEC_HEX)), DEC_HEX)
        return (DEC_HEX)
    else:
        return DEC_HEX
