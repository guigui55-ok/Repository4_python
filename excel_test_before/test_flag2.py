
class Direction():
    LEFT = 1 << 0  # 0000000001 in binary
    TOP = 1 << 1  # 0000000010 in binary
    RIGHT = 1 << 2  # 0000000100 in binary
    BOTTOM = 1 << 3 # 0000001000 in binary

def _set_dirction(direction):
    """ 方向をセットする、何もない場合はRIGHT,BOTTOMとする """
    horizon = None
    if Direction.RIGHT & direction:
        horizon = Direction.RIGHT
    else:
        horizon = Direction.LEFT
    vertical = None
    if Direction.BOTTOM & direction:
        vertical = Direction.BOTTOM
    else:
        vertical = Direction.TOP
    return horizon | vertical

####
direction = _set_dirction(Direction.LEFT)

if Direction.LEFT & direction:
    is_left = True
else:
    #Direction.RIGHT & direction:
    is_left = False
print('is_left = {}'.format(is_left))