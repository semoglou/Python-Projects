# ROT13 Coding - str

def ROT13(S):
    encoded_string = ''
    for ch in S:
        letter_order = ord(ch)   #  ASCII number
        if 'A' <= ch.upper() <= 'M':
            encoded_string += chr(letter_order + 13)
        elif 'N' <= ch.upper() <= 'Z':
            encoded_string += chr(letter_order - 13)
        else:
            encoded_string += ch  
    return encoded_string


#  ROT13 Coding - File 

def file_encode():
    file_name = input('File Name: ')
    tmp_file = open(file_name)
    S = tmp_file.read()
    tmp_file.close()
    S = ROT13(S)
    encoded_text_name = input('Coded File Name: ')
    tmp_file = open(encoded_text_name,'w')  # Writing/Creating the file
    tmp_file.write(S)
    tmp_file.close()


file_encode()
