
import mylogo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(mylogo.logo)

# get user information

direction = input("Type encode to encrypt and decode to decrypt: ").lower()
shift = int(input("Enter the number of shifts: "))
word = input("Enter your word: ").lower()

#function to encrypt or decrypt

def enc_word(shift_no, user_word):
    new_word = ""
    new_letter = ""
    for letter in user_word:
        position = alphabet.index(letter)
        new_position = position + shift_no
        new_letter += alphabet[new_position]
        new_word += new_letter
    print(f"Your word is {new_word}")

def dec_word(shift_no, user_word):
    new_word = ""
    new_letter = ""
    for letter in user_word:
        position = alphabet.index(letter)
        new_position = position - shift_no
        new_letter += alphabet[new_position]
        new_word += new_letter
    print(f"Your word is {new_word}")

if direction == "decode":
    dec_word(shift_no=shift, user_word=word)
else:
    enc_word(shift_no=shift, user_word=word)