import time
from secrets import token_bytes

from bitstring import BitArray
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from cipher import AESCipher

KEY = token_bytes(16)
IV = token_bytes(16)

def num_format(number):
  return format(number*1000, ".8f").replace(".",",")

def count_time(mode):
  short, medium, long = read_benchmark_files()
  results = []

  time_start = time.perf_counter()
  ct = encrypt(mode, short)
  time_end = time.perf_counter()
  time_enc = time_end - time_start

  time_start = time.perf_counter()
  decrypt(mode, ct)
  time_end = time.perf_counter()
  time_dec = time_end - time_start
  results.append((time_enc, time_dec))

  time_start = time.perf_counter()
  ct = encrypt(mode, medium)
  time_end = time.perf_counter()
  time_enc = time_end - time_start

  time_start = time.perf_counter()
  decrypt(mode, ct)
  time_end = time.perf_counter()
  time_dec = time_end - time_start
  results.append((time_enc, time_dec))

  time_start = time.perf_counter()
  ct = encrypt(mode, long)
  time_end = time.perf_counter()
  time_enc = time_end - time_start

  time_start = time.perf_counter()
  decrypt(mode, ct)
  time_end = time.perf_counter()
  time_dec = time_end - time_start
  results.append((time_enc, time_dec))
  return results

def times():
  open('results-dec.txt', 'w').close()
  open('results-enc.txt', 'w').close()
  file_dec = open('results-dec.txt', 'a')
  file_enc = open('results-enc.txt', 'a')

  mode = 'ecb'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'cbc'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'cfb'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'ofb'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'ctr'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'ccm'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'eax'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'gcm'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'siv'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  mode = 'ocb'
  times = count_time(mode)
  file_enc.write(f'{mode.upper()}\t{num_format(times[0][0])}\t{num_format(times[1][0])}\t{num_format(times[2][0])}\n')
  file_dec.write(f'{mode.upper()}\t{num_format(times[0][1])}\t{num_format(times[1][1])}\t{num_format(times[2][1])}\n')

  file_enc.close()
  file_dec.close()

def read_benchmark_files():
  fs = open('mess-short.txt', 'r')
  fm = open('mess-medium.txt', 'r')
  fl = open('mess-long.txt', 'r')
  short = fs.read()
  medium = fm.read()
  long = fl.read()
  return short, medium, long

def read_manipulation_files():
  fala = open('ala-ma-kota.txt', 'r')
  faa = open('aaa.txt', 'r')
  falph = open('alphabet.txt', 'r')
  text_ala = fala.read()
  text_aa = faa.read()
  text_alph = falph.read()
  return text_ala, text_aa, text_alph

def encrypt(mode, plaintext):
  cipher = AESCipher()
  if mode == 'ecb':
    return cipher.ECBencrypt(plaintext)
  elif mode == 'cbc':
    return cipher.CBCencrypt(plaintext, init_vector=IV)
  elif mode == 'pbc':
    return cipher.PBCencrypt(plaintext, init_vector=IV)

def decrypt(mode, ciphertext):
  cipher = AESCipher()
  if mode == 'ecb':
    return cipher.ECBdecrypt(ciphertext)
  elif mode == 'cbc':
    return cipher.CBCdecrypt(ciphertext, init_vector=IV)
  elif mode == 'pbc':
    return cipher.PBCdecrypt(ciphertext, init_vector=IV)

def delete_block(ciphertext):
  blocks = [ ciphertext[i : i + AES.block_size] for i in range(0, len(ciphertext), AES.block_size) ]
  _ = blocks.pop(1)
  return b''.join(blocks)

def duplicate_block(ciphertext):
  blocks = [ ciphertext[i : i + AES.block_size] for i in range(0, len(ciphertext), AES.block_size) ]
  blocks.insert(1, blocks[0])
  return b''.join(blocks)

def swap_blocks(ciphertext):
  blocks = [ ciphertext[i : i + AES.block_size] for i in range(0, len(ciphertext), AES.block_size) ]
  blocks[1], blocks[2] = blocks[2], blocks[1]
  return b''.join(blocks)

def add_new_block(ciphertext):
  new_block = AES.new(KEY, AES.MODE_ECB).encrypt('-thisisnewblock-'.encode('utf-8'))
  blocks = [ ciphertext[i : i + AES.block_size] for i in range(0, len(ciphertext), AES.block_size) ]
  blocks.insert(1, new_block)
  return b''.join(blocks)

def change_one_bit(ciphertext):
  bits = list(AESCipher().convert(ciphertext, 'bytes', 'bits'))
  if(bits[146] == '0'): bits[146] = '1' 
  else: bits[146] = '0'
  return AESCipher().convert(''.join(bits), 'bits', 'bytes')

def swap_bytes(ciphertext):
  hex = list(ciphertext.hex())
  hex[36:38], hex[38:40] = hex[38:40], hex[36:38]
  return bytes.fromhex(''.join(hex))

def delete_byte(ciphertext):
  hex = list(ciphertext.hex())
  _ = hex.pop(56); hex.pop(56)
  hex.append('00')
  return bytes.fromhex(''.join(hex))


def manipulation_tests():
  path = 'results-delbyte.txt'
  modes = ['ecb', 'cbc', 'pbc']

  open(path, 'w').close()
  file = open(path, 'a')
  ala, aaa, alph = read_manipulation_files()

  file.write(f'{ala}\n')
  file.write(f'{aaa}\n')
  file.write(f'{alph}\n')

  for mode in modes:
    ct_ala = delete_byte(encrypt(mode, ala))
    pt_ala = decrypt(mode, ct_ala)
    file.write(f'{pt_ala}\n')

  for mode in modes:
    ct_aaa = delete_byte(encrypt(mode, aaa))
    pt_aaa = decrypt(mode, ct_aaa)
    file.write(f'{pt_aaa}\n')
    
  for mode in modes:    
    ct_alph = delete_byte(encrypt(mode, alph))
    pt_alph = decrypt(mode, ct_alph)
    file.write(f'{pt_alph}\n')

  file.close()


if __name__ == '__main__':
  manipulation_tests()
