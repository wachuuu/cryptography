class TrithemiusCipher():
  __ALPHABET=list(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
  __ALPHABET_LENGTH = len(__ALPHABET)

  def encrypt(self, message, step=1):
    output = ''
    if message is None: message=''
    if step is None: step=1
    for index, letter in enumerate(message):
      try:
        new_index = self.__ALPHABET.index(letter) + (index * step)
        output += self.__ALPHABET[new_index % self.__ALPHABET_LENGTH]
      except ValueError:
        output += letter
    return output

  def decrypt(self, message, step=1):
    output = ''
    if message is None: message=''
    if step is None: step=1
    for index, letter in enumerate(message):
      try:
        new_index = self.__ALPHABET.index(letter) - (index * step)
        output += self.__ALPHABET[new_index % self.__ALPHABET_LENGTH]
      except ValueError:
        output += letter
    return output
