def Encrypt(text, key_1, key_2, key_3, alphabet): 

    i = 0
    result = ''

    for char in text:
        position = alphabet.index(char)

        change = ((key_1+1337)**19 + (key_3+i*33)**13 + (key_3+333)**15 + (key_2+17+i)**17) + i
        position = (position + change) % (len(alphabet)-1)

        result = result + alphabet[position]

        key_1 = key_1 + key_3 + 11
        key_2 = (key_2*5) + key_1 + (key_3*3) + 311
        key_3 = key_3 * (3**i)
        i = i + 1



    return result




    

def Decrypt(text, key_1, key_2, key_3, alphabet): 

    i = 0
    result = ''

    for char in text:
        position = alphabet.index(char)
        
        change = ((key_1+1337)**19 + (key_3+i*33)**13 + (key_3+333)**15 + (key_2+17+i)**17) + i
        position = (position - change) % (len(alphabet)-1)
        
        result = result + alphabet[position]

        key_1 = key_1 + key_3 + 11
        key_2 = (key_2*5) + key_1 + (key_3*3) + 311
        key_3 = key_3 * (3**i)
        i = i + 1


    return result

def pass_through_cipher(choice, text, key_1, key_2, key_3, iterations):
    alphabet = ['=','x','~','$','+','l','m','B','o','p','"','w',',','y','.','/','0','d','2','9',':',';','@','A','b','I','J','K','<',' ',')','*',
                'k','O','P','n','C','3','4','5','6','7','8','h','i','j','t',']','^','_','`','a','H','#','!','-','z','D','E','Q','R','X','Y','Z',
                '[','(','F','G','f','g','U','|','N','1','e','S','T','{','V','W','u','v','>','?','L','M','c','&','\'','\\','}','q','r','s','%']


    if choice == 'e':
        text = Encrypt(text=text, key_1=key_1, key_2=key_2, key_3=key_3, alphabet=alphabet)
    elif choice == 'd':
        text = Decrypt(text=text, key_1=key_1, key_2=key_2, key_3=key_3, alphabet=alphabet)
        
    return text

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

#password = input("Enter password: ")

#permission = check_password(password)

while True:
    key_input = int(input("First Key:  "))

    if is_valid_key(key_input):
        key_1 = key_input
        break

while True:
    key_input = int(input("Second Key: "))

    if is_valid_key(key_input):
        key_2 = key_input
        break

while True:
    key_input = int(input("Third Key:  "))

    if is_valid_key(key_input):
        key_3 = key_input
        break


print("-------------------------")
print('Enter "exit" to quit.')

while True:

#TODO make this other way round, so first ask for message then option


    option = input("Encrypt or Decrypt ? Enter [e/d]: ").lower()
    
    if option == 'e':
        message = input("Enter a message to encrypt: ")

        #encryption happens here
        message = pass_through_cipher(option, message, key_1, key_2, key_3, 1)


        print(f"Encrypted message: \"{message}\"")
        print("------------------------------------\n")

    elif option == 'd':
        message = input("Enter a message to decrypt: ")

        #decryption happens here
        message = pass_through_cipher(option, message, key_1, key_2, key_3, 1)


        print(f"Decrypted message: \"{message}\"")
        print("------------------------------------\n")

    elif option == "exit":
        exit()

    else:
        print("Please enter 'e' or 'd': ")
    
