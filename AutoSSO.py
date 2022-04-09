from inspect import Attribute
import os #Run commands
import winreg # Allow access to the windows registry


# Coded by BlackSheep4 - GitHub: https://github.com/BlackSheep4
# Note: Shitty Code, but works :P


print(""" ▄▄▄· ▄• ▄▌▄▄▄▄▄      .▄▄ · .▄▄ ·       
▐█ ▀█ █▪██▌•██  ▪     ▐█ ▀. ▐█ ▀. ▪     
▄█▀▀█ █▌▐█▌ ▐█.▪ ▄█▀▄ ▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ 
▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌
 ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪ ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪""")

print("\n----------------------------------------------\n")


#Show usernames and sid of each one
os.system('wmic useraccount get name,sid')

#Getting the SID of the local user
localuser = input("[!] Put the name of your local user >> ")
localsid = input("[!] Put your SID >> ")

#Getting the SID of the Google User
googleuser = input("Put the username of your new Windows Google Account (should be XX_mediktor) >> ")
googlesid = input("Put the SID of your new Google User >> ")

#Resumen
print("Local User: " + localuser)
print("Local SID User:" + localsid)
print("Google User: " + googleuser)
print("Google SID: " + googlesid)

# Starting to work
choice = input("Is this info correct?[y/n] >> ")

if choice == 'y':
    os.system('cls')
    print('STARTING... \n')

    #Create a new key
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, f"Software\\Google\\GCPW\\Users\\{localsid}")
    print(f"[+] Registry Key: {localsid} created successfully!")
    
    #Copy the key and the content inside of Google SID to the new key with the localusersid
    os.system(f'reg copy HKEY_LOCAL_MACHINE\\SOFTWARE\\Google\\GCPW\\Users\\{googlesid}  HKEY_LOCAL_MACHINE\\SOFTWARE\\Google\\GCPW\\Users\\{localsid} /s')
    print(f"[+] Copying the content from {googlesid} to {localsid}")

    #Delete key of the OLD Google SID Key
    os.system(f'reg delete HKEY_LOCAL_MACHINE\\SOFTWARE\\Google\\GCPW\\Users\\{googlesid}')
    print(f"[+] Deleting old Google Key => {googlesid}")

    #Edit user_name SUBKEY
    os.system(f'reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Google\\GCPW\\Users\\{localsid} /t REG_SZ /v user_name /d {localuser} /f')
    print(f"[+] Editing user_name from {googleuser} to {localuser}")

    ## IN TEST MODE ##

    # Delete google old user
    os.system(f'net user {googleuser} /delete')

    print("REGEDIT EDITED SUCCESSFULLY!")
    input("Press any key to continue...")
    exit(3)
else:
    exit