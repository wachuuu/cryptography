import random

import cv2
import numpy as np


def getNoise(color):
  choice = random.randint(0, 5)
  black_moves = [
  # ((share1),     (share2))
    ((255, 255, 0, 0), (0, 0, 255, 255)), 
    ((255, 0, 255, 0), (0, 255, 0, 255)), 
    ((255, 0, 0, 255), (0, 255, 255, 0)), 
    ((0, 0, 255, 255), (255, 255, 0, 0)), 
    ((0, 255, 0, 255), (255, 0, 255, 0)), 
    ((0, 255, 255, 0), (255, 0, 0, 255)), 
  ]

  white_moves = [
  # ((share1),     (share2))
    ((255, 255, 0, 0), (255, 255, 0, 0)), 
    ((255, 0, 255, 0), (255, 0, 255, 0)), 
    ((255, 0, 0, 255), (255, 0, 0, 255)), 
    ((0, 0, 255, 255), (0, 0, 255, 255)), 
    ((0, 255, 0, 255), (0, 255, 0, 255)), 
    ((0, 255, 255, 0), (0, 255, 255, 0)), 
  ]

  if color == 'white':
    return white_moves[choice]
  return black_moves[choice]

class VisualCipher():
  def encrypt(self, filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    share_1 = np.zeros((img.shape[0]*2, img.shape[1]*2), dtype=np.uint8)
    share_2 = np.zeros((img.shape[0]*2, img.shape[1]*2), dtype=np.uint8)

    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    for i in range(img.shape[0]):
      for j in range(img.shape[1]):
        color = 'black'
        if img[i][j] == 0:
          color = 'white'
        # (top left,                   top right,             bottom left,           bottom right) 
        ( ( share_1[(2*i)-1][(2*j)-1], share_1[(2*i)-1][2*j], share_1[2*i][(2*j)-1], share_1[2*i][2*j] ), 
          ( share_2[(2*i)-1][(2*j)-1], share_2[(2*i)-1][2*j], share_2[2*i][(2*j)-1], share_2[2*i][2*j] )
        ) = getNoise(color)

    cv2.imwrite('./static/share1.png', share_1)
    cv2.imwrite('./static/share2.png', share_2)

    return 'share1.png', 'share2.png'

  def decrypt(self, file1, file2):
    share1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    share2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)
    if share1.shape != share2.shape: return

    output = np.zeros(share1.shape, dtype=np.uint8)

    for i in range(share1.shape[0]):
      for j in range(share1.shape[1]):
        output[i][j] = max(share1[i][j], share2[i][j])
    
    cv2.imwrite('./static/decrypted.png', output)
    return 'decrypted.png'
