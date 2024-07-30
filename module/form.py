from scapy.all import UDP, load_contrib, send, IP, conf
from scapy.contrib.automotive.someip import SOMEIP

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
        send(self.packet)

    def viewPacket(self):
        self.packet.show()

    def setUdp(self, port_sim, port_dest):
        self.udp = UDP(sport=port_sim,dport=port_dest)

    def setIp(self, address_sim, address_dest):
        self.ip = IP(src = address_sim, dst = address_dest)

    def setPacket(self):
        self.packet = self.ip/self.udp/self.sip