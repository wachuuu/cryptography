from cipher import StreamCipher


def main():
  # cipher = StreamCipher(p=350087, q=417379, seed=127879458143)
  # or
  cipher = StreamCipher()
  
  # encryption message written in plain text
  cipher.encrypt('input.txt', 'ciphertext.txt', inputformat='str')
  
  # saving p, q and seed for later (just in case)
  cipher.savelogs('encrypted input.txt')

  # manipulation cipher properties
  (p, q, s) = cipher.get_cipher_properties()
  cipher.set_cipher_properties(p=p, q=q, seed=s)
  
  # decrypting file
  cipher.decrypt('ciphertext.txt', 'decrypted.txt', outputformat='str')
  cipher.savelogs('decrypted ciphertext.txt and saved in decrypted.txt')

if __name__ == '__main__':
  main()
