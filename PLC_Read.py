# PLC สามารถ เขียนและส่งข้อมูลได้ที่ละ 1 ชุดคำส่ง โดย เมื่อสั่งการแล้วต้องรอการตอบกับของ PLC ทุกครั้ง
# ชุดชุดคำสั่งของ PLC คือ 1E Frame(Ascii code) 
# External Device Side ประกอบด้วย Header, Subheader, PC No., Monitoring timer, Area A
# PLC Side ประกอบด้วย  Header, Subheader, Complate code, Area B
# Read Bit units(X, Y, M, S, T, C) 1E Frame(256 points)
# Write bit units(X, Y, M, S, T, C) 1E Frame(160 Points)
# Read word units(D, R, T, C) 1E Frame(64 Points) 
# Write word units(D, R, T, C) 1E Frame(64 Point)
# X(58H, 20H), Y(59H, 20H), M(4DH, 20H), S(53H, 20H), T(54H, 53H), C(43H, 53H)
# D(44H, 20H), R(52H, 20H), T(54H, 4EH), C(43H, 4EH)
# PLC Read (00, 01)
# PLC Write (02, 03)
# External Device Read(00 FF 000A 5820 00000000 01 00) Communication ASCII code (X00) send PLC
# Data PLC (80 00 01) PLC Send
# External Device Write(02 FF 000A 5820 00000000 01 00 10) Communication ASCII (X00) send PLC
# Data PLC (82 00)
# Sample bit units PLC_Read.Input_X/Output_Y/Auxiliry_M/State_S/Timer_TS/Counter_CS(0, None)
# Sample bit units PLC_Write.Input_X/Output_Y/Auxiliry_M/State_S/Timer_TS/Counter_CS(0, None, 0/1)
# Sample word units PLC_Read.Data_D)Register_R/Timer_TN/Counter_CN(0, *None)
# Sample word units PLC_Write.Data_D)Register_R/Timer_TN/Counter_CN(0, *None, Value)
# Sample word units (32bit) PLC_Read.Data_D)Register_R/Timer_TN/Counter_CN(0, 32)
# Sample word units (32bit) PLC_Write.Data_D)Register_R/Timer_TN/Counter_CN(0, *32, Value)
# *เมื่อต้องการ อ่านหรือเขียน ตัวแปรค่า 32 บิต Divce ทั้งหมด จะนับเป็นคู่ เช่น (32bit ของ D0) โปรแกรมจะทำการ อ่านหรือเขียนค่าจาก D0 และ D1 
# หากอต้องอ่านหรือเขียนค่า Data/Register ที่ตำแหน่งเลขคี่(ตัวอย่าว D1/R1) ค่าที่ได้จะไม่ถูกต้อง ค่าที่ถูกต้องของการอ่าน Data/Register 32Bit คือเลขคู่ (ตัวอย่าง D100/R100, D202/R202)

from PointCheck import * 
from PLC_Connect import *
from DecToHex import *


#คลาสการรับค่าของ PLC
class PLC_Read:
    def __init__(self):
        self.DATA = PLC_SEND_RECIVE()

    def Input_X(self, POINT:int, BIT:int=None):
        Input = X_POINT(POINT)
        if(Input is True):
            Input_hex = DEC_TO_HEC(POINT)
            Input = "00FF000A58200000{0}0100".format(Input_hex)
            return self.DATA.SEND_RECIVE(Input)
        else:
            return Input

    def Output_Y(self, POINT:int, BIT:int=None):
        Output = Y_POINT(POINT)
        return Output
       
    def Auxiliry_M(self, POINT:int, BIT:int=None):
        Auxiliry = M_POINT(POINT)
        if(Auxiliry is True):
            Auxiliry_hex = DEC_TO_HEC(POINT)
            Auxiliry = "00FF000A4D200000{0}0100".format(Auxiliry_hex)
            return self.DATA.SEND_RECIVE(Auxiliry)
        else:
            return Auxiliry

    def State_S(self, POINT:int, BIT:int=None):
        State = S_POINT(POINT)
        return State

    def Timer_TS(self, POINT:int, BIT:int=None):
        Timer = T_POINT(POINT)
        return Timer

    def Counter_CS(self, POINT:int, BIT:int=None):
        Counter = C_POINT(POINT)
        return Counter

    def Data_D(self, POINT:int, BIT:int=None):
        Data = D_POINT(POINT)
        if(Data is True):
            Data_hex = DEC_TO_HEC(POINT)
            Data = "01FF000A44200000{0}0100".format(Data_hex)
            return self.DATA.SEND_RECIVE(Data)
        else:
            return Data

    def Register_R(self, POINT:int, BIT:int=None):
        Register = R_POINT(POINT)
        return Register

    def Timer_TN(self, POINT:int, BIT:int=None):
        TimerValue = T_POINT(POINT)
        return TimerValue
    
    def Counter_CN(self, POINT:int, BIT:int=None):
        CounterValue = C_POINT(POINT)
        return CounterValue