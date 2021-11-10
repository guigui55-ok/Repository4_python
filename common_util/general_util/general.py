
logger = None

def cnv_tuple_to_str(value,delimita=',') -> str:
    try:
        if isinstance(value, tuple):
            ret = ''
            for buf in value:
                ret += str(buf) + delimita
            if len(ret) > len(delimita):
                ret = ret[:len(ret)-len(delimita)]
            return ret
        else:
            # logger.info('cnv_tuple_to_str : value type is not tuple')
            print('cnv_tuple_to_str : value type is not tuple')
            return value
    except Exception as e:
        logger.exp.error(e)
        return ''

def cnv_int(value) -> int:
    try:
        if not isinstance(value, str):
            return 0
        else:
            if value.isnumeric():
                return int(value)
            else:
                return 0
    except Exception as e:
        logger.exp.error(e)
        return 0
