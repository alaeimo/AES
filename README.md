![alt text](https://github.com/alaeimo/AES/blob/master/img/AES-Overview.png)

# What is this?

An implementation of the AES algorithm in Python 3.

## Setup

```
pip install -r requirements.txt
```

## Run tests

```
python main.py
```

# Usage

```
from AES import AES
key = "<Enter Your Own Key>"
rounds = 10 # Possible Rounds: 10 or 12 or 14
text = "<Enter Your Own Text or Read It from a File>"
aes = AES(key,rounds)
```

## Encrypt

```
encrypted = aes.encrypt(text)
print(encrypted)
```

## Decrypt

```
decrypted = aes.decrypt(encrypted)
print(decrypted)
```

# References

1.  [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
