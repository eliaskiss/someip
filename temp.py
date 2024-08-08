def convert_to_hex(code, prefix=True):
    return '0x' + code.hex() if prefix else code.hex()

def feedback_parser(data):
    # b'E\x00\x000\x1e\xe6\x00\x00@\x11\xb7\x1fd@n\x0bd@n,\xc7E\xc7E\x00\x1cFO
    # \x00\x13                      # Service ID
    # \x05\x01                      # Method ID
    # \x00\x00\x00\x0c              # Length 12
    # \x00\x01                      # Client ID
    # \x00\x01                      # Session ID
    # \x01\x01                      # SOME/IP Version
    # \x80                          # Interface Version
    # \x00                          # Return Code
    # \x00\x00\x00\x00              # Payload
    # \x00\x00'
    # print(data[0:28])
    data = data[28:]

    service_id = convert_to_hex(data[0:2])
    # print(service_id)

    method_id = convert_to_hex(data[2:4])
    # print(method_id)

    client_id = convert_to_hex(data[8:10])
    # print(client_id)

    session_id = convert_to_hex(data[10:12])
    # print(session_id)

    some_ip_version = convert_to_hex(data[12:14])
    # print(some_ip_version)

    payload = convert_to_hex(data[16:20], False)
    # print(payload)

    return {'service_id':service_id,
            'method_id':method_id,
            'client_id':client_id,
            'session_id':session_id,
            'some_ip_version':some_ip_version,
            'payload':payload}

def parse_ip(summary):
    from_ip, to_ip = summary.split(' > ')
    from_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', from_ip)[0]
    to_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', to_ip)[0]
    # print(from_ip)
    # print(to_ip)
    return {'from_ip':from_ip, 'to_ip':to_ip}

import re

if __name__ == '__main__':
    # data = b'E\x00\x000\x1e\xe6\x00\x00@\x11\xb7\x1fd@n\x0bd@n,\xc7E\xc7E\x00\x1cFO\x00\x13\x05\x01\x00\x00\x00\x0c\x00\x01\x00\x01\x01\x01\x80\x00\x00\x00\x00\x00\x00\x00'
    # result = feedback_parser(data)
    # print(result)
    #
    # summary = 'IP / UDP 100.64.110.11:51013 > 100.64.110.44:51013 / Raw / Padding'
    # ips = parse_ip(summary)
    # print(ips)

    a = {}
    b = {'name':'elias'}
    c = {'age':10}
    a.update(b)
    a.update(c)
    print(a)



