def apply_cipher(choice, text, key_1, key_2, key_3, iterations):
    alphabet = ['=','x','~','$','+','l','m','B','o','p','"','w',',','y','.','/','0','d','2','9',':',';','@','A','b','I','J','K','<',' ',')','*',
                'k','O','P','n','C','3','4','5','6','7','8','h','i','j','t',']','^','_','`','a','H','#','!','-','z','D','E','Q','R','X','Y','Z',
                '[','(','F','G','f','g','U','|','N','1','e','S','T','{','V','W','u','v','>','?','L','M','c','&','\'','\\','}','q','r','s','%']


    
    for index in range(0, iterations):
        i = 0
        result = ''
        for char in text:
            if alphabet.count(char) == 0:
                print(f"Message contains an illegal character '{char}'")
                break
            position = alphabet.index(char)
        
            change = ((key_1+1337)**10 + (key_3+i*33)**11 + (key_3+333)**7 + (key_2+17+i)**11) + i
           
            if choice == 'e':
                position = (position + change) % (len(alphabet)-1)
            elif choice == 'd':
                position = (position - change) % (len(alphabet)-1)
            else: 
                return False

            result = result + alphabet[position]

            key_1 = key_1 + key_3 + 11
            key_2 = (key_2*5) + key_1 + (key_3*3) + 311
            key_3 = key_3 * (3**i) + 2
            i = i + 1

        text = result

        
    return text


def get_key(index):

    while True:

        if index == 0:
            key = input("First Key:  ")
        elif index == 1:
            key = input("Second Key: ")
        elif index == 2:
            key = input("Third Key:  ")
        else: 
            return False

        if is_valid_key(key):
            return int(key)
        

def is_valid_key(key): #TODO

    if key == '':
        print("Key cannot be empty")
        return False
    elif len(key) > 8:
        print("Key too long")
        return False 
    else:
        return True


print("************************************")
print("license")
print("************************************")

key = []

for i in range(0,3):
    key.append(get_key(i))

print("------------------------------------")
print('Enter "exit" to quit.')

while True:

    option = input("Encrypt or Decrypt ? Enter [e/d]: ").lower()
    
    if option == 'e' or option == 'd':
        message = input("Enter a message: ")

        print("Working...\n")
        message = apply_cipher(choice=option, text=message, key_1=key[0], key_2=key[1], key_3=key[2], iterations=5)

        print(f"Processed message: \"{message}\"")
        print("------------------------------------\n")

    elif option == "exit":
        exit()

    else:
        print("Please enter 'e' or 'd'.")
    
