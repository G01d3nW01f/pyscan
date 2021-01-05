import socket
from colorama import Fore as fore
from threading import Thread, Lock
from queue import Queue
import os

def init():

    print("portscanner_module [OK]")



def execute(host):
    N_THREADS = 400
    
    global q
    q = Queue()
    
    print_lock = Lock()
    
    global open_ports
    open_ports = []
    

    def portscan(port):

        try:
            s = socket.socket()
            s.connect((host,port))

        except:

            with print_lock:
                print(f"{fore.LIGHTBLACK_EX}{host:15} : {port:5} {fore.RESET}",end='\r')

        else:

            with print_lock:
                print(f"{fore.GREEN}{host:15} : {port:5} is open {fore.RESET}")
                open_ports.append(port)

        finally:
            s.close()
    
    def scan_thread():
        global q
        while True:

            worker = q.get()
            portscan(worker)
            q.task_done()

    def main(host,ports):

        global q

        for t in range(N_THREADS):
            t = Thread(target=scan_thread)
            
            t.daemon = True

            t.start()

        for worker in ports:

            q.put(worker)

        q.join

    print(f"{fore.RED}[+]Target: {host}")

 
    #print("Enter the range for scan Default: 1-1024")
    #port_range = 1-65535

       
    #try:

    #    start,end = port_range.split("-")
    #    start,end = int(start),int(end)
    
    #    global ports
    #    ports = [p for p in range(start,end)]
    
    #except:

    start = "1"
    end   = "65535"

        
    ports = [p for p in range(int(start),int(end))]


    main(host,ports)
    print("--------------------------------")
    print("--------------------------------")
    #os.system("clear")


    print("[Wait......]")
    return open_ports
