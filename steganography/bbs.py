from math import gcd
from random import randint

from Crypto.Util import number


class BBS:
  PRIME_SIZE_LOWER = 19
  PRIME_SIZE_UPPER = 21

  def __get_prime(self):
    return number.getPrime(randint(self.PRIME_SIZE_LOWER, self.PRIME_SIZE_UPPER))

  def __init__(self, p=None, q=None, seed=None) -> None:
    (self._p, self._q) = (p, q) if (p and q) else self.__generate_blum_numbers()
    self._n = self._q * self._p
    self.seed = seed if seed else self.__generate_seed()

  def __str__(self) -> str:
    return f'p: {self._p}, q: {self._q}, seed: {self.seed}'

  def __generate_blum_numbers(self):
    p = self.__get_prime()
    while ((p - 3) % 4 != 0):
      p = self.__get_prime()
    q = self.__get_prime()
    while ((q != p) and ((q - 3) % 4 != 0)):
      q = self.__get_prime()
    return p, q

  def __generate_seed(self) -> int:
    seed_candidate = randint(1, self._n - 1)
    while gcd(seed_candidate, self._n) != 1:
      seed_candidate = randint(1, self._n - 1)
    return seed_candidate

  def generate_bits(self, length, show_properties=False, filepath=None) -> str or None:
    next_val = pow(self.seed, 2, self._n) # x0 = (seed^2) % n
    bits = str(next_val % 2)
    for _ in range(1, length):
      next_val = pow(next_val, 2, self._n)
      bits += str(next_val % 2)
    if filepath:
      fp = open(filepath, 'w')
      if show_properties: fp.write(f'{self._p};{self._q};{self.seed}\n')
      fp.write(bits)
      fp.close()
    else:
      return bits
