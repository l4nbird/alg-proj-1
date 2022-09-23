from Fast_Expo_encrypt_decrypt import *

def public_user(e, n, sig, sig_msg):
    loop = True
    valid = False
    enc_msg = None
    while loop != False:
        print("As a public user, what would you like to do?\n       1. Send an encrypted message\n      2. Authenticate a digital signature")
        print("     3. Exit\n")
        selection = input()

        if selection == '1':    
            msg = input("Enter a message: ")
            enc_msg = encode_str(msg, e, n)
            print("Message encrypted and sent.")
        elif selection == '2':
            # authenticate signature using S^e mod n to see if the message is the same
            if (sig == None or sig_msg == None):
                print("There are no signatures to authenticate.")
                continue
            dec_sig = decode_str(sig, e, n)
            if ''.join(to_char(dec_sig)) == sig_msg:
                valid = True

            if valid == True:
                print("Signature is valid.")
            else:
                print(to_char)
                print("Signature is not valid.")
        elif selection == '3':
            # go back to user selection screen
            loop = False
    if enc_msg:
        return enc_msg
    else:
        return None

def owner(n, d, msg):
    loop = True
    sig = None

    while loop != False:
        print("As the owner of the keys, what would you like to do?\n       1. Decrypt a received message\n      2. Digitally sign a message")
        print("     3. Exit\n")
        selection = input()

        if selection == '1':
            dec_msg = decode_str(msg, d, n)
            print("Decrypted message: " + ' '.join(to_char(dec_msg)))
        elif selection == '2':
            # Digitally sign a message
            sig_msg = input("Enter a message: ")
            sig = encode_str(sig_msg, d, n)
            print("Message signed and sent.")
        elif selection == '3':
            # go back to user selection screen
            loop = False
    
    if sig:
        return sig, sig_msg
    else: return None