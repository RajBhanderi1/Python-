import random
import string

temp_keys = string.punctuation + string.ascii_letters + string.digits
temp_keys = list(temp_keys)

temp_values = temp_keys.copy()
random.shuffle(temp_values)

cipher = dict(zip(temp_keys,temp_values))
rev_cipher = dict(zip(temp_values,temp_keys))

#Message Encryption

def main():

    message = input("Enter your message to encrypt: ")
    encrypt_msg = ""
    print(f"Your message is : {message}")
    print()
    
    for x in message:
        encrypt_msg += cipher.get(x) 


    print(f"Your Encrypted message is : \"{encrypt_msg}\"")
    
    decrypted_msg = ""
    
    for y in encrypt_msg :
        decrypted_msg += rev_cipher.get(y)


    print()
    print(f"Your Decrypted message is : \"{decrypted_msg}\"")
    

if __name__ == '__main__':
    main()