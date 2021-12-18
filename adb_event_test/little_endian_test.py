hex_be = 'f0148c'
hex_be = '000f0148c' # ValueError: non-hexadecimal number found in fromhex() arg at position 9
hex_be = '0x000f0148c' # non-hexadecimal number found in fromhex() arg at position 1
hex_be = '0' # ValueError: non-hexadecimal number found in fromhex() arg at position 1
hex_be = '00'
hex_be = '0x00' # ValueError: non-hexadecimal number found in fromhex() arg at position 1
hex_be = '0100' # 0001
hex_be = '0010' # 1000
hex_be = '00f0'
hex_be = '00000258'
bytes_be = bytes.fromhex(hex_be)
bytes_le = bytes_be[::-1]
hex_le = bytes_le.hex()
hex_le  # '8c14f0'

print(hex_le)