# Class  : CSCE 477 - Fall2024
# Author : Cong Nguyen
# Title  : Main program 
# Date   : 09/04/2024
# Description : This program is used for outputing the decipher message.

import sys
import decrypt
import keys

# Main programming to decipher the cipher text.
def deciphering():
  print('''
        The hacker plants the malware inside your computer.
        Your mission is to detect and defuse the malware. Knowing that it has 4 phases.
        Try to find the correct key to defuse the it. Inputing wrong key will cause the whole data be deleted.
        REMEMBER YOU ONLY HAVE ONE CHANCE TO TYPE CORRECT KEY FOR EACH PHASE.

        *** IMPORTANT: You can find more hints at the analysis folder. ***
        ''')
  # Decrpyt Ciphertext #1.
  cipherText_1 = "../nguyen_hw1/ciphertext/cipher1.txt"
  try:
    print("Hint: Only 1 number for phase 1.")
    key_1 = int(input("Enter Key 1 or Press Ctrl + C to give up: "))
    if (key_1 != keys.CORRECT_KEY_1):
      raise ValueError("Incorrect Key! 3... 2... 1")
    print("Good start! 3 more to go.")
  except ValueError as e:
    print(e)
    print("KBOOM!!! All data are gone. Try again next time.\n")
    sys.exit()
  plaintext_1 = "../nguyen_hw1/plaintext/plaintext1.txt"
  decrypt.cipher1(cipherText_1,key_1,plaintext_1)

  # Decrpyt Ciphertext #2.
  cipherText_2 = "../nguyen_hw1/ciphertext/cipher2.txt"
  try:
    print("\nHint: Need 2 numbers for phase 2.")
    key_2 = list(map(int,(input("Enter Key 2 or Press Ctrl + C to give up: ").split()))) # For example, to input the key, type: 0 0
    if (key_2 != keys.CORRECT_KEY_2):
      raise ValueError("Incorrect Key! 3... 2... 1")
    print("Nicely done! 2 keys left.")
  except ValueError as e:
    print(e)
    print("KBOOM!!! All data are gone. At least you got first key. Try again next time.\n")
    sys.exit()
  plaintext_2 = "../nguyen_hw1/plaintext/plaintext2.txt"
  decrypt.cipher2(cipherText_2,key_2,plaintext_2)

  # Decrpyt Ciphertext #3.
  cipherText_3 = "../nguyen_hw1/ciphertext/cipher3.txt"
  try:
    print("\nHint: Find the familiar number between cipher 3 and cipher 4.")
    key_3 = int(input("Enter Key 3 or Press Ctrl + C to give up: "))
    if (key_3 != keys.CORRECT_KEY_3):
      raise ValueError("Incorrect Key! 3... 2... 1")
    print("Wonderful! I cannot believe you can decrypt this ciphertext. Only one left.")
  except ValueError as e:
    print(e)
    print("KBOOM!!! All data are gone. This is the hard one. I can understand. Try again next time.\n")
    sys.exit()
  plaintext_3 = "../nguyen_hw1/plaintext/plaintext3.txt"
  decrypt.cipher3(cipherText_3,key_3,plaintext_3)

  # Decrpyt Ciphertext #4.
  cipherText_4 = "../nguyen_hw1/ciphertext/cipher4.txt"
  try:
    print("\nNo more hint... because they are already showed in analysis file.")
    key_4 = str(input("Enter Key 4 or Press Ctrl + C to give up: "))
    if (key_4 != keys.CORRECT_KEY_4):
      raise ValueError("Incorrect Key! 3... 2... 1")
    print("Congrat! (@^_^@) You successfully break the malware. Good job on saving your computer.")
  except ValueError as e:
    print(e)
    print("KBOOM!!! All data are gone. Ouch (>>_<<) you're so closed. Try again next time.\n")
    sys.exit()
  plaintext_4 = "../nguyen_hw1/plaintext/plaintext4.txt"
  decrypt.cipher4(cipherText_4,key_4,plaintext_4)
  
  print("\nNow, you can go to \"plaintext\" folder to see all plaintext 1, 2, and 4.")
  print("Ciphertext 3 is discovered as One-Time Pads Cipher, so the key is nearly unbreakable.\n")

if __name__=="__main__":
  deciphering()