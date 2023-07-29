# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:40:11 2023

@author: Retired Dragon
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  unique_letters = []
  for letter in letters:
    if letter in word:
      unique_letters.append(letter)
  return len(unique_letters)
print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))