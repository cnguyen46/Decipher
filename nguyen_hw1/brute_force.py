# Class  : CSCE 477 - Fall2024
# Author : Cong Nguyen
# Title  : Brute Force methods
# Date   : 09/05/2024
# Description : This program demonstrate how the brute force working on ciphertext.
# This is just for fun, merely my curiosity.

'''
# Function: Shift decipher in brute force.
# Return: A string that contain all deciphered message.
'''
def brute_force(ciphertext) :
  key = 1
  result = ""
  first_50_letters = ciphertext[:50] # Only need first 50 letters.
  while (key < 26):
    current_character = 0
    plaintext = ""
    while (current_character < len(first_50_letters)):
      decipher = ord(first_50_letters[current_character]) - ord('A')
      decipher += key
      decipher = chr(decipher % 26 + ord('A'))
      plaintext += decipher
      current_character += 1
    # Print out all results.
    result += "Secret key #" + str(key) + "\n"
    result += plaintext
    result += "\n\n"
    key += 1
  return result