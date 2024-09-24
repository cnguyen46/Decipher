# Class  : CSCE 477 - Fall2024
# Author : Cong Nguyen
# Title  : All ciphertext
# Date   : 09/17/2024
# Description : This program contains all steps to decryt the ciphertext.

import crytanalysis
import brute_force
import decipherMethod
import textFile
import identifyCipher

'''
Steps by Steps to decipher cipher1.txt
'''
def cipher1(ciphertext,key,plaintext):
  # Input the file.
  message = textFile.read_file(ciphertext)
  
  # Analyzing the ciphertext.
  analysis = "***Analyzing Ciphertext #1***\n"
  analysis += crytanalysis.analysing(message)

  # Identify the type of Cipher. After doing crytanalysis
  # Choose U - E, J - T or J - E, U - T
  analysis += "\n\nChoose: U - E, J - T."
  analysis += identifyCipher.shift_or_affine_or_subtitution_cipher("U", "E", "J", "T")
  analysis += "\n\nChoose: J - E, U - T."
  analysis += identifyCipher.shift_or_affine_or_subtitution_cipher("J", "E", "U", "T")
  textFile.write_file(analysis,"../nguyen_hw1/analysis/analysis1.txt")

  # Choosing Shift Decipher method after analyzing.
  decipher_text = decipherMethod.shift_decrypt(message,key)

  # Output to the file.
  textFile.write_file(decipher_text,plaintext)

  # Attemping Brute Force.
  bf_result = brute_force.brute_force(message)
  textFile.write_file(bf_result,"../nguyen_hw1/brute_force/brute_force1.txt")

'''
Steps by Steps to decipher cipher2.txt
'''
def cipher2(ciphertext,key,plaintext):
  # Input the file.
  message = textFile.read_file(ciphertext)
  
  # Analyzing the ciphertext.
  analysis = "***Analyzing Ciphertext #2***\n"
  analysis += crytanalysis.analysing(message)
  textFile.write_file(analysis,"../nguyen_hw1/analysis/analysis2.txt")

  # Identify the type of Cipher. After doing crytanalysis
  # Choose G - E, V - T, or V - E, G - T
  analysis += "\n\nChoose: G - E, V - T."
  analysis += identifyCipher.shift_or_affine_or_subtitution_cipher("G", "E", "V", "T")
  analysis += "\n\nChoose: V - E, G - T."
  analysis += identifyCipher.shift_or_affine_or_subtitution_cipher("V", "E", "G", "T")
  textFile.write_file(analysis,"../nguyen_hw1/analysis/analysis2.txt")

  # Choosing Affine Decipher method after analyzing.
  decipher_text = decipherMethod.affine_decrypt(message,key)

  # Output to the file.
  textFile.write_file(decipher_text,plaintext)

  # Attemping Brute Force.
  bf_result = brute_force.brute_force(message)
  textFile.write_file(bf_result,"../nguyen_hw1/brute_force/brute_force2.txt")

'''
Steps by Steps to decipher cipher3.txt
'''
def cipher3(ciphertext,key,plaintext):
  # Input the file.
  message = textFile.read_file(ciphertext)
  
  # Analyzing the ciphertext.
  analysis = "***Analyzing Ciphertext #3***\n"
  analysis += crytanalysis.analysing(message)

  # Identify the type of Cipher. Choosing "VZO" as the most repeated trigrams.
  analysis += identifyCipher.vigenere_or_otp_cipher(message,"VZO")
  textFile.write_file(analysis,"../nguyen_hw1/analysis/analysis3.txt")

  # Realized this is the One-Time Pad Cipher after analyzing.
  decipher_text = "One-Time Pad Cipher." 
  decipher_text += "\nThis cipher is nearly impossible to decrypted if we cannot know exactly the key."
  decipher_text += "\nKey: %s - This value is invalid." % (f"{key}")
  
  # Output to the file.
  textFile.write_file(decipher_text,plaintext)

  # Attemping Brute Force.
  bf_result = brute_force.brute_force(message)
  textFile.write_file(bf_result,"../nguyen_hw1/brute_force/brute_force3.txt")

'''
Steps by Steps to decipher cipher4.txt
'''
def cipher4(ciphertext,key,plaintext):
  # Input the file.
  message = textFile.read_file(ciphertext)
  
  # Analyzing the ciphertext.
  analysis = "***Analyzing Ciphertext #4***\n"
  analysis += crytanalysis.analysing(message)
  
  # Identify the type of Cipher. Choosing "DLV" as the most repeated trigrams.
  analysis += identifyCipher.vigenere_or_otp_cipher(message,"DLV")
  textFile.write_file(analysis,"../nguyen_hw1/analysis/analysis4.txt")


  # Choosing Vigenère Decipher method after analyzing.
  decipher_text = decipherMethod.vigenere_decrypt(message,key)

  # Output to the file.
  textFile.write_file(decipher_text,plaintext)

  # Attemping Brute Force.
  bf_result = brute_force.brute_force(message)
  textFile.write_file(bf_result,"../nguyen_hw1/brute_force/brute_force4.txt")
  