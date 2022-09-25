from Fast_Expo_encrypt_decrypt import *


# frontend choices for public user type
# offers choice to encrypt message or authenticate a signature
# takes variables for encryption/decryption, a list of encrypted signatures, and a list of original signatures
# returns list of encrypted message
def public_user(e, n, sig, sig_msg):
    # initialize stage
    loop = True
    valid = False
    enc_msg = []

    #loop through choices until exit (3) is called
    while loop != False:
        print("As a public user, what would you like to do?\n       1. Send an encrypted message\n      2. Authenticate a digital signature")
        print("     3. Exit\n")
        selection = input()

        # gather string input, encrypt it, append it to encoded message list, and print confirmation
        if selection == '1':    
            msg = input("Enter a message: ")
            enc_msg.append(encode_str(msg, e, n))
            print("Message encrypted and sent.")
        # see if signature is valid using S^e mod n to see if decoded messsage is the same as original message
        elif selection == '2':
            # if no signature exists, go back to loop
            if (sig == [] or sig_msg == []):
                print("There are no signatures to authenticate.")
                continue
            # list all available signatures, gather input on which, decode it and compare it to original
            else:
                print("The following messages are available:")
                i = 1
                for x in sig:
                    print(str(i) + '. ' + sig_msg[i-1])
                    i += 1
                
                sn = input()
                dec_sig = decode_str(sig[int(sn)-1], e, n)
                if ''.join(to_char(dec_sig)) == sig_msg[int(sn)-1]:
                    valid = True
            # Confirm whether signature is valid
            if valid == True:
                print("Signature is valid.")
            else:
                print(to_char)
                print("Signature is not valid.")
        elif selection == '3':
            # go back to user selection screen
            loop = False
    
    return enc_msg
    
# frontend/handling for owner user type
# offers choice to decrypt a message or create a digital signature
# takes list of encrypted messages as well as variables for encryption/decryption function
# returns list of encrypted signatures and list of original signatures
def owner(n, d, msg):
    # initialization stage
    loop = True
    sig = []
    sig_msg = []

    # loop through choices until exit (3) is called
    while loop != False:
        print("As the owner of the keys, what would you like to do?\n       1. Decrypt a received message\n      2. Digitally sign a message")
        print("     3. Exit\n")
        selection = input()

        # shows list of encrypted messages, designating each by their length
        # takes choice and decrypts and prints the chosen message
        if selection == '1':
            print("Available Encrypted Messages:")
            i = 1
            for x in msg:
                print(str(i) + '. (length = ' + str(len(msg[i-1])) + ')')
                i += 1
            
            sn = input()
            dec_msg = decode_str(msg[int(sn)-1], d, n)
            print("Decrypted message: " + ''.join(to_char(dec_msg)))

        # digital signature creation
        # takes a string, encrypts it, and appends it to list. also appends unencrypted string to a separate list. prints confirmation
        elif selection == '2':
            sig_msg.append(input("Enter a message: "))
            x = len(sig_msg)
            sig.append(encode_str(sig_msg[x-1], d, n))
            print("Message signed and sent.")
        elif selection == '3':
            # go back to user selection screen
            loop = False
    
    return sig, sig_msg