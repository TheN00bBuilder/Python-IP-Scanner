import os
import time

from subprocess import Popen

devnull = open(os.devnull, 'wb')

ipscanner_ico = '''
#########################################################
#       LOCAL NETWORK IP SCANNER - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : Ismail Tasdelen              #                       
#      	       Translation; TheN00bBuilder		#
#    Dev Mail Address : pentestdatabase@gmail.com	#
#Translator Mail Address : then00bbuilder@overclocked.net#
#Dev LINKEDIN : https://www.linkedin.com/in/ismailtasdelen#
#      Dev  Whatsapp : + 90 534 295 94 31               #
#########################################################
'''

print ipscanner_ico

star = "**********************************************************************"

print star

ip_araligi_deger = raw_input("Choose a range of IPs to search. ( example: 192.168.0 ) ---> ")

print star

print "Scanned IP Range ",ip_araligi_deger 

print star

if ip_araligi_deger == "":
 print star
 print "Hooking on to process... hold on..."
 print star

import sys

p = []
aktif = 0
yanit_yok = 0
pasif = 0

for aralik in range(0,255):
    ip = ip_araligi_deger + ".%d" % aralik
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s Active' % ip)
                aktif = aktif + 1
            elif proc.returncode == 2:
                print('%s No Response' % ip)
                aktif = yanit_yok + 1
            else:
                print('%s Inactive' % ip)
                pasif = pasif + 1
    time.sleep(.04)
devnull.close()

print star

print "LOCAL NETWORK IP SCANNER. By GH0ST-SOFTWARE."

print star

import os

print "Current Operating System",os.name
print "Final Status Report"
print "Active IP Count  [ ",aktif," ]"
print "Inactive IP Count  [ ",pasif," ]"
print "No Response Count  [ ",yanit_yok," ]"

print star

bitis_mesaj = "Scan complete. Happy hacking!"

print bitis_mesaj

print star
