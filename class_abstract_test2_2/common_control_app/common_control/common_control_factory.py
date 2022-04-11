
import enum
if __name__ == '__main__':
    import __init__

from common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass

class ModelName(enum.Enum):
    MODEL_BASE = 1
    MODEL_A = 2

def get_object(ext_base:ExtendsBaseClass, mode:int):
    if mode == ModelName.MODEL_BASE:
        from common_control_base.common_control_main import CommonActionBase
        ret = CommonActionBase(ext_base)
    elif mode == ModelName.MODEL_A:
        from platform_control_a.common_control_main import CommonActionBase_A
        ret = CommonActionBase_A(ext_base)
    else:
        raise NotImplementedError()
    return ret
