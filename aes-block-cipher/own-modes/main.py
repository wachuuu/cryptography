from secrets import token_bytes

from bitstring import BitArray
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher:
  ENCODING_TYPE = 'ascii'
  BLOCK_SIZE = 16
  key = token_bytes(16)
  cipher = AES.new(key, AES.MODE_ECB)


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

    elif _from == 'hex':
      if _to == 'bytes':
        return bytes.fromhex(_text)
      if _to == 'bits':
        return BitArray(hex=_text).bin
      if _to == 'hex':
        return _text

  def xor(self, a, b):
    a = self.convert(a, 'bytes', 'bits')
    b = self.convert(b, 'bytes', 'bits')
    xor = ''.join(map(str, [int(_a) ^ int(_b) for(_a, _b) in zip(a, b)]))
    return self.convert(xor, 'bits', 'bytes')

  def ECBencrypt(self, msg, output_format='bytes'):
    ciphertext = self.cipher.encrypt(pad(msg.encode(self.ENCODING_TYPE), self.BLOCK_SIZE, style='pkcs7'))
    return self.convert(ciphertext, 'bytes', output_format)

  def ECBdecrypt(self, ciphertext, input_format='bytes'):
    plaintext = unpad(self.cipher.decrypt(self.convert(ciphertext, input_format, 'bytes')), self.BLOCK_SIZE).decode(self.ENCODING_TYPE)
    return plaintext

  def CBCencrypt(self, msg, init_vector, output_format='bytes'):
    padded = pad(msg.encode(self.ENCODING_TYPE), self.BLOCK_SIZE, style='pkcs7')
    blocks = [ padded[i : i + self.BLOCK_SIZE] for i in range(0, len(padded), self.BLOCK_SIZE) ]
    encrypted_blocks = [None] * len(blocks)
    for index, block in enumerate(blocks):
      if index == 0:
        encrypted_blocks[index] = self.cipher.encrypt(self.xor(init_vector, block))
      else:
        encrypted_blocks[index] = self.cipher.encrypt(self.xor(encrypted_blocks[index - 1], block))
    return self.convert(b''.join(encrypted_blocks), 'bytes', output_format)

  def CBCdecrypt(self, ciphertext, init_vector, input_format='bytes'):
    ciphertext = self.convert(ciphertext, input_format, 'bytes')
    blocks = [ ciphertext[i : i + self.BLOCK_SIZE] for i in range(0, len(ciphertext), self.BLOCK_SIZE) ]
    decrypted_blocks = [None] * len(blocks)
    for index, block in enumerate(blocks):
      if index == 0:
        decrypted_blocks[index] = self.xor(init_vector, self.cipher.decrypt(block))
      else:
        decrypted_blocks[index] = self.xor(blocks[index - 1], self.cipher.decrypt(block))
    return unpad(b''.join(decrypted_blocks), self.BLOCK_SIZE).decode(self.ENCODING_TYPE)

  def PBCencrypt(self, msg, init_vector, output_format='bytes'):
    padded = pad(msg.encode(self.ENCODING_TYPE), self.BLOCK_SIZE, style='pkcs7')
    blocks = [ padded[i : i + self.BLOCK_SIZE] for i in range(0, len(padded), self.BLOCK_SIZE) ]
    encrypted_blocks = [None] * len(blocks)
    for index, block in enumerate(blocks):
      if index == 0:
        encrypted_blocks[index] = self.cipher.encrypt(self.xor(init_vector, block))
      else:
        encrypted_blocks[index] = self.cipher.encrypt(self.xor(blocks[index - 1], block))
    return self.convert(b''.join(encrypted_blocks), 'bytes', output_format)

  def PBCdecrypt(self, ciphertext, init_vector, input_format='bytes'):
    ciphertext = self.convert(ciphertext, input_format, 'bytes')
    blocks = [ ciphertext[i : i + self.BLOCK_SIZE] for i in range(0, len(ciphertext), self.BLOCK_SIZE) ]
    decrypted_blocks = [None] * len(blocks)
    for index, block in enumerate(blocks):
      if index == 0:
        decrypted_blocks[index] = self.xor(init_vector, self.cipher.decrypt(block))
      else:
        decrypted_blocks[index] = self.xor(decrypted_blocks[index - 1], self.cipher.decrypt(block))
    return unpad(b''.join(decrypted_blocks), self.BLOCK_SIZE).decode(self.ENCODING_TYPE)


def encrypt(message, mode='ECB', format='bytes', debug=False):
  aes = AESCipher()
  iv = token_bytes(16)

  if mode == 'ECB':
    if(debug): print('---------------- ECB mode ----------------')
    if(debug): print('Original message: ', message)
    if(debug): print(f'Encryption key ({format}): ', aes.convert(aes.key, 'bytes', format))

    ct = aes.ECBencrypt(msg, output_format=format)
    pt = aes.ECBdecrypt(ct, input_format=format)
    
    print(f'Ciphertext ({format}): ', ct)
    if(debug): print('Decrypted message: ', pt)
    if(debug): print('------------------------------------------')

  elif mode == 'CBC':
    if(debug): print('---------------- CBC mode ----------------')
    if(debug): print('Original message: ', message)
    if(debug): print(f'Encryption key ({format}): ', aes.convert(aes.key, 'bytes', format))
    if(debug): print(f'Initial vector: ({format}): ', aes.convert(iv, 'bytes', format))

    ct = aes.CBCencrypt(msg, iv, output_format=format)
    pt = aes.CBCdecrypt(ct, iv, input_format=format)

    print(f'Ciphertext ({format}): ', ct)
    if(debug): print('Decrypted message: ', pt)
    if(debug): print('------------------------------------------')

  elif mode == 'PBC':
    if(debug): print('---------------- PBC mode ----------------')
    if(debug): print('Original message: ', message)
    if(debug): print(f'Encryption key ({format}): ', aes.convert(aes.key, 'bytes', format))
    if(debug): print(f'Initial vector: ({format}): ', aes.convert(iv, 'bytes', format))

    ct = aes.PBCencrypt(msg, iv, output_format=format)
    pt = aes.PBCdecrypt(ct, iv, input_format=format)

    print(f'Ciphertext ({format}): ', ct)
    if(debug): print('Decrypted message: ', pt)
    if(debug): print('------------------------------------------')


if __name__ == '__main__':
  # available modes: ECB, CBC, PBC
  # available fomats: bytes, bits, hex
  msg = input('Type message here: ')
  format = input('Choose format (hex, bytes, bits): ')
  encrypt(msg, mode='ECB', format=format, debug=True)
  encrypt(msg, mode='CBC', format=format, debug=True)
  encrypt(msg, mode='PBC', format=format, debug=True)
