import time

from bbs import BBS
from utils import Utils


class StreamCipher(BBS, Utils):
  def __init__(self, p=None, q=None, seed=None) -> None:
    super().__init__(p, q, seed)

  def savelogs(self, info):
    with open('logs.txt', 'a') as file:
      file.write(f'time: {time.ctime()}\n')
      file.write(f'info: {info}\n')
      file.write(f'p: {self._p}\tq: {self._q}\tseed: {self.seed}\n\n')

  def encrypt(self, inputfile, outputfile=None, inputformat='str' or 'bits'):
    with open(inputfile, 'r') as file:
      message = self.convert(file.read(), inputformat, 'bits')
    key = self.generate_bits(len(message))
    ciphertext = self.xor(message, key)
    if (outputfile):
      with open(outputfile, 'w') as file:
        file.write(ciphertext)
    else: return ciphertext

  def decrypt(self, inputfile, outputfile=None, outputformat='str' or 'bits'):
    with open(inputfile, 'r') as file:
      message = file.read()
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
    