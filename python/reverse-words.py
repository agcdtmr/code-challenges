# INSTRUCTIONS

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# SOLUTION

def reverse_words(text):
    words = text.split(" ")
    new_words = [word[::-1] for word in words]
    new_sentence = " ".join(new_words)
    return new_sentence

# RESOURCES

# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
