# Class  : CSCE 477 - Fall2024
# Author : Cong Nguyen
# Title  : Identify Cipher Program
# Date   : 09/18/2024
# Description : This program helps to identify the type of Cipher

from math import gcd
import helper

# Index of Coincidence
IC_ENGLISH = 0.065 # IC for Monoalphabetic (English)
IC_RANDOM = 0.038 # IC for Polyalphabetic (Random)

'''
# Function to define ciphertext is monoalphabet, or polyalphabet.
# Return: monoalphabet, or polyalphabet.
'''
def mono_or_poly_alphabet(indexCoin):
  result = "\nIndex of Coincidence (IC): " + f"{indexCoin}"
  if indexCoin > (IC_ENGLISH + IC_RANDOM) / 2:
    result += "\nThis should be Monoalphabetic Cipher, due to IC approximately 0.065."
  else:
    result += "\nThis should be Polyalphabetic Cipher, due to IC approximately 0.038."
  return result

"""
Function: Determines whether the given ciphertext correspond to a Shift or Affine Cipher or Substitution.
Parameters:
- letter_1 : the most repeated letter in ciphertext
- letter_2 : other most repeated letter in ciphertext
- english_1: the most repeated letter in English text
- english_2: other most repeated letter in English text
Returns: A string indicating whether it's a Shift or Affine Cipher.
Known:
- a: The multiplicative key (should be 1 for Shift Cipher).
- c: The size of the alphabet (default is 26 for English alphabet).
If a = 1                  : The cipher is a Shift Cipher.
If a ≠ 1 and GCD(a, c) = 1: The cipher is an Affine Cipher.
If a ≠ 1 and GCD(a, c) ≠ 1: The cipher is not Shift or Affine Cipher.
"""
def shift_or_affine_or_subtitution_cipher(letter_1, english_1, letter_2, english_2):
  # Calculate the determinant.
  det = (helper.letTonum(english_1) - helper.letTonum(english_2)) % 26
  # No unique solution exists.
  if det == 0:
    return None
  
  # Calculate the modular inverse of the determinant.
  det_inv = helper.modular_inverse(det, 26)
  
  # Calculate a and b.
  a_num = (helper.letTonum(letter_1) - helper.letTonum(letter_2)) % 26
  b_num = (helper.letTonum(english_1) * helper.letTonum(letter_2) - helper.letTonum(english_2) * helper.letTonum(letter_1)) % 26

  a = (det_inv * a_num) % 26
  b = (det_inv * b_num) % 26

  # Output the result.
  result = ""
  result += "\nFound: a = %s, b = %s" % (f"{a}",f"{b}")
  result += "\ngcd(%s,26) = %s" % (f"{a}", f"{gcd(a,26)}")
  if a == 1:
    result += "\nThe ciphertext is likely the Shift Cipher or the Affine Cipher."
  elif (gcd(a, 26) == 1):
    result += "\nThe ciphertext is likely the Affine Cipher."
  else:
    result += "\nUnknown Cipher."
  return result

'''
Function: Determines whether the given cipheretext correspond to a Vigenère or One Time Pads (OTP) Cipher.
Parameters:
- ciphertext: all letters in ciphertext.
- trigram: chosen trigram for anlayzig.
Returns: A string indicating whether it's a Vigenère or OTP.
'''
def vigenere_or_otp_cipher(ciphertext,trigram):
  result = "\n"
  # Kasiski method.
  result += "\nUsing Kasiski method."
  result += "\n---------------------------"
  all_position_of_trigram = helper.find_trigram_positions(ciphertext,trigram)
  group_of_gcd, key_length = helper.find_key_length_kasiski_method(all_position_of_trigram)
  result += "\nGroup of adjacent GCD: \"%s\"" % (trigram)
  result += "\nList of all position of \"%s\": %s" % (trigram, f"{all_position_of_trigram}")
  for num, repeat in group_of_gcd.items():
    result += "\nDistance of %s repeats %s times." % (f"{num}", f"{repeat}")
  result += "\nLength of keyword may likely has the most repeated gcd: %s" % (f"{key_length}")
  
  # Index of Coincidence method.
  result += "\n\nUsing Index of Coincidence method."
  result += "\n-----------------------------"
  average_ics = helper.find_key_length_ic_method(ciphertext, 10)
  best_guess_length = 0
  for length in average_ics:
    result += f"\nKeyword Length: {length}, Average IC: {average_ics.get(length):.4f}"
    if average_ics.get(length) > (IC_ENGLISH + IC_RANDOM) / 2:
      best_guess_length = length
  result += f"\nLength of keyword may likely has the largest IC average: {best_guess_length}"

  # Divide into groups and calculate the IC of each block.
  result += "\n\nKeyword Recovery with x square method."
  result += "\n-------------------------------------------"
  result += helper.table_of_IC(ciphertext, key_length)
  # Decide whether the cipher is Vigenère cipher or One-Time Pad cipher.   
  if (key_length == best_guess_length):
    result += "\n\nThe ciphertext is likely the Vigenere cipher."
  else:
    result += "\n\nThe ciphertext is likely the One-Time Pad cipher."
  return result
  
