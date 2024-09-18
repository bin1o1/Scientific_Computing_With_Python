'''Program for vigenere cipher. Each letter of the message is shifted by the number of 
positions corresponding to the letter in the keyword. For example, if the keyword letter 
is 'B' (2nd letter of the alphabet), the message's letter is shifted by 1 position (A to B, D to E, etc.).'''



text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            #finding the key character, then increasing the index for the next iteration. 
            key_char = key[key_index % len(key)]
            key_index += 1
            
            offset = alphabet.index(key_char)       #finding number corresponding to the key character. (number to be added)
            index = alphabet.find(char)             #finding index of the selected character in the message.
            new_index = (index + offset*direction) % len(alphabet)      #self explanatory
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')