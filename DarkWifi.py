import os

os.system('cls')

def banner() :

    os.system('cls')
    print("\n ██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗    ██╗██╗███████╗██╗ ")   
    print(" ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║    ██║██║██╔════╝██║ ")    
    print(" ██║  ██║███████║██████╔╝█████╔╝     ██║ █╗ ██║██║█████╗  ██║ Author    : M. Farhan")   
    print(" ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║███╗██║██║██╔══╝  ██║ Github    : github.com/mfarhanz1")   
    print(" ██████╔╝██║  ██║██║  ██║██║  ██╗    ╚███╔███╔╝██║██║     ██║ Version   : 1.5")  
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝ Instagram : @mfarhanz1") 
    print(" ═══════════════════════════════════════════════════════════════════════════════════════════════\n")
    print(" [01] Start Attack ")
    print(" [02] Exit\n ")
                                                                







def system() :

    xop = input('Choose One : ')
    if xop =="01" or xop =="1":
        os.system('netsh wlan show profiles')
        xz = input('Enter The Wifi Name : ')
        os.system('netsh wlan show profiles ' + xz + ' key=clear')
        print("")
        xax = input('Use This Tool Again? [Y/n] ')
        if xax =="Y" or xax =="y":
            banner()
            system()
        else:
            os.system('exit')        
    else:
        os.system('exit')

def login() :
    x = input('Username : ')
    y = input('Password : ')
    xy = (x + y)
    if xy =="MFarhanZ1Hanz":
        banner()
        system()
    else:    
        print("\nAkun Yang Anda Masukkan Salah, DM ke Instagram @MFARHANZ1 Untuk Infonya...")

login()        