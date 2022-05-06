import cv2

from bbs import BBS
from utils import Utils


class StreamCipher(BBS, Utils):
  def __init__(self, p=None, q=None, seed=None) -> None:
    super().__init__(p, q, seed)

  def encrypt(self, input, outputfile=None, inputformat='str' or 'bits'):
    message = self.convert(input, inputformat, 'bits')
    key = self.generate_bits(len(message))
    ciphertext = self.xor(message, key)
    if (outputfile):
      with open(outputfile, 'w') as file:
        file.write(ciphertext)
    else: return ciphertext

  def decrypt(self, input, outputfile=None, outputformat='str' or 'bits'):
    message = input
    key = self.generate_bits(len(message))
    ciphertext = self.xor(message, key)
    if (outputfile):
      with open(outputfile, 'w') as file:
        file.write(self.convert(ciphertext, 'bits', outputformat))
    else: return self.convert(ciphertext, 'bits', outputformat)

  def set_cipher_properties(self, p, q, seed):
    self._p = p
    self._q = q
    self.seed = seed

  def get_cipher_properties(self):
    return (self._p, self._q, self.seed)
    


class SteganographyCipher:  
  def encrypt(self, message, filename, debug=False, inputformat='str' or 'bits'):
    img = cv2.imread(filename)
    height, width, channels = img.shape
    if filename.endswith('.jpg'):
      raise ValueError('Inappropriate image format. Avaiable formats: .png, .bmp')
    if channels < 3:
      raise ValueError('Inappropriate image format')
    if inputformat == 'str':
      bit_msg = Utils().convert(message, 'str', 'bits')
    else: bit_msg = message
    if len(bit_msg) > (height*width*3-24):
      raise ValueError('Message too long')

    prefix = '{:0>24b}'.format(len(bit_msg))
    msg_to_encrypt = f'{prefix}{bit_msg}'
    print('len: ', len(bit_msg), ' full len: ', len(msg_to_encrypt))
    for index, elem in enumerate(msg_to_encrypt):
      color = (img[int(index / (width * 3))][int(index / 3) % width][index % 3])
      if elem != str(color % 2):
        color_bin = '{0:b}'.format(color)
        color_bin = color_bin[:-1] + elem
        new_color = int(color_bin, 2)
        if(debug): new_color = int(elem)
        img[int(index / (width * 3))][int(index / 3) % width][index % 3] = new_color
    if filename.endswith('.bmp'):
      cv2.imwrite(f'./static/encrypted.bmp', img)
      return 'encrypted.bmp'
    else: 
      cv2.imwrite(f'./static/encrypted.png', img)
      return 'encrypted.png'

  def decrypt(self, filename, debug=False):
    img = cv2.imread(filename)
    length_bin = ''
    message_bin = ''
    height, width, channels = img.shape

    if channels < 3:
      raise ValueError('Inappropriate image format')
    for i in range(24):
      color = img[0][int(i / 3)][i % 3]
      color_bin = '{0:b}'.format(color)
      length_bin += color_bin[-1]
    msg_length = int(length_bin, 2)

    if msg_length > (height*width*3-24):
      raise ValueError('Encrypted message is invalid')

    for index in range(24, 24+msg_length):
      color = (img[int(index / (width * 3))][int(index / 3) % width][index % 3])
      color_bin = '{0:b}'.format(color)
      message_bin += color_bin[-1]

    message = Utils().convert(message_bin, 'bits', 'str')
    return message
