
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
