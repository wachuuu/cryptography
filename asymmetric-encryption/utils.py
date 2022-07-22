def xgcd(a, b):
  x, old_x = 0, 1
  y, old_y = 1, 0

  while (b > 0):
      quotient = a // b
      a, b = b, a - quotient * b
      old_x, x = x, old_x - quotient * x
      old_y, y = y, old_y - quotient * y

  return a, old_x, old_y
