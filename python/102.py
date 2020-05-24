#!/usr/bin/env python3

import sys  # import sys library, its system functions and parameters
from datetime import datetime as dt # importing date time and aliasing it as dt
print(sys.version)
print(dt.now())

# Advanced strings
my_name = "Heath"
print(my_name[0]) # the firsr letter
print(my_name[-1]) # the last letter

sentence = "This is indeed a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) # o/p: This is a sentence

quote = "He said, \"Give me all your money\"" #character escaping so that we can use double quotes inside the double quoutes
print(quote)

too_much_space = "          hello"
print(too_much_space.strip()) #o/p: hello #Strips the spaces

print ("A" in "Apple") # o/p: True
print ("a" in "Apple") # o/p: False

#logic to find if a letter is there in a word or not, case-sensitivity does not matter
letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) 

movie = "The Hangover"
print("My favorite movie is {}".format(movie)) # '{}' is the placeholder for 'movie' 
 
print('\n')
# Dictionaries
drinks = {"White Russian":7, "Old Fashion":18, "Lemon Drop":8} #drink is key, price is value
print(drinks)

employees = {"Finance":["Bob", "Linda", "Tina"], "IT":["Gorge", "Louis", "Teddy"], "HR":["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ['Mr. Frond'] # add key value pair
print(employees)

employees.update({"Sales":["Andie", "Ollie"]}) # add new key value pair
print(employees)

print(drinks.get("White Russian"))
