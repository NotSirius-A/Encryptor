def Encrypt(text, key_1, key_2, key_3, iterations): #TODO
    return "e"

def Decrypt(text, key_1, key_2, key_3, iterations): #TODO
    return "d"

def check_password(text): #TODO
    if text == '123':
        return 1
    elif text == 'admin':
        return 2
    else:
        return 0


def is_valid_key(key): #TODO
    return True 


#TODO add exit condition

print("------------------------------------")

password = input("Enter password: ")

permission = check_password(password)

while True:
    key_input = input("First Key: ")

    if is_valid_key(key_input):
        key_1 = key_input
        break

while True:
    key_input = input("Second Key: ")

    if is_valid_key(key_input):
        key_2 = key_input
        break

while True:
    key_input = input("Third Key: ")

    if is_valid_key(key_input):
        key_3 = key_input
        break


while True:

#TODO make this other way round, so first ask for message then option


    option = input("Encrypt or Decrypt ? Enter [e/d]: ").lower()
    
    if option == 'e':
        message = input("Enter a message to encrypt: ")

        #encryption happens here
        message = Encrypt(message, key_1, key_2, key_3, 1)


        print(f"Encrypted message: \"{message}\"")
        print("------------------------------------\n")

    elif option == 'd':
        message = input("Enter a message to decrypt: ")

        #decryption happens here
        message = Decrypt(message, key_1, key_2, key_3, 1)


        print(f"Decrypted message: \"{message}\"")
        print("------------------------------------\n")

    else:
        print("Please enter 'e' or 'd': ")
    
