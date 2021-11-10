# Caesar cipher
def cipher(text, shift, encrypt=True):
    
    '''
    This function implements Caesar cipher.

    Inputs:
    text: text to be encrypted
    shift: parameter of Caesar cipher algorithm to shift characters.
    if negative, it will decrypt the message
    encrypt: a boolean vaiable to decrypt or encrypt

    Outputs:
    encrypted or decrypted text

    Use case:

    cipher('hello',3,encrypt=True) ---> 'khoor'
    cipher('khoor',3,encrypt=False) ---> 'hello' 

    '''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    
    for c in text:
        index = alphabet.find(c)
        
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    
    return new_text


