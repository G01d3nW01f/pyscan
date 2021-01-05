import os
import sys
import re
import portscan
import subprocess

def init():

    logo = """
    
     ____                            
    |  _ \ _   _ ___  ___ __ _ _ __  
    | |_) | | | / __|/ __/ _` | '_ \ 
    |  __/| |_| \__ \ (_| (_| | | | |
    |_|    \__, |___/\___\__,_|_| |_|
           |___/                     


    """
    print(logo)
    
    portscan.init()

def check_root():
    
    if os.getuid() != 0:
        print("[!]You must be root, say magic word: sudo!!!!")
        sys.exit()

def usage():

    if len(sys.argv) == 2:
        
        print("")

    else:

        info = """

        <Usage>

            python3 pyscan.py <host> or <ip>

        <example>

            python3 pyscan.py <vitcim.com> or <192.168.0.1>

        """

        print(info)
        sys.exit()
    

def main():

    
    host = sys.argv[1]

    open_ports = portscan.execute(host)
    
    counter = 0
    text = ""
    for i in open_ports:
        counter += 1
        
        text += str(i)

        if len(open_ports) != counter:

            text += ","

    payload = f"sudo nmap -A -vvv -p {text} {host}"

    result = subprocess.getoutput(payload)
    
    array = result.split("\n")
    os.system("clear")
    print("+-------------------------+")
    print("|Result of Open Ports Scan|")
    print("+-------------------------+")

    print(f"<Target: > {host}")

    for i in array:
        reg = re.search(r"^\d{1,5}/.+",str(i))
        
        if reg != None:
            print(reg.group())


if __name__ == "__main__":

    init()
    check_root()
    usage()
    main()

