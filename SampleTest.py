from PLC_Read import PLC_Read
from time import sleep

data = PLC_Read()
def Divice():
    while True:
        Hour= data.Data_D(8015) 
        minute = data.Data_D(8014)
        second = data.Data_D(8013)
        sleep(1)
        print("D8015:{0}, D8014:{1}, D8013:{2}".format(Hour,\
             minute, second))
Divice()