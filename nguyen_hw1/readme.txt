*** THESE ARE THE SUMMARIES OF STEPS BY STEPS OF HOW I DECRYPT CIPHERTEXT ***
__________________________________________________________________________________________

### 1. Testing hypothesis:
# Hypothesis : All letters in 4 cipher files are 26 alphabet capital letters. 
#
# Testing    : Check if the sum number of each character is equal with total number 
#              of letters in each 4 files.
#            - If it's true, then the hypothesis is true
#            - Else, deny hypothesis.
#
# Discover   : For this assignment, after running the test for all four files, 
#            the output shows that
#            there are only capital charaters inside the message, which means we only need 
#            to count 26 alphabet letters => Hypothesis is true.
#
# Approach   : We can use the function ord(), ranging from 65 to 90, repeatively A to Z
#            to perform frequency analysis, Kasiski Test, 
#            and calculate Index of Coincidence in the files.

### 2. Attempt using Brute Force:
* In this assignment, students should avoid using brute force for deciphering.
Instead, they should use frequency analysis, Kasiski Test, and Index of Coincidence
to decide which deciphered method working best to solve the ciphertext.

* The brute force is merely my curiosity.
It is recommended to use crytanalysis to solve the problems, which will shows later.

* Steps by step:
- Shift each character by n value, where 0 < n < 26, n is an integer.
- Need looping 25 times due to having 26 alphabet letters.
- After that, we look for the content that makes sense. Only need to look at the first 50 letters.
Founding:
  + cipher1.txt: Shift 10 times
  + cipher2.txt: Shift 24 times
  + cipher3.txt: No content makes sense
  + cipher4.txt: No content makes sense
=> Need a new strategy for cipher3 and cipher4
=> Recommend using frequency analysis, Kasiski Test, and Index of Coincidence.


### 3. Using crytanalysis to solve the problems:
***Note: 
- Reading the analysis from txt file in "../analysis/"
- The full plaintext is outputed at the directory "../nguyen_hw1/plaintext/""

* Cipher #1: 
Using Shift decipher - Key: 10
Using Affine decipher - Key: [1,16]

* Cipher #2: 
Using Shift decipher - Key: 24
Using Affine decipher - Key: [1,2]

* Cipher #3: This is One-Time Pads cipher.
Key: Impossible to find the key.

* Cipher #4: Using Vigenère decipher
Key: HUSKERS
__________________________________________________________________________________________

***Hint:
-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
IC = 0.065 -> Mono alphabet
IC = 0.038 -> Polyalphabet

Mono alphabet -> Find the shift -> Shift (Yes) or Substitution(No)
Poly alphabet -> IC with substring -> Vigenère (Yes) or One time Pads(No)
-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Using GCD to Define the Cipher (Mono alphabet):
If a = 1 and GCD(a, 26) = 1: The cipher is an Shift Cipher, or Affine Cipher.
If a ≠ 1 and GCD(a, 26) = 1: The cipher is an Affine Cipher.
If a ≠ 1 and GCD(a, 26) ≠ 1: The cipher is not Shift or Affine Cipher.

E(x) = (ax + b) mod m

Where:
- E(x) is the encrypted letter.
- x is the numerical position of the plaintext letter (e.g., A = 0, B = 1, ..., Z = 25).
- a and b are keys that define the cipher (with a and m being coprime).
- m is the size of the alphabet (usually 26 for English letters).

_________________________________________________________________________________

*** Polyalphabetic Ciphertext: Assume a ciphertext with a known key length of 4.

IC = total of (f_i *(f_i - 1)) / N (N - 1) 

Where: 
- f_i is the frequency of each letter (a to z) in amount,
- N is the total amount of letters in the group.

1/ Segments: Divide into groups:

Group 1: Characters at positions 0, 4, 8, ...
Group 2: Characters at positions 1, 5, 9, ...
Group 3: Characters at positions 2, 6, 10, ...
Group 4: Characters at positions 3, 7, 11, ...

2/ Frequency Counts: Count the occurrences of each letter in each group.

3/ Calculate IC: Use the formula for each group.
IC = total of (p_i * f_(i+g)) / n 

Where: 
- p_i is the probability of each letter (a to z) in alphabet text,
- f_(i+g) is the frequency of the letter in alphabet shifted by g (0 <= g <= 25, g is the integer)
- n is the total amount of letters in each group.

4/ Average IC: Combine the IC values from all groups to find the average.
