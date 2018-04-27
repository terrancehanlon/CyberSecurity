alphabet = "abcdefghijklmnopqrstuvwxyz"
#decision = raw_input("Decrypt(0) or Encrypt(1)")
message = raw_input("Enter message ")


dictonary_alphabet = {}
dictonary_encrypted_alphabet = {}

#key,val
count = 1
for letter in alphabet:
    dictonary_alphabet[letter] = count
    count += 1

def encrypt_alphabet(shift):
    for letter in alphabet:
        key = dictonary_alphabet.get(letter, default= None)
        if key + shift > 26:
            key = ( old_key + shift - 26)
        else:
            dictonary_encrypted_alphabet[letter] = key + shift


def encrypt(message, shift):
    #print(dictonary_alphabet)




encrypt("test", 0)

