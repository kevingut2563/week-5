# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
print(magic[5])
# a. Retrieve the 5th character.
print(magic[-2])
# b. Retrieve the second to last character.
print(magic.find("c"))
# c. Find the first occurrence of the letter 'c'.

# Advanced Slicing:
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(alphabet.find("hji"))
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[7:10])
# c. Reverse the entire string using slicing.
print(alphabet[0:14:2])
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
kennedy="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print=(kennedy.find("J"))


# Manipulating Words:
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
words = info.split()
# b. Extract every third word.
everythirdword= words[::3]
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
result= ''.join(everythirdword)
print(result)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
force="MAY THE FORCE BE WITH YOU."
print(force.lower())

# String Joining and Splitting:
# Given the list motto 
wordlist = ["Make", "haste", "slowly."]
joinlist = " ".join(wordlist)
print(joinlist)
newjoinlist= "a".join(wordlist)
print(newjoinlist)
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
life = "Life is what happens when you are busy making other plans."
print(life.replace("busy", "distracted").replace("plans", "mistakes"))
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition: 
repetition = "Iteration" * 7
print(repetition)
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote= "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(quote.find("moonlight"))
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
random="Supercalifragilisticexpialidocious"
print(random.find("Supercalifragilisticexpialidocious"))
# b. Count the number of times the letter 'i' appears in the same word/phrase.