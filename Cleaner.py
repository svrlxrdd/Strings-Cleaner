import sys, time, os, shutil
import pyfiglet

#bypass names as login
os.system('@title Login for cleaner.' + ' && cls')

#define clear function
clear = lambda: os.system("cls")

#login input
username = input("User: ")
password = input("Pass: ")

#Login checker
def checklogin(username, password):
    if username == 'root' and password == 'root':
        pass
    else:
        #Failed logins will delete the cleaner. but make a backup of it in a selected file location.
        print("Incorrect login deleting file...")
        original = 'svCleaner.py'
        target = r'Location\filename.py'
        shutil.copyfile(original, target)
        os.remove('svCleaner.py')
        print("File removed L.")

#try except incase they input retarded shit
try:
    checklogin(username, password)
except Exception as e:
    print(e)
    time.sleep(2)
    clear()
    loading2()

#banner
def banner():
    text = pyfiglet.figlet_format('sv Cleaner', font="alligator").replace("\n", "\n\t\t")
    print("\n\t\t" + text)

#Loading to next thing.
def loading():
    spinsymbol = ['|', '/', '-']
    for i in spinsymbol + spinsymbol + spinsymbol:
        sys.stdout.write('\r' + '[+]' + i)
        sys.stdout.flush()
        time.sleep(0.2)

#Loading exit
def loading2():
    spinsymbol = ['|', '/', '-']
    for i in spinsymbol + spinsymbol + spinsymbol:
        sys.stdout.write('\r' + '[-]' + i)
        sys.stdout.flush()
        time.sleep(0.2)

#Loading cleaner
def loading3(string):
    spinsymbol = ['.', '..', '...']
    string = ''
    for i in spinsymbol + spinsymbol + spinsymbol:
        sys.stdout.write('\r' + string + i)
        sys.stdout.flush()
        time.sleep(0.2)

#Defines the rename, copy, delete function for ss bypassing.
def clearstrings():
    clear()
    string = 'Renaming '
    loading3(string)
    os.rename(r'current file location of cheat',r'where to put file and what to rename it to use complete file directory')
    print('Renamed')
    string = 'Copying '
    loading3(string)
    original = r'File location of what you want to put in place of the cheat'
    
    #Below(This should be the same as the location of your cheat)(ss bypass)
    target = r'location\filename.exe'
    shutil.copyfile(original, target)
    print('Copied')
    time.sleep(2)
    clear()
    print("Cleared Strings")
    time.sleep(1)
    main()

#Runs CCleaner (NOT FOR SS YOU WILL BE BANNED FOR USING CCLEANER BEFORE AN SS)
def runccleaner():
    os.startfile(r'ccleaner file location')
    clear()
    main()

#after ss renames the file back to orignal
def reverserename():
    clear()
    #Deletes copy file that you put in place of your cheat.
    string = 'Deleting Copy '
    loading3(string)
    os.remove(r'FILE LOCATION OF THE COPY(WHATEVER THE COPY YOU MADE IS NAMED AS)')
    print('Deleted Copy')
    string = 'Renaming '
    loading3(string)
    
    #Below (Whatever your original file location is.)
    os.rename(r'your renamed cheat.exe',r'WHAT YOU WANT IT TO BE RENAMED BACK TO')
    print('Renamed')

#Prints options
def options():
    print('\n')
    print('Anything else to exit')
    print("\n\t\t"+"[1]Clear Strings"+"\t"+"[2]CCleaner"+"\t"+"[3]Reverse Rename")

#Option input
def cleanoptions(number):
    if number == 1:
        clearstrings()
    elif number == 2:
        runccleaner()
    elif number == 3:
        reverserename()
    else:
        print('Unable to process your input')
        time.sleep(2)
        loading2()
        sys.exit()
    main()

#Clears and loads into the main function
def startingmain():
    clear()
    loading()

#Main function loop for inf input.
def main():
#after login checked renames to actual thing.
    os.system('@title sv Cleaner' + ' ^|^ BYPASS ALL SSES ' + ' && cls')
    clear()
    banner()
    options()
    number = int(input('@' + username + ': '))
    cleanoptions(number)

startingmain()
main()
