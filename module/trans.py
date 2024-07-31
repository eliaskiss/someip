import sys
def ConvertPayloadToHexString(payload):
    try:
        payload = str(payload)
        if len(payload) % 2 != 0:
            raise Exception("payload를 변환할 수 없습니다.")

        tmp = []
        for i in range(0, len(payload), 2):
            hexed_option = decStringToHexString(payload[i:i+2])
            if len(hexed_option) == 1:
                hexed_option = f"0{hexed_option}"
            tmp.append(hexed_option)

        return ''.join(tmp)
    except Exception as e:
        msg = f'Function ConvertPayloadToHexString - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
        raise Exception(msg)

def decStringToHexString(decimal_string):
    try:
        return str(hex(int(decimal_string)))[2:]
    except Exception as e:
        msg = f'Function decStringToHexString - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
        raise Exception(msg)

def hexStringToByte(hex_string):
    try:
        return bytes.fromhex(hex_string, )
    except Exception as e:
        msg = f'Function hexStringToByte - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
        raise Exception(msg)

def binStringToHexString(bin_string):
    try:
        return str(hex(int(bin_string, 2)))[2:]
    except Exception as e:
        msg = f'Function binStringToHexString - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
        raise Exception(msg)

def hexStringToDecimal(hex_string):
    try:
        return int(hex_string, 16)
    except Exception as e:
        msg = f'Function hexStringToDecimal - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
        raise Exception(msg)

def getIds(header_id):
    try:
        binary_value_str = str(bin(int(header_id)))[2:]
        # 24자리가 될 때까지, 앞에 0을 붙여줌.
        formatted_header_id = "{0:0>24}".format(binary_value_str)

        if len(formatted_header_id) > 24:
            raise Exception("Header ID 값이 너무 큽니다.")

        splitted_header_id = [formatted_header_id[:8], formatted_header_id[8:16], formatted_header_id[16:]]

        service_id = hexStringToDecimal(binStringToHexString(splitted_header_id[0]))

        group_hex_str = binStringToHexString(splitted_header_id[1])
        index_hex_str = binStringToHexString(splitted_header_id[2])
        formatted_index_hex_str = "{0:0>2}".format(index_hex_str)
        method_id = hexStringToDecimal(group_hex_str + formatted_index_hex_str)

        return [service_id, method_id]
    except Exception as e:
        msg = f'Function getIds - "{e}" (Line: {sys.exc_info()[-1].tb_lineno})'
        raise Exception(msg)
