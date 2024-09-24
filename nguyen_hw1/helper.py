# Class  : CSCE 477 - Fall2024
# Author : Cong Nguyen
# Title  : Helper program
# Date   : 09/04/2024
# Description : This program contain many helper methods 
# supporting for analyzing and deciphering the message.

from math import gcd
from typing import Counter
import crytanalysis

# Index of Coincidence
IC_ENGLISH = 0.065 # IC for Monoalphabetic (English)
IC_RANDOM = 0.038 # IC for Polyalphabetic (Random)

'''
# Function to create a dictionary of all alphabet letters from the ciphertext.
# Return: The dictionary of all letters {key = character : value = repeated times of character}
'''
def freq_amount_Char(ciphertext):
  # Initialize an dictionary having keys of 26 upper-case alphabet letters, with empty value.
  dictOf_Char = {}
  for character in range(ord('A'),ord('Z') + 1):
    dictOf_Char[chr(character)] = 0

  # Updating the repeating time of the dictionary.
  letter = 0
  while (letter < len(ciphertext)):
    match ciphertext[letter]:
      case "A":
        dictOf_Char[chr(ord('A'))] += 1
      case "B":
        dictOf_Char[chr(ord('B'))] += 1
      case "C":
        dictOf_Char[chr(ord('C'))] += 1
      case "D":
        dictOf_Char[chr(ord('D'))] += 1
      case "E":
        dictOf_Char[chr(ord('E'))] += 1
      case "F":
        dictOf_Char[chr(ord('F'))] += 1
      case "G":
        dictOf_Char[chr(ord('G'))] += 1
      case "H":
        dictOf_Char[chr(ord('H'))] += 1
      case "I":
        dictOf_Char[chr(ord('I'))] += 1
      case "J":
        dictOf_Char[chr(ord('J'))] += 1
      case "K":
        dictOf_Char[chr(ord('K'))] += 1
      case "L":
        dictOf_Char[chr(ord('L'))] += 1
      case "M":
        dictOf_Char[chr(ord('M'))] += 1
      case "N":
        dictOf_Char[chr(ord('N'))] += 1
      case "O":
        dictOf_Char[chr(ord('O'))] += 1
      case "P":
        dictOf_Char[chr(ord('P'))] += 1
      case "Q":
        dictOf_Char[chr(ord('Q'))] += 1
      case "R":
        dictOf_Char[chr(ord('R'))] += 1
      case "S":
        dictOf_Char[chr(ord('S'))] += 1
      case "T":
        dictOf_Char[chr(ord('T'))] += 1
      case "U":
        dictOf_Char[chr(ord('U'))] += 1
      case "V":
        dictOf_Char[chr(ord('V'))] += 1
      case "W":
        dictOf_Char[chr(ord('W'))] += 1
      case "X":
        dictOf_Char[chr(ord('X'))] += 1
      case "Y":
        dictOf_Char[chr(ord('Y'))] += 1
      case "Z":
        dictOf_Char[chr(ord('Z'))] += 1
    letter += 1

  return dictOf_Char

'''
# Function to test hypothesis.
# Return: Print out the conclusion.
'''
def hypothesis(ciphertext, dictOf_Char):
  result = "\nTotal number of letters in ciphertext: " + str(len(ciphertext))
  result += "\nTotal number of 26 alphabet letters  : " + str(total_amount(dictOf_Char))
  if (total_amount(dictOf_Char) == len(ciphertext)):
    result += "\nHypothesis is true that ciphertext only containts 26 uppercased alphabet letters."
    result += "\n^_^ Total sum of each letter is equal with total number of character in the file.\n"
    
  else:
    result += "\nHypothesis is false."
    result += "\nT_T Total sum of each letter is not equal with total number of character in the file.\n"
  return result

'''
# Function to find the total number of letter in ciphertext.
# Return: The total number of letter in ciphertext.
'''
def total_amount(dictOf_Char):
  total = 0
  for value in dictOf_Char.values():
    total += value
  return total

'''
# Function to find all frequency rate of each letter in ciphertext.
# Return: A map of frequency rate of each letter in ciphertext.
'''
def freq_probability_Char(dictOf_Char):
  dictOf_Freq = {}
  total = total_amount(dictOf_Char)
  for key, value in dictOf_Char.items():
    dictOf_Freq[key] = round(value/total * 100, 2)
  return dictOf_Freq

'''
# Function to find the most repeated character.
# Return: Print out the most repeated character.
'''
def mostRepeated_Char(dictOf_Char):
  maxValue = 0
  which_Max = ''
  for key, value in dictOf_Char.items():
    if (maxValue <= value):
      maxValue = value
      which_Max = key
    else:
      continue
  frequency = round(maxValue/total_amount(dictOf_Char) * 100, 2)
  return "\nLetter {} repeats the most: {} times, with {}%".format(which_Max, maxValue,frequency)

'''
# Function to find the least repeated character.
# Return: Print out the least repeated character.
'''
def leastRepeated_Char(dictOf_Char):
  minValue = dictOf_Char[chr(ord('A'))]
  which_Min = ''
  for key, value in dictOf_Char.items():
    if (minValue >= value):
      minValue = value
      which_Min = key
    else:
      continue
  frequency = round(minValue/total_amount(dictOf_Char) * 100, 2)
  return "\nLetter {} repeats the least: {} times, with {}%".format(which_Min, minValue, frequency)

# Function to return the value and frequency of initial letter.
def initial_letter(ciphertext, dictOf_Char):
  first = ciphertext[0]
  for key, value in dictOf_Char.items():
    if first == key:
      return "\nInitial letter is {} repeats {} times, with {}%".format(key, value, round(value/total_amount(dictOf_Char) * 100, 2))
    
# Function to return the value and frequency of final letter.
def final_letter(ciphertext, dictOf_Char):
  last = ciphertext[-1]
  for key, value in dictOf_Char.items():
    if last == key:
      return "\nFinal letter is {} repeats {} times, with {}%".format(key, value, round(value/total_amount(dictOf_Char) * 100, 2))

'''
# Function to find the most trigrams in the ciphertext.
# Return: The most trigrams, with their number of repeated times.
'''
def most_trigrams(ciphertext, top_value):
  trigrams = [ciphertext[i:i+3] for i in range(len(ciphertext) - 2)]
  count = Counter(trigrams)
  result = count.most_common(top_value)
  return result

'''
# Function to find the most digrams in the ciphertext.
# Return: The most triagrams, with their number of repeated times.
'''
def most_digrams(ciphertext, top_value):
  digrams = [ciphertext[i:i+2] for i in range(len(ciphertext) - 1)]
  count = Counter(digrams)
  result = count.most_common(top_value)
  return result

'''
# Function to find all position of one trigrams in the ciphertext.
'''
def find_trigram_positions(ciphertext, trigram):
  positions = []
  trigram_length = len(trigram)
  for i in range(len(ciphertext) - trigram_length + 1):
    if ciphertext[i:i + trigram_length] == trigram:
      positions.append(i)
  return positions

'''
# Function to find keyword's length using Kasiski Test.
'''
def find_key_length_kasiski_method(all_position_of_one_trigram):
  group_of_gcd = []
  for i in range(len(all_position_of_one_trigram)-2):
    group_of_gcd.append(gcd(all_position_of_one_trigram[i+1] - all_position_of_one_trigram[i],
                      all_position_of_one_trigram[i+2] - all_position_of_one_trigram[i+1]))
  key_length = Counter(group_of_gcd).most_common(1)[0][0]
  return Counter(group_of_gcd), key_length

# Function to split the ciphertext into n groups based on assumed keyword length
def split_by_keyword_length(ciphertext, length):
    return [''.join([ciphertext[i] for i in range(j, len(ciphertext), length)]) for j in range(length)]

# Function to calculate the average IC for a given keyword length
def average_ic_for_keyword_length(ciphertext, length):
    groups = split_by_keyword_length(ciphertext, length)
    ics = [crytanalysis.index_of_coincidence(group) for group in groups]
    return sum(ics) / len(ics) if ics else 0

'''
# Function to find keyword's length using Index of Coincidence method.
'''
def find_key_length_ic_method(ciphertext, max_key_len):
  average_ics = {}
  for length in range(1, max_key_len + 1):
    avg_ic = average_ic_for_keyword_length(ciphertext, length)
    average_ics[length] = avg_ic
  return average_ics

'''
# Function to find keyword using Index of Coincidence method.
'''
def table_of_IC(ciphertext, max_key_length):
  EXPECTED_FREQ_ENGLISH = {
    'A': 0.0820, 'B': 0.0150, 'C': 0.0280, 'D': 0.0430, 'E': 0.1270,
    'F': 0.0220, 'G': 0.0200, 'H': 0.0610, 'I': 0.0700, 'J': 0.0015,
    'K': 0.0077, 'L': 0.0400, 'M': 0.0240, 'N': 0.0670, 'O': 0.0750,
    'P': 0.0190, 'Q': 0.0010, 'R': 0.0600, 'S': 0.0630, 'T': 0.0910,
    'U': 0.0280, 'V': 0.0098, 'W': 0.0240, 'X': 0.0015, 'Y': 0.0200,
    'Z': 0.0007
  }
  result = ""
  keyword = []
  
  # Split the ciphertext into the block.
  # Max number of block = max_key_length
  block = ['' for _ in range(max_key_length)]
  length = 0
  while length < max_key_length:
    character = 0
    while character < len(ciphertext):
      if ((character <= max_key_length - 1)):
        block[length] = ciphertext[character + length]
        character = character + length + max_key_length   
      else: 
        block[length] += ciphertext[character]
        character += max_key_length
    length += 1
  
  # Calculate all IC in each block.
  for each_block in range(len(block)):
    result += "\nBlock %s: " % (f"{each_block + 1}")
    total_amount = len(block[each_block])
    shift = 0
    while shift < 26:
      frequency = freq_amount_Char(block[each_block])
      value_of_each_shift = 0
      for letter in frequency.keys():
        value_of_each_shift += (EXPECTED_FREQ_ENGLISH[letter] * frequency[chr(((ord(letter) + shift - ord("A")) % 26) + ord("A"))] / total_amount)
      result += "[%s - %s : %s] %2s" % (numTolet(shift), f"{shift}", f"{round(value_of_each_shift, 4):.4f}","")
      if value_of_each_shift > (IC_ENGLISH + IC_RANDOM) / 2:
        keyword.append(numTolet(shift))
      shift += 1
  
  # Output the key.      
  result += "\nKeyword: %s" % (f"{keyword}")
  return result

# Helper function to solve system equation
def modular_inverse(a, modular):
  initial_modular, x0, x1 = modular, 0, 1
  if modular == 1:
      return 0
  while a > 1:
      quotient = a // modular
      modular, a = a % modular, modular
      x0, x1 = x1 - quotient * x0, x0
  if x1 < 0:
      x1 += initial_modular
  return x1

# Inverve the modular. Helper function for Affine Cipher.
def modInverse(a):
  for x in range(1, 26):
    if (((a % 26) * (x % 26)) % 26 == 1):
      return x
  return -1

# Assign number to letter for deciphering.
def numTolet(number):
  letter = ""
  match number:
    case 0:
      letter = "A"
    case 1:
      letter = "B"
    case 2:
      letter = "C"
    case 3:
      letter = "D"
    case 4:
      letter = "E"
    case 5:
      letter = "F"
    case 6:
      letter = "G"
    case 7:
      letter = "H"
    case 8:
      letter = "I"
    case 9:
      letter = "J"
    case 10:
      letter = "K"
    case 11:
      letter = "L"
    case 12:
      letter = "M"
    case 13:
      letter = "N"
    case 14:
      letter = "O"
    case 15:
      letter = "P"
    case 16:
      letter = "Q"
    case 17:
      letter = "R"
    case 18:
      letter = "S"
    case 19:
      letter = "T"
    case 20:
      letter = "U"
    case 21:
      letter = "V"
    case 22:
      letter = "W"
    case 23:
      letter = "X"
    case 24:
      letter = "Y"
    case 25:
      letter = "Z"     
  return letter

# Assign letter to number for deciphering.
def letTonum(letter):
  number = 0
  match letter:
    case "A":
      number = 0
    case "B":
      number = 1
    case "C":
      number = 2
    case "D":
      number = 3
    case "E":
      number = 4
    case "F":
      number = 5
    case "G":
      number = 6
    case "H":
      number = 7
    case "I":
      number = 8
    case "J":
      number = 9
    case "K":
      number = 10
    case "L":
      number = 11
    case "M":
      number = 12
    case "N":
      number = 13
    case "O":
      number = 14
    case "P":
      number = 15
    case "Q":
      number = 16
    case "R":
      number = 17
    case "S":
      number = 18
    case "T":
      number = 19
    case "U":
      number = 20
    case "V":
      number = 21
    case "W":
      number = 22
    case "X":
      number = 23
    case "Y":
      number = 24
    case "Z":
      number = 25     
  return number