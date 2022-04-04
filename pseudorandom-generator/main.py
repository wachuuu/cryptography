from numpy import ones

from bbs import BBS
from bbs_test import BBSTest

SAMPLE_SETUP = {
  'p': 1000003,
  'q': 2001911,
}

def gen_bits(size, file):
  bbs = BBS()
  bbs.generate_bits(size, filepath=file)
  

def run_tests(input_files):
  file = open('testout.txt', 'w')
  for input_file in input_files:
    test = BBSTest(input_file, op='cut')

    file.write(f'Plik: {input_file}\n')

    # test pojedynczych bitow
    (zeros, ones) = test.single_bits_test()
    file.write(f'\tTest pojedynczych bitow\n\t\t0:{zeros}, 1: {ones}\n')
    if (9725 < ones < 10275):
      file.write('\tSPELNIONE\n')
    else:
      file.write('\tNIE SPELNIONE\n')

    # test serii
    series1 = test.series_test(count='ones')
    series0 = test.series_test(count='zeros')
    file.write(f'\n\tTest serii\n\t\tserie dla 0: {series0}\n')
    file.write(f'\t\tserie dla 1: {series1}\n')

    if (2315 < series0[0] < 2685) and \
      (1114 < series0[1] < 1386) and \
      (527 < series0[2] < 723) and \
      (240 < series0[3] < 384) and \
      (103 < series0[4] < 209) and \
      (103 < series0[5] < 209) and \
     (2315 < series1[0] < 2685) and \
      (1114 < series1[1] < 1386) and \
      (527 < series1[2] < 723) and \
      (240 < series1[3] < 384) and \
      (103 < series1[4] < 209) and \
      (103 < series1[5] < 209):
      file.write('\tSPELNIONE\n')
    else: file.write('\tNIE SPELNIONE\n')

    # test dlugiej serii
    max_serie = test.long_series_test()
    file.write(f'\n\tTest dlugiej serii\n\t\tmax seria: {max_serie}\n')
    if (max_serie >= 26):
      file.write('\tNIE SPELNIONE\n')
    else:
      file.write('\tSPELNIONE\n')

    # test pokerowy
    poker_val = test.poker_test()
    file.write(f'\n\tTest pokerowy\n\t\twartosc funkcji: {poker_val}\n')
    if (2.16 < poker_val < 46.17):
      file.write('\tSPELNIONE\n')
    else:
      file.write('\tNIE SPELNIONE\n')

    file.write('\n')
  file.close()
  

def main():
  # gen_bits(size=20000, file='20k_3.txt')
  run_tests(input_files=['20k_1.txt', '20k_2.txt', '20k_3.txt'])

if __name__ == '__main__':
  main()
