#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Using substring search methods for strings
# ------------------------------------------

GREETING: str = "Hello my friend! How are you doing this morning, my friend?"
SUB: str = "friend"
header: str = f"GREETING = \"{GREETING}\"; SUB = \"{SUB}\"\n"
header += f"{'-' * (len(header) - 1)}"
print(f"{header}")

print(f"\"{SUB}\" in GREETING: {SUB in GREETING}")
print(f"GREETING.count(SUB): {GREETING.count(SUB)}")
print(f"GREETING.find(SUB): {GREETING.find(SUB)}")
print(f"GREETING.index(SUB): {GREETING.index(SUB)}")
print(f"GREETING.rfind(SUB): {GREETING.rfind(SUB)}")
print(f"GREETING.rindex(SUB): {GREETING.rindex(SUB)}")


# In[2]:


# Constructing related strings
# ----------------------------

ST: str = "   a brand new day   "
header = f"ST = {ST}\n"
header += f"{'-' * (len(header) - 1)}"
print(f"{header}")

print(f"ST.replace(\"day\", \"night\"): {ST.replace('day', 'night')}")
print(f"ST.capitalize(): {ST.capitalize()}")
print(f"ST.title(): {ST.title()}")
print(f"ST.upper(): {ST.upper()}")
print(f"ST.lower(): {ST.lower()}")
print(f"ST.center(50, '-'): {ST.center(50, '-')}")
print(f"ST.ljust(50, '-'): {ST.ljust(50, '-')}")
print(f"ST.rjust(50, '-'): {ST.rjust(50, '-')}")
print(f"ST.zfill(50): {ST.zfill(50)}")
print(f"ST.strip(): {ST.strip()}")
print(f"ST.lstrip(): {ST.lstrip()}")
print(f"ST.rstrip(): {ST.rstrip()}")


# In[3]:


# Testing boolean conditions
# --------------------------

passage: str = "and thus, it has been so since then..."
header = f"passage = {passage}\n"
header += f"{'-' * (len(header) - 1)}"
print(f"{header}")

print(f"passage.startswith('And'): {passage.startswith('And')}")
print(f"passage.endswith('.'): {passage.endswith('.')}")
print(f"passage.isspace(): {passage.isspace()}")
print(f"passage.isalpha(): {passage.isalpha()}")
print(f"passage.islower(): {passage.islower()}")
print(f"passage.isupper(): {passage.isupper()}")
print()

passage = passage.replace(".", "").replace(",", "")
header = f"passage = {passage}\n"
header += f"{'-' * (len(header) - 1)}"
print(f"{header}")

print(f"passage.isdigit(): {passage.isdigit()}")
print(f"passage.isdecimal(): {passage.isdecimal()}")
print(f"passage.isnumeric(): {passage.isnumeric()}")
print(f"passage.isalnum(): {passage.isalnum()}")


# In[4]:


# Splitting and joining strings
# -----------------------------

from keyword import kwlist
from typing import Tuple

print(f"', '.join(kwlist):\n{', '.join(kwlist)}")
print()

PARAGRAPH: str = "Good morning!\nToday, we will discuss about the weather.\nThank you!"
print(f"PARAGRAPH.splitlines():\n{PARAGRAPH.splitlines()}")
print()
print(f"PARAGRAPH.split():\n{PARAGRAPH.split()}")
print()
print(f"PARAGRAPH.rsplit():\n{PARAGRAPH.rsplit()}")
print()

parts: Tuple[str, str, str] = PARAGRAPH.partition("\n")
print(f"PARAGRAPH.partition('\\n'):\n{parts}")
print()

parts = PARAGRAPH.rpartition("\n")
print(f"PARAGRAPH.rpartition('\\n'):\n{parts}")


# In[5]:


# String Formatting: Center the string (^) and pad with -
# -------------------------------------------------------

VAL: str = "hello"

print("{:*>20}".format(VAL))
print(f"{VAL:-^20}")


# In[6]:


# String Formatting: Pad numbers with 0
# -------------------------------------

YEAR: int = 2023
MONTH: int = 3
DAY: int = 15

print(f"{YEAR}/{MONTH:02}/{DAY:02}")


# In[7]:


# String Formatting: Converting integers to bin, octal, or hex
# ------------------------------------------------------------

MY_INT: int = 1965

print(f"MY_INT: {MY_INT}")
print(f"MY_INT in binary: {MY_INT:b}")
print(f"MY_INT in octal: {MY_INT:o}")
print(f"MY_INT in hexadecimal: {MY_INT:x}")


# In[8]:


# String Formatting: Formatting Floating-Points
# ---------------------------------------------

MY_FLOAT: float = 3.1415

print(f"MY_FLOAT: {MY_FLOAT:.3f}")
print(f"MY_FLOAT in scientific notation: {MY_FLOAT:.3e}")

