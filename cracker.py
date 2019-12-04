import string
from random import choice
from time import sleep

# Gathers all ditis that should be shown while cracking
digit_list = "".join((string.digits,
                      string.ascii_lowercase,
                      string.ascii_uppercase,
                      string.punctuation))

# Defining the colors of the text in bash
CBLINK = '\033[5m'
CRED = '\33[31m'
CEND = '\033[0m'
GRN = '\33[92m'
BOLD = ' \33[1m'
WHITE = '\33[97m'

# The "code" which should be cracked
text = "$i5YPH0S "

print("\n")
for i, x in enumerate(text):
    for digit in digit_list:
        if digit != x:
            print("\r",
                  (''.join(choice(digit_list) for _ in range(len(text)-1))), 
                  text[:i], end="",
                  sep=(BOLD +
                       CRED +
                       CBLINK +
                       "\r Key is being cracked: " +
                       CEND),
                  flush=True)
        sleep(0.016)

sleep(1)
print(WHITE+"\r Key has been cracked! ")
print(BOLD + GRN +
      "\n   [ A C C E S S   G R A N T E D ]" +
      CEND + "\n")
