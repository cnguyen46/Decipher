# Class       : CSCE 477 - Fall2024
# Author      : Cong Nguyen
# Title       : Analyze Cipher program
# Date        : 09/04/2024
# Description : This program is used for analyzing cipher<n>.txt, 
#               before choosing the best decipher approaching. 

from typing import Counter
import helper
import identifyCipher

'''
# Function to perform frequency analysis.
# Output the frquency of repeating time of each letter.
# Return: Print out the frequency analysis.
'''
def frequency_analysis(dictOf_Char):
  # Sorting the value inside the dictionary following increasing order.
  # Credit for GeeksforGeeks.com: I learn this code from Geeksforgeeks to shorten the process of creating a map with sorted value.
  dictOf_Char = {key : value for key, value in sorted(dictOf_Char.items(), key = lambda element: element[1], reverse = True)}
  
  # Print out the report.
  total = helper.total_amount(dictOf_Char)
  result = "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
  result += "\nFREQUENCY ANALYSIS"
  result += "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
  result += "\n%-8s %-10s %s" % ("Letter", "Amount", "Frequency Rate (%)")
  result += "\n---------------------------------------"
  for key, value in dictOf_Char.items():
    result += "\n%-8s %-10s %s" % (key, f"{value}", f"{round(value/total * 100, 2)}")
  result += "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
  return result

'''
# Kisiski Test: To print out the top common triagrams, and diagrams.
# It should be at least 5 most common triagrams, and diagrams.
# The number of triagrams and diagrams is recommended having the same number for easier analysis.
'''
def kasiski_test(trigrams, digrams):
  # Preparing data for format printing.
  output_list = trigrams + digrams
  rows, cols = len(trigrams), 2
  table_2D = [[0]*cols for _ in range(rows)]
  element = 0
  for i in range(cols):
    for j in range(rows):
      if (element < len(output_list)):
        table_2D[j][i] = output_list[element]
        element += 1
  # Output the top most common triagram, and diagram.
  result = "\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
  result += "\nKasiski Test:"
  result += "\nTop 10 common of trigrams and digrams"
  result += "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
  for row in table_2D:
    if len(row) == 2 and isinstance(row[0], tuple) and isinstance(row[1], tuple):
      first_string, first_integer = row[0]
      second_string, second_integer = row[1]
      result += "\n%s: %-5s %s: %s" % (first_string, first_integer,
        second_string, second_integer)
    else:
      result += "\nUnexpected row format:", row
  result += "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
  return result

'''
# Function to calculation index of coincidence.
# Return the value of index of coincidence.
'''
def index_of_coincidence(ciphertext):
  total_Char = len(ciphertext)
  freqs = Counter(ciphertext)
  numerator = sum(freq * (freq - 1) for freq in freqs.values())
  denominator = total_Char * (total_Char - 1)
  if total_Char > 1:
    result = numerator / denominator
  else:
    result = 0
  return round(result, 4)


'''
# Function to print out all analyzation of ciphertext.
'''
def analysing(ciphertext):
  # Create a dictionary for analysis.
  dictOf_Char = helper.freq_amount_Char(ciphertext)
  
  # Create a string to contain all crytanalysis.
  analysis = ""

  # Testing hypothesis.
  analysis += helper.hypothesis(ciphertext, dictOf_Char)
  
  # Frequency analysis.
  analysis += frequency_analysis(dictOf_Char)
  analysis += helper.mostRepeated_Char(dictOf_Char)
  analysis += helper.leastRepeated_Char(dictOf_Char)
  analysis += helper.initial_letter(ciphertext,dictOf_Char)
  analysis += helper.final_letter(ciphertext,dictOf_Char)

  # Kasiski test.
  trigrams = helper.most_trigrams(ciphertext,10)
  digrams = helper.most_digrams(ciphertext,10)
  analysis += kasiski_test(trigrams,digrams)

  # Using Index of Coincidence to determine monoalphabet or polyalphabet. 
  indexCoin = index_of_coincidence(ciphertext)
  analysis += identifyCipher.mono_or_poly_alphabet(indexCoin)

  return analysis



    

  


                

  


