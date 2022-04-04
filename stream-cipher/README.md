# Stream cipher

Implemented stream cipher using BBS pseudo-random generator

#### Setup
Run `main.py` using Python interpreter as follows:
```
$> python main.py
```

#### scripts:
- `main.py` - main script where you can encrypt and decrypt files
- `cipher.py` - implementation of stream cipher
- `bbs.py` - Blum Blum Shub algorithm for pseudo-random bit streams
- `utils.py` - utilities for managing data and operating on bitstrings

#### auxilliary files:
- `logs.txt` - file that stores logs and parameters of the cipher, you can provide additional description and save BBS settings for later
- `input.txt` - sample ~20k bit long message for encryption
- `ciphertext.txt` - ciphertext stored as stream of bits, you can test it using pseudo-random stream test from [here](https://github.com/wachuuu/cryptography/tree/main/pseudorandom-generator)
- `decrypted.txt` - decrypted `ciphertext.txt`. It should be same as `input.txt`
