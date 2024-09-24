# Class  : CSCE 477 - Fall2024
# Author : Cong Nguyen
# Title  : File I/O
# Date   : 09/04/2024
# Description : This program is used for input/ output the message.

'''
# Function to open the txt file.
# Return: The string of message.
'''
def read_file(ciphertext):
  with open(ciphertext, "r") as file:
    message = file.read()
    file.close
  return message

'''
# Function to output the decipher message.
'''
def write_file(plaintext, filename):
  with open(filename, "w") as file:
    file.write(plaintext)
    file.close