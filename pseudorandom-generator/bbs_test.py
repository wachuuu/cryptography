class BBSTest():
  FILE_LEN = 20000

  def __init__(self, filename, op='cut' or 'substr', start=None, end=None) -> None:
    self.filename = filename
    with open(self.filename, 'r') as file:
      self.bits = file.read()
    if len(self.bits) < self.FILE_LEN: 
      raise ValueError('Input is too short. It must be at least 20000 characters')
    if op == 'cut':
      self.bits = self.bits[:self.FILE_LEN]
    if op == 'substr':
      if start == None or end == None:
        raise ValueError('Provide start & end parameters for "substr" operation')
      if start <= end:
        raise ValueError('Invalid parameters. start shoud not be smaller than end')
      if start > len(self.bits) or end > len(self.bits) or start < 0:
        raise ValueError('Invalid parameters. Parameters should be  in range of a file')


  def single_bits_test(self):
    zeros = 0
    ones = 0
    for bit in self.bits:
      if (bit == '0'):
        zeros += 1
      elif (bit == '1'):
        ones += 1
    return (zeros, ones)

  def series_test(self, count='ones' or 'zeros'):
    if count == 'ones': 
      xbit = '1'
    elif count == 'zeros': 
      xbit = '0'
    counter = 0
    series = [0]*6
    for bit in self.bits:
      if (bit == xbit): counter += 1
      else:
        if counter == 1:
          series[0] += 1
        elif counter == 2:
          series[1] += 1
        elif counter == 3:
          series[2] += 1
        elif counter == 4:
          series[3] += 1
        elif counter == 5:
          series[4] += 1
        elif counter >= 6:
          series[5] += 1
        counter = 0
    return series

  def long_series_test(self):
    curr_length = 0
    current_bit = '0'
    max_length = 0
    for bit in self.bits:
      if bit == current_bit:
        curr_length += 1
      else:
        if curr_length > max_length: max_length = curr_length
        curr_length = 1
        current_bit = bit
    return max_length

  def poker_test(self):
    if len(self.bits) != 20000: raise ValueError('Input must be 20000 chars long')
    num_counts = [0]*16
    for i in range(0, len(self.bits), 4):
      number = int(self.bits[i:i+4], 2)
      num_counts[number]+=1
    val = (16/5000) * sum(i**2 for i in num_counts) - 5000
    return val
