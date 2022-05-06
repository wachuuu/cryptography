from bitstring import BitArray


class Utils:
  def convert(self, _text, _from, _to):
    if _from == 'bytes':
      if _to == 'bytes':
        return _text
      if _to == 'bits':
        return BitArray(hex=_text.hex()).bin
      if _to == 'hex':
        return _text.hex()

    elif _from == 'bits':
      if _to == 'bytes':
        return BitArray(bin=_text).tobytes()
      if _to == 'bits':
        return _text
      if _to == 'hex':
        return hex(int(_text, 2))
      if _to == 'str':
        return BitArray(bin=_text).tobytes().decode('utf-8')

    elif _from == 'hex':
      if _to == 'bytes':
        return bytes.fromhex(_text)
      if _to == 'bits':
        return BitArray(hex=_text).bin
      if _to == 'hex':
        return _text

    elif _from == 'str':
      if _to == 'bits':
        return BitArray(hex=_text.encode('utf-8').hex()).bin


  def xor(self, a, b):
    return ''.join(map(str, [int(_a) ^ int(_b) for(_a, _b) in zip(a, b)]))
