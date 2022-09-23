from Fast_Expo_encrypt_decrypt import *

def public_user(e, n, sig, sig_msg):
    loop = True
    valid = False
    enc_msg = []
    while loop != False:
        print("As a public user, what would you like to do?\n       1. Send an encrypted message\n      2. Authenticate a digital signature")
        print("     3. Exit\n")
        selection = input()

        if selection == '1':    
            msg = input("Enter a message: ")
            enc_msg.append(encode_str(msg, e, n))
            print("Message encrypted and sent.")
        elif selection == '2':
            # authenticate signature using S^e mod n to see if the message is the same
            if (sig == [] or sig_msg == []):
                print("There are no signatures to authenticate.")
                continue
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

            if valid == True:
                print("Signature is valid.")
            else:
                print(to_char)
                print("Signature is not valid.")
        elif selection == '3':
            # go back to user selection screen
            loop = False
    
    return enc_msg
    

def owner(n, d, msg):
    loop = True
    sig = []
    sig_msg = []

    while loop != False:
        print("As the owner of the keys, what would you like to do?\n       1. Decrypt a received message\n      2. Digitally sign a message")
        print("     3. Exit\n")
        selection = input()

        if selection == '1':
            print("Available Encrypted Messages:")
            i = 1
            for x in msg:
                print(str(i) + '. (length = ' + str(len(msg[i-1])) + ')')
                i += 1
            
            sn = input()
            dec_msg = decode_str(msg[int(sn)-1], d, n)
            print("Decrypted message: " + ''.join(to_char(dec_msg)))
        elif selection == '2':
            # Digitally sign a message
            sig_msg.append(input("Enter a message: "))
            x = len(sig_msg)
            sig.append(encode_str(sig_msg[x-1], d, n))
            print("Message signed and sent.")
        elif selection == '3':
            # go back to user selection screen
            loop = False
    
    return sig, sig_msg