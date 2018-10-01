#from helpers import alphabet_position, rotate_character

#Part 1: Caesar
#alphabet_position
alphabet_position(letter)
#Note
#The function should be case-insensitive.
#---------
#Note
#You can assume that your input will definitely be a letter. 
#Don’t worry about what might happen if somebody tries to use your function with an input 
#parameter that is something other than a single letter, like alphabet_position("grandpa22

letter = letter.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
position = ''
if letter in alphabet:
    position = alphabet.index(letter)
    rotated_index = alphabet.index(letter)
#return position
#print(position)

#rotate_character
rotate_character(char, rot)
#Note
##### CAMILLA DO THIS  ##### use/create upper/lower flag so that it can be put back
#The upper or lower case of the letter should be preserved. For example, rotate_character("A", 13) results in "N", rather than "n"
#---------
#Note
#For non-alphabetical characters, you should ignore the rot argument and simply return char untouched. For example, see "!" and "6" in the table above.


#encrypt
encrypt(text, rot)
#Note
#The text argument might contain non-alphabetic characters (spaces, numbers, symbols). You should leave these as they are.	


#Make It Interactive
def main():
    # your main code (input and print statements)
    letter = input("Please input a letter")
    alphabet_position(letter)

if __name__ == "__main__":
    main()
