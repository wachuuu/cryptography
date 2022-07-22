from math import gcd
from random import randint

from Crypto.Util import number

from utils import xgcd


class RSA:
  PRIME_SIZE_LOWER = 1000
  PRIME_SIZE_UPPER = 1000

  def __get_prime(self):
    return number.getPrime(randint(self.PRIME_SIZE_LOWER, self.PRIME_SIZE_UPPER))

  def __get_p_q(self):
    p = self.__get_prime()
    q = self.__get_prime()
    while (p == q):
      q = self.__get_prime()
    return p, q

  def __get_n(self):
    return self.__q * self.__p

  def __get_phi(self):
    return (self.__p - 1) * (self.__q - 1)

  def __get_e(self):
    candidate = randint(3, (self.__phi - 1))
    while gcd(candidate, self.__phi) != 1:
      candidate = randint(3, (self.__phi - 1))
    return candidate

  def __get_d(self):
    _, x, _ = xgcd(self.__e, self.__phi)
    return x if x > 0 else x + self.__phi

  def __init__(self, p=None, q=None, e=None, d=None) -> None:
    (self.__p, self.__q) = (p, q) if (p and q) else self.__get_p_q()
    self.__n = self.__get_n()
    self.__phi = self.__get_phi()
    self.__e = e if e else self.__get_e()
    self.__d = d if d else self.__get_d()

  def __str__(self) -> str:
    return f'p: {self.__p}, q: {self.__q}, n: {self.__n}, phi: {self.__phi}, e: {self.__e}, d: {self.__d}'
  
  def get_private_key(self):
    return self.__d, self.__n

  def set_private_key(self, d, n):
    self.__d = d 
    self.__n = n

  def get_public_key(self):
    return self.__e, self.__n

  def set_public_key(self, e, n):
    self.__e = e
    self.__n = n

  def encrypt(self, message) -> str:
    ciphertext = ''
    for char in message:
      c = pow(ord(char), self.__e, self.__n)
      ciphertext += f'{c} '
    return ciphertext

  def decrypt(self, ciphertext) -> str:
    message = ''
    cipher_blocks = [int(x) for x in ciphertext[:-1].split(' ')]
    for num in cipher_blocks:
      m = chr(pow(num, self.__d, self.__n))
      message += m
    return message

if __name__ == '__main__':
  mess = 'some message to encrypt'
  rsa = RSA()
  print(rsa.get_private_key())
  print(rsa.get_public_key())
  c = rsa.encrypt(mess)
  print(c)
  m = rsa.decrypt(c)
  print(m)
