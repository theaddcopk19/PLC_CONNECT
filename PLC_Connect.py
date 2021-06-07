import socket
from time import sleep


class PLC_SEND_RECIVE():
    def __init__(self):
        self.REVICE_FROM_USER = []

    def SEND_RECIVE(self, INPUT:str):
        self.REVICE_FROM_USER.append(INPUT)
        PLC_DATA = self.REVICE_FROM_USER
        sleep(0.01)
        return PLC_CONNECTED.PLC_CONNECT(PLC_DATA.pop(0))


class PLC_CONNECTED(): 
    def PLC_CONNECT(DATA_SEND:str):
        PLC_IP_Fix = "192.168.1.250"
        PLC_PORT_Fix = 10000
        FX3G = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        FX3G.settimeout(1)
        try:
            FX3G.connect((PLC_IP_Fix, PLC_PORT_Fix))
        except socket.timeout:
            print("PLC Connect timeout")
        FX3G.send(DATA_SEND.encode("UTF-8"))
        DATA_RECV = FX3G.recv(1024).decode("UTF-8")
        FX3G.close
        ReCheck_PLC = DATA_RECV[:4]
        PLC_COMPLATE_CODE = ["8000", "8100", "8200", "8300"]
        if(ReCheck_PLC not in PLC_COMPLATE_CODE):
            return None
        else:
            return DATA_RECV 
    