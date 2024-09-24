# Class  : CSCE 477 - Fall2024
# Author : Cong Nguyen
# Title  : Decipher program
# Date   : 09/04/2024
# Description : This program contains method for deciphering the message.

import helper

'''
# Function: Shift decipher.
# Return: A string that contain all deciphered message.
'''
def shift_decrypt(ciphertext, key) :
  plaintext = ""
  current_character = 0
  while (current_character < len(ciphertext)):
    decipher = ord(ciphertext[current_character]) - ord('A')
    decipher += key
    decipher = chr(decipher % 26 + ord('A'))
    plaintext += decipher
    current_character += 1
  return plaintext

'''
# Function: Affine decipher.
# Return  : A string that contain all deciphered message.
'''
def affine_decrypt(ciphertext, key):
  plaintext = ""
  decipher = 0
  # Decipher process.
  for letter in ciphertext:
    decipher = ((helper.letTonum(letter) - key[1]) * helper.modInverse(key[0])) % 26
    plaintext += helper.numTolet(decipher)
  return plaintext

'''
# Function: Vigenere decipher.
# Return  : A string that contain all deciphered message.
'''
def vigenere_decrypt(ciphertext, key):
  plaintext = ""
  letter = 0
  # Create a reapeated key words.
  for element in range(len(ciphertext) - len(key)):
    key += key[element % len(key)]
  
  # Decipher process.
  while (letter < len(ciphertext)):
    decipher = chr((ord(ciphertext[letter]) - ord(key[letter]) + 26) % 26 + ord('A'))
    plaintext += decipher
    letter += 1
  return plaintext

