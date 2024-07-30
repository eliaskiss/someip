from module.trans import getIds, hexStringToByte, ConvertPayloadToHexString
from module.form import SomeIpForm

if __name__ == "__main__":
    address_sim = "100.64.110.61"
    address_dest = "100.64.110.11"

    port_sim = 51018
    port_dest = 51013

    protocol_ver = 1
    client_id = 0x1
    session_id = 0x1
    msg_type = "RESPONSE"
    msg_status = "E_OK"
    
    payload = '0102'
    header_id = 1246465

    service_id, method_id = getIds(header_id)
    payload = hexStringToByte(ConvertPayloadToHexString(payload))

    form = SomeIpForm(
                proto = protocol_ver,
                msg_type = msg_type,
                ret_code = msg_status,
                srv_id = service_id,
                method_id = method_id,
                client_id = client_id,
                session_id = session_id,
                payload = payload
            )
    form.setIp(address_sim, address_dest)
    form.setUdp(port_sim, port_dest)
    form.setPacket()
    
    # form.viewPacket()
    form.send()
