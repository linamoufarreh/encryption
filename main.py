def encrypt(text, key):
    encrypted=""
    letter=""
    for i in range(0, len(text)):
        if text[i]==" ":
            letter=" "
        else:
            letter= chr(ord(text[i])+ key)
        
        encrypted= encrypted + letter
        
    return encrypted

def decrypt(message, key):
    decrypted=""
    code=""
    for i in range(0, len(message)):
        if message[i]==" ":
            code =" "
        else:
            code= chr(ord(message[i])- key)
        decrypted= decrypted + code
    
    return decrypted


def hack(secret, lexicon):
    for k in range(1,25):
        D= decrypt(secret, k)
        while True:
    if D in " ".join(lexicon):
        return D
    else:
        return ""
        break

english_words = ["A", "THE", "APPLE", "SECRET", "HELLO", "WORLD", "MESSAGE"]
print(hack("D VHFUHW PHVVDJH",english_words))
