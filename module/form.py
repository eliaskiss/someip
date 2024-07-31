from scapy.layers.inet import UDP
from scapy.layers.inet import IP
from scapy.all import load_contrib, send, conf, sr
from scapy.contrib.automotive.someip import SOMEIP
import sys

class SomeIpForm:
    def __init__(self, proto, msg_type, ret_code, srv_id, method_id, client_id, session_id, payload):
        # verbose = 0, 로그 남기지 않음.
        conf.verb = 0
        load_contrib("automotive.someip", globals_dict=globals())
        self.sip = SOMEIP()
        self.sip.proto_ver = proto
        self.sip.msg_type = msg_type
        self.sip.retcode = ret_code
        self.sip.srv_id = srv_id
        self.sip.method_id = method_id 
        self.sip.client_id = client_id 
        self.sip.session_id = session_id
        self.sip.add_payload(payload)

    def send(self):
        try:
            # 기존코드
            return send(self.packet)

            # 수정코드
            return sr(self.packet)
        except Exception as e:
            msg = f'Function send - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
            raise Exception(msg)

    def viewPacket(self):
        try:
            self.packet.show()
        except Exception as e:
            msg = f'Function viewPacket - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
            raise Exception(msg)

    def setUdp(self, port_sim, port_dest):
        try:
            self.udp = UDP(sport=port_sim,dport=port_dest)
        except Exception as e:
            msg = f'Function setUdp - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
            raise Exception(msg)

    def setIp(self, address_sim, address_dest):
        try:
            self.ip = IP(src = address_sim, dst = address_dest)
        except Exception as e:
            msg = f'Function setIp - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
            raise Exception(msg)

    def setPacket(self):
        try:
            self.packet = self.ip/self.udp/self.sip
        except Exception as e:
            msg = f'Function setPacket - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
            raise Exception(msg)

if __name__ == '__main__':
    sif = SOMEIP()