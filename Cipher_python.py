alphabet = "abcdefghijklmnopqrstuvwxyz"
#decision = raw_input("Decrypt(0) or Encrypt(1)")
message = raw_input("Enter message ")
message_reformat = ""

for letter in message:
    if letter == " ":
        continue
    else:
        message_reformat += letter

print message
print message_reformat

dictonary_alphabet = {}
dictonary_alphabet_source = {}
dictonary_encrypted_alphabet = {}

#key,val
count = 1
for letter in alphabet:
    dictonary_alphabet[letter] = count
    dictonary_alphabet_source[count] = letter
    count += 1

def encrypt_alphabet(shift):
    for letter in alphabet:
        val = dictonary_alphabet.get(letter, '')
        if val + shift > 26:
            val = ( val + shift - 26 )
            dictonary_encrypted_alphabet[val] = letter
        else:
            dictonary_encrypted_alphabet[val+shift] = letter


def encrypt(str, shift):
    encrypted_key_values = []
    encrypted_message = ""

    for letter in str:
        index = dictonary_alphabet.get(letter)
        new_index = 0
        print 'letter: ' + letter
        if index + shift > 26:
            new_index += ( ( index + shift ) - 26 ) 
        else:
            new_index += (index + shift)
        
        encrypted_message += dictonary_alphabet_source.get(new_index)
        print encrypted_message

    print "final " + encrypted_message                      



encrypt(message_reformat, 1)

